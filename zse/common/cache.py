from zse.common import logging
from flask import g, has_request_context
import functools

# These variables are only used when outside the Flask request context - i.e. in tasks / scripts
_simple_bank = {}
_skip_cache = False

log = logging.getLogger()


def __is_cache_skipped():
    if has_request_context():
        return g.get('skip_cache', False)
    else:
        return _skip_cache


def __get_cache_bank():
    if has_request_context():
        return g
    else:
        return _simple_bank


def __make_key(*args, **kwargs):
    key_args = '_'.join([str(arg) for arg in args])
    key_kwargs = '_'.join('='.join((str(k), str(v))) for k, v in sorted(kwargs.items()))
    key = 'cache_%s' % '_'.join((key_args, key_kwargs))
    return key


def put_cache(key, value):
    cache = __get_cache_bank()
    cache[key] = value


def get_cache(key):
    if __is_cache_skipped():
        return None
    cache = __get_cache_bank()
    return cache.get(key, None)


def has_cache(key):
    if __is_cache_skipped():
        return False
    cache = __get_cache_bank()
    return key in cache


def disable_cache_for_request():
    global _skip_cache
    log.warn('Cache disabled for this request - This may cause performance issues')
    if has_request_context():
        g['_skip_cache'] = True
    else:
        _skip_cache = True


def cached(f):
    @functools.wraps(f)
    def wrap(*args, **kwargs):
        key = __make_key(f.__name__, *args, **kwargs)
        if not has_cache(key):
            ret = f(*args, **kwargs)
            if not __is_cache_skipped():
                put_cache(key, ret)
        else:
            ret = get_cache(key)
        return ret
    return wrap
