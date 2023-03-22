from flask import Flask, request

from app.services.user_service import UserService


app = Flask(__name__)

@app.route('/')
def index():
    return "hello"


@app.route('/users', methods=['POST'])
def postUsers():

    request_params = request.get_json()
    if 'data' not in request_params:
        raise Exception("include data to insert")
    service = UserService()
    service.insert_users(request_params['data'])

    return "success"

@app.route('/users/<id>', methods=['GET'])
def getUser(id):
    service = UserService()
    user = service.retrieve_user_with_id(int(id))

    return [user]

@app.route('/users/search', methods=['POST'])
def searchUser():
    request_params = request.get_json()

    service = UserService()
    users = service.search_users(request_params)

    return users
