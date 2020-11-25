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

<<<<<<< HEAD
=======
#for pytest
# app.config['MONGODB_SETTINGS'] = {
#     'host': 'mongodb://localhost/User-test'
# }
>>>>>>> 48340382ef8281ae3a621d3983a13a68de3dd902
app.config['PROPAGATE_EXCEPTIONS'] = False

initialize_db(app)
initialize_routes(api)

app.run(debug=True)
