from zse import query
from zse.common.flask import app
from flask import jsonify


@app.get('/nav/preferred_routes')
def preferred_routes():
    data = [{
        'departure': x.departure_airport,
        'arrival': x.arrival_airport,
        'route': x.route
    } for x in query.navigation.get_preferred_routes()]
    return jsonify(data)
