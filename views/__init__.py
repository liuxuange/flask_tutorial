from flask import jsonify


def create_response_body(data):
    body = {'counts': 1, 'datas': data}
    if isinstance(data, (list, tuple)):
        body['counts'] = len(data)
    return jsonify(body)
