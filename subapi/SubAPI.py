from flask import Blueprint, request, jsonify, session

api = Blueprint('some_name', 'subapi', url_prefix='/api')

@api.route('/polls', methods=['GET', 'POST'])
# retrieves/adds polls from/to the database
def api_polls():
    return "<h1>{}</h1>".format(request.method)