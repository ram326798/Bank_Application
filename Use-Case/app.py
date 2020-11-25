from flask import Flask
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
from resources.errors import errors

app = Flask(__name__)
# In App.py we are connecting with database and initialising db and routes

api = Api(app, errors=errors)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/User'
}

app.config['PROPAGATE_EXCEPTIONS'] = False

initialize_db(app)
initialize_routes(api)

app.run(debug=True)