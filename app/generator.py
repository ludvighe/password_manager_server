import uuid  
import random
import string
from app.db.crud_interface import CrudInterface

def gen_id(of_type, database:CrudInterface):
    if of_type == 'user':
        while True:
            id = 'U' + str(uuid.uuid4())
            user = database.read_user(id)
            if user == None:
                return id
    elif of_type == 'password_data':
        while True:
            id = 'PWD' + str(uuid.uuid4()) 
            pwdata = database.read_password_data(id)
            if pwdata == None:
                return id
    else:
        raise Exception(f'Argument of_type [={of_type}] is not valid.')

def gen_key(database):
    while True:
        key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))
        user = database.read_user_from_key(key)
        if user == None:
            return key