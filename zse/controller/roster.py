from zse import query
from zse.common.constants import ControllerRating
from zse.common.flask import app
from flask import jsonify


@app.get('/roster')
def get_roster():
    controller_result = query.controller.get_active_controllers()
    roster = {
        "stats": get_stats(controller_result),
        "controllers": [get_controller_entity(row) for row in controller_result]
    }
    return jsonify(roster)


def get_stats(results):
    stats = {}
    for rating in ControllerRating:
        stats[rating.name] = {
            'rating': rating.name,
            'home': 0,
            'visitor': 0
        }
    for row in results:
        if row.is_visitor:
            stats[row.rating]['visitor'] += 1
        else:
            stats[row.rating]['home'] += 1
    result = []
    total = {
        'rating': 'Total',
        'home': 0,
        'visitor': 0,
        'total': 0
    }
    for rating in ControllerRating:
        stats[rating.name]['total'] = stats[rating.name]['visitor'] + stats[rating.name]['home']
        total['home'] += stats[rating.name]['home']
        total['visitor'] += stats[rating.name]['visitor']
        total['total'] += stats[rating.name]['total']
        result.append(stats[rating.name])
    result.append(total)
    return result


def get_controller_entity(row):
    entity = {
            'cid': row.vatsim_cid,
            'display_name': row.display_name,
            'initials': row.initials,
            'rating': row.rating,
            'is_visitor': row.is_visitor,
            'facility': row.facility,
            'is_loa': row.loa is not None,
            'loa_end_date': row.loa.end_date if row.loa is not None else None,
            'staff_position': row.staff.staff_position if row.staff is not None else None,
            'positions': {
                'delivery': row.positions.delivery,
                'ground': row.positions.ground,
                'tower': row.positions.tower,
                'approach': row.positions.approach,
                'center': row.positions.center
            } if row.positions is not None else {}
        }
    return entity
