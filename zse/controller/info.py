from zse import query
from zse.common.flask import app
from flask import jsonify


@app.get('/info/news')
def news():
    data = [{
        'news_id': x.news_id,
        'message': x.message,
        'link': x.link,
        'post_date': x.post_date
    } for x in query.info.get_recent_news(50)]
    return jsonify(data)


@app.get('/info/notams')
def notams():
    data = [{
        'notam_id': x.notam_id,
        'message': x.message,
        'link': x.link,
        'post_date': x.post_date
    } for x in query.info.get_notams()]
    return jsonify(data)


@app.get('/info/staff')
def staff():
    data = [{
        'vatsim_cid': x.Controller.vatsim_cid,
        'display_name': x.Controller.display_name,
        'staff_position': x.Staff.staff_position,

    } for x in query.info.get_staff()]
    return jsonify(data)
