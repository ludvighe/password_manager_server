from flask import request

from app.models.user import User
from app.models.password_data import PasswordData
from app.db.crud_interface import CrudInterface
import app.views.static.messages as messages

class PasswordDataView:
    # Requres Flask app reference (app) and reference to database module (db)
    def __init__(self, app, db:CrudInterface):
        @app.route('/pwdata', methods=['POST','GET', 'PUT', 'DELETE'])
        def password_data():
            
            # Parameter check
            if 'key' not in request.args: return messages.missing_params_error

            # Key verification
            if not db.verify_key(request.args['key']): return messages.key_verification_error
            user = User(sqlite=db.read_user_from_key(request.args['key']))

            # Request methods
            if request.method == 'POST':
                try:
                    pwdata = PasswordData.fromJson(request.json, user.id, db)
                    db.create_password_data(pwdata)
                    return messages.message(pwdata.id)
                except:
                    return messages.error('could not create password data')

            elif request.method == 'GET':
                if 'id' in request.args:
                    try:
                        pwdata = PasswordData(sqlite=db.read_password_data(request.args['id']))
                        return pwdata.toJson()
                    except:
                        return messages.not_found_error('Password Data')
                else:
                    pwdata_list = db.read_users_password_data(user.id)
                    json = {}
                    for index in range(len(pwdata_list)):
                        pwdata = PasswordData(sqlite=pwdata_list[index])
                        json[index] = {index: pwdata.toJson()}
                    return json
            
            elif request.method == 'PUT':
                try:
                    db.update_password_data(PasswordData.fromJson(request.json, user.id))
                    return messages.success_message
                except:
                    return messages.error('could not update password data')
            elif request.method == 'DELETE':
                try:
                    db.delete_password_data(request.args['id'])
                    return messages.success_message
                except:
                    return messages.error('could not delete password')
            else:
                return messages.invalid_request_error
