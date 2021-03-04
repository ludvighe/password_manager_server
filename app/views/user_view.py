from flask import request

import app.views.static.messages as messages
from app.models.user import User
from app.db.crud_interface import CrudInterface

class UserView:
    # Requres Flask app reference (app) and reference to database module (db:CrudInterface)
    def __init__(self, app, db:CrudInterface):
        @app.route('/user', methods=['GET', 'PUT', 'DELETE'])
        def get_user():
            
            # Parameter check
            if 'key' not in request.args: return messages.missing_params_error

            # Key verification
            if not db.verify_key(request.args['key']): return messages.key_verification_error
            user = User(sqlite=db.read_user_from_key(request.args['key']))

            # Request methods
            if request.method == 'GET':
                return user.toJson()
            
            elif request.method == 'PUT':
                try:
                    exists_check = db.exists_in_users(request.json['name'], request.json['email'])
                    if request.json['name'] != user.name:
                        if exists_check[0] == 1: return messages.already_exists_error('Name')
                    if request.json['email'] != user.email:
                        if exists_check[1] == 1: return messages.already_exists_error('Email')

                    user.name = request.json['name']
                    user.email = request.json['email']
                    db.update_user(user) 
                    return messages.success_message 
                except:
                    return messages.error('could not update user')

            elif request.method == 'DELETE':
                try:
                    db.delete_user(user.id) 
                    return messages.success_message 
                except:
                    return messages.error('could not delete user')

            else:
                return messages.invalid_request_error
        
        @app.route('/register', methods=['POST'])
        def register():
            if request.method == 'POST':
                try:
                    exists_check = db.exists_in_users(request.json['name'], request.json['email'])
                    if exists_check[0] == 1: return messages.already_exists_error('Name')
                    if exists_check[1] == 1: return messages.already_exists_error('Email')

                    user = User.fromJson(request.json, db)
                    db.create_user(user)
                    return messages.message(user.key)
                except:
                    return messages.error('could not create user')
            else:
                return messages.invalid_request_error