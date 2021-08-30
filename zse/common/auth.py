from zse.common.constants import Permission
from zse.common import logging
from zse.common.flask import error
from zse.query.staff import get_staff_by_cid
import base64
from datetime import datetime, timedelta
from flask import abort, request
from functools import wraps
import jwt
from typing import List

ALG = "HS256"
SECRET = "c2VjcmV0"  # TODO - Change Me
ISS = 'ZSE'
AUD = 'ZSE'
EXP_MINS = 20

log = logging.getLogger()


def require_login(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        get_user_id()
        return f(*args, **kwargs)
    return wrap


def guard(permissions):
    if not isinstance(permissions, list):
        permissions = [permissions]

    def decorator(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            if not check_permissions(permissions):
                error('Forbidden', 403)
            return f(*args, **kwargs)
        return wrap
    return decorator


def check_permissions(permissions: List[Permission], *, strict=False):
    if not strict and get_request_permission(Permission.ADM):
        return True  # ADM counts as all permissions -- unless strict
    for permission in permissions:
        if get_request_permission(permission):
            return True
    log.debug("Permission %r is required, but not granted [strict: %s]"
              % ([permission.name for permission in permissions], strict))
    return False


def assert_request_has_permission(permission: Permission, *, strict=False):
    if not strict and get_request_permission(Permission.ADM):
        return  # ADM counts as all permissions -- unless strict
    if get_request_permission(permission):
        return
    raise NotAuthorizedException("Permission %s is required, but not granted [strict: %s]" % (permission.name, strict))


def get_request_permission(permission: Permission):
    return get_request_jwt().get(permission.value, False)


def get_user_id():
    data = get_request_jwt()
    return data.get('sub')


def make_token_json(cid):
    staff = get_staff_by_cid(cid)
    return {
        'iss': ISS,
        'aud': AUD,
        'sub': cid,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=EXP_MINS),
        'zse_adm': staff.is_admin if staff is not None else False,
        'zse_ins': staff.is_instructor if staff is not None else False,
        'zse_mtr': staff.is_mentor if staff is not None else False,
        'zse_ta': staff.is_training_administrator if staff is not None else False,
        'zse_ec': staff.is_event_coordinator if staff is not None else False,
        'zse_fe': staff.is_facility_engineer if staff is not None else False
    }


def make_jwt(cid):
    secret = base64.urlsafe_b64decode(SECRET + '=' * (-len(SECRET) % 4))
    data = make_token_json(cid)
    return jwt.encode(data, secret, algorithm=ALG)


def get_request_jwt():
    secret = base64.urlsafe_b64decode(SECRET + '=' * (-len(SECRET) % 4))
    header = request.headers.get('Authorization', None)
    if header is None:
        error('Authorization required', 401)
    header_parts = header.split(' ')
    type = header_parts[0]
    token = header_parts[1]
    if len(header_parts) > 2:
        error('Invalid Authorization format', 400)
    if type != 'Bearer':
        error('Invalid Authorization type', 400)
    try:
        return jwt.decode(token, secret, algorithms=["HS256", "HS512"], audience=[AUD], issuer=ISS, leeway=30)
    except jwt.exceptions.ExpiredSignatureError:
        error('Invalid token', 400)


class AuthenticationException(Exception):
    pass


class NotAuthorizedException(Exception):
    pass
