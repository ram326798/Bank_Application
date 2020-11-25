from flask_mongoengine import MongoEngine

db = MongoEngine()
# importing and intialising database
def initialize_db(app):
    db.init_app(app)