import unittest
import json
from app import app
from database.db import db

class BaseCase(unittest.TestCase):
<<<<<<< HEAD
# we are invoking test db 
=======

>>>>>>> 48340382ef8281ae3a621d3983a13a68de3dd902
    def setUp(self):
        self.app = app.test_client()
        self.db = db.get_db()

<<<<<<< HEAD
# After running all test cases to destroy test database automatically we use teardown
    def tearDown(self):
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)
=======

    def tearDown(self):
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)
>>>>>>> 48340382ef8281ae3a621d3983a13a68de3dd902
