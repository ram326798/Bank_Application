<<<<<<< HEAD
from .db import db

# defining Document Structure in a collection
class User(db.Document):
    username = db.StringField(required=True, unique=True, min_length=6)
    password = db.StringField(required=True,min_length=6)
    address = db.StringField(required=True)
    state = db.StringField(required=True)
    country = db.StringField(required=True)
    emailAddress = db.EmailField(required=True)
    pan = db.StringField(required=True, min_length=6,max_length=10)
    contactNo = db.IntField(required=True,min_length=10,max_length=12)
    DOB = db.StringField(required=True)
    accountType = db.StringField(required=True)    
     
# defining Document structure in a collection
class Loan(db.Document):
    username=db.StringField(required=True)
    loan_type = db.StringField(required=True, min_length=3)
    loan_Amount = db.FloatField(required=True, min_length=4)
    date=db.StringField(required=True)
    rate_of_interest = db.IntField(required=True, min_length=1)
=======
from .db import db


class User(db.Document):
    username = db.StringField(required=True, unique=True, min_length=6)
    password = db.StringField(required=True,min_length=6)
    address = db.StringField(required=True)
    state = db.StringField(required=True)
    country = db.StringField(required=True)
    emailAddress = db.EmailField(required=True)
    pan = db.StringField(required=True, min_length=6,max_length=10)
    contactNo = db.IntField(required=True,min_length=10,max_length=12)
    DOB = db.StringField(required=True)
    accountType = db.StringField(required=True)    
     

class Loan(db.Document):
    username=db.StringField(required=True)
    loan_type = db.StringField(required=True, min_length=3)
    loan_Amount = db.FloatField(required=True, min_length=4)
    date=db.StringField(required=True)
    rate_of_interest = db.IntField(required=True, min_length=1)
>>>>>>> 48340382ef8281ae3a621d3983a13a68de3dd902
    duration_of_loan = db.IntField(required=True, min_length=1)