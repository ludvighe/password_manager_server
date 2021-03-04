import os
import sqlite3

class CrudInterface:

    # CRUD user
    def create_user(self, user): pass
    def read_user(self, id): pass
    def read_user_from_key(self, key): pass
    def update_user(self, user): pass
    def delete_user(self, id): pass
    def exists_in_users(self, key, value): pass

    # CRUD password_data
    def create_password_data(self, pwdata): pass
    def read_password_data(self, id): pass
    def read_users_password_data(self, usr_id): pass
    def update_password_data(self, pwdata): pass
    def delete_password_data(self, id): pass    
    def delete_all_password_data(self, usr_id): pass
   
    # Verification
    def verify_key(self, key): pass