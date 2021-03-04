import os
import sqlite3

from app.db.crud_interface import CrudInterface

class CrudSqlite(CrudInterface):
    def __init__(self):
        self.basedir = os.path.abspath(os.path.dirname(__file__))
        self.db_path = 'app/db/db.sqlite'

    def __execute_query(self, query, values):
        # print('Reading from ' + self.db_path)
        print('Query: ' + query)
        print('Values: ' + str(values))

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, values)
            conn.commit()
            return cursor.fetchall()




    # CRUD user
    def create_user(self, user):
        self.__execute_query(
            "INSERT INTO users (id, key, name, email) VALUES (?, ?, ?, ?);", 
            user.var_list(order='insert')
        )

    def read_user(self, id):
        try:
            return self.__execute_query(
                "SELECT * FROM users WHERE id = ?;", 
                [id]
            )[0] # Only expecting one => Only selecting first
        except:
            return None
    
    def read_user_from_key(self, key):
        try:
            return self.__execute_query(
                "SELECT * FROM users WHERE key = ?;", 
                [key]
            )[0] # Only expecting one => Only selecting first
        except:
            return None

    def update_user(self, user):
        self.__execute_query(
            "UPDATE users SET key = ?, name = ?, email = ? WHERE id = ?;", 
            user.var_list(order='update')
        )
    
    def delete_user(self, id):
        self.__execute_query(
            "DELETE FROM password_data WHERE usr_id = ?;", 
            [id]
        )
        self.__execute_query(
            "DELETE FROM users WHERE id = ?;", 
            [id]
        )
    
    def exists_in_users(self, name, email):
        name_exists = self.__execute_query(
            "SELECT EXISTS(SELECT * FROM users WHERE name = ?);", 
            [name]
        )[0][0]

        email_exists = self.__execute_query(
            "SELECT EXISTS(SELECT * FROM users WHERE email = ?);", 
            [email]
        )[0][0]
        return [name_exists, email_exists]

    # CRUD password_data
    def create_password_data(self, pwdata):
        self.__execute_query(
            "INSERT INTO password_data (id, usr_id, title, salt, count, length, created, last_used) VALUES (?, ?, ?, ?, ?, ?, ?, ?);", 
            pwdata.var_list(order='insert')
        )

    def read_password_data(self, id):
        try:
            return self.__execute_query(
                "SELECT * FROM password_data WHERE id = ?;", 
                [id]
            )[0] # Only expecting one => Only selecting first
        except:
            return None

    def read_users_password_data(self, usr_id):
        try:
            return self.__execute_query(
                "SELECT * FROM password_data WHERE usr_id = ?;", 
                [usr_id]
            )
        except:
            return None

    def update_password_data(self, pwdata):
        self.__execute_query(
            "UPDATE password_data SET usr_id = ?, title = ?, salt = ?, count = ?, length = ?, created = ?, last_used = ? WHERE id = ?", 
            pwdata.var_list(order='update')
        )

    def delete_password_data(self, id):
        self.__execute_query(
            "DELETE FROM password_data WHERE id = ?;", 
            [id]
        )
    
    def delete_all_password_data(self, usr_id):
        self.__execute_query(
            "DELETE FROM password_data WHERE usr_id = ?;", 
            [usr_id]
        )

   
    # Verification
    def verify_key(self, key):
        if self.read_user_from_key(key) != None:
            return True
        else:
            return False