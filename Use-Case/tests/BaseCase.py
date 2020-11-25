import unittest
import json
from app import app
from database.db import db

class BaseCase(unittest.TestCase):
# we are invoking test db 
    def setUp(self):
        self.app = app.test_client()
        self.db = db.get_db()

# After running all test cases to destroy test database automatically we use teardown
    def tearDown(self):
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)