# For testing features, classes and functionality in/of this app

import json
import traceback
import sqlite3

from app.models.user import User
from app.models.password_data import PasswordData
from app.db.crud_sqlite import CrudSqlite
import app.generator as gen

### UNIQUE GENERATION ###

def id_gen(verbose):
    print('\nTESTING: Unique Generation')

    db = CrudSqlite()

    if verbose: print('\n- id')
    if verbose: print('User ID: ' + gen.gen_id('user', db))
    if verbose: print('Password Data ID: ' + gen.gen_id('password_data', db))
    
    if verbose: print('\n- key')
    if verbose: print('Key: ' + gen.gen_key(db))

    print('Unique Generation PASSED')


### DATABASE ###

def database(verbose):
    print('\nTESTING: Database:')

    db = CrudSqlite()
    usr_id = gen.gen_id('user', db)
    pw_id = gen.gen_id('password_data', db)
    key = gen.gen_key(db)

    
    if verbose: print('\n- db.create')
    db.create_user(User(
        id=usr_id, 
        key=key, 
        name='name-2', 
        email='email-2'))


    db.create_password_data(PasswordData(
        id=pw_id, 
        usr_id='usr_id-2', 
        title='title-2', 
        salt='salt-2', 
        count=16, 
        length=16, 
        created='created-2', 
        last_used='last_used-2'))
    if verbose: print('passed')

    if verbose: print('\n- db.read')
    user = db.read_user(usr_id)
    if verbose: print('User: ' + str(user))
    pwdata = db.read_password_data(pw_id)
    if verbose: print('Password Data: ' + str(pwdata))
    if user == None: raise Exception(f'Could not read user [{usr_id}]')
    if pwdata == None: raise Exception(f'Could not read Password Data [{pw_id}]')
    if verbose: print('passed')

    if verbose: print('\n- db.update')

    updated_name = 'name-2-updated'
    db.update_user(User(
        id=usr_id, 
        key=key, 
        name=updated_name, 
        email='email-2'))
    user = User(sqlite=db.read_user(usr_id))
    if (user.name != updated_name): raise Exception(f'Update User name failed.\nExpected: {updated_name}\tRecieved: {user.name}')

    updated_title = 'title-2-updated'
    db.update_password_data(PasswordData(
        id=pw_id, 
        usr_id=usr_id, 
        title=updated_title, 
        salt='salt-2', 
        count=16, 
        length=16, 
        created='created-2', 
        last_used='last_used-2'))
    pwdata = PasswordData(sqlite=db.read_password_data(pw_id))
    if (pwdata.title != updated_title): raise Exception(f'Update Password Data title failed.\nExpected: {updated_title}\tRecieved: {pwdata.title}')
    if verbose: print('passed')

    if verbose: print('\n- delete')
    db.delete_user(usr_id)
    db.delete_password_data(pw_id)
    
    try:
        user = User(sqlite=db.read_user(usr_id))
        raise Exception(f'Delete User [{usr_id}] failed')
    except:
        pass
    try:
        pwdata = PasswordData(sqlite=db.read_password_data(pw_id))
        raise Exception(f'Delete Password Data [{pw_id}] failed')
    except:
        pass

    if verbose: print('passed')

    print('Database PASSED')


### MDOELS ###

def models(verbose):
    print('\nTESTING: models')

    user = User(id='usr_id-2', key='key', name='name-2', email='email-2')
    pwdata = PasswordData(id='pwid-2', usr_id='usr_id-2', title='title-2', salt='salt-2', count=16, length=16, created='created-2', last_used='last_used-2')
    
    print('Models PASSED')


def launch_test(verbose=False):
    print('=================================================')
    print('LAUNCHING APP TEST')
    models(verbose)
    id_gen(verbose)
    database(verbose)
    print('\nAPP TEST DONE')
    print('=================================================')