import config
import app.tests.app_test as app_test

conf = config.Config()
if conf.TESTING: app_test.launch_test(verbose=conf.TESTING_VERBOSE)

from flask import Flask, request, jsonify
import os

from app.db.crud_sqlite import CrudSqlite

from app.views.home_view import HomeView
from app.views.user_view import UserView
from app.views.password_data_view import PasswordDataView

# Init app
app = Flask(__name__)

# Init database
db = CrudSqlite()

# Init Views
HomeView(app)
UserView(app, db)
PasswordDataView(app, db)


# Run server
if __name__ == '__main__':
    if conf.DEBUG:
        # Run locally with debug
        app.run(debug=conf.DEBUG)
    else:
        # Run production without debug (Available on LAN)
        app.run(debug=conf.DEBUG, host='0.0.0.0', port=5000)
