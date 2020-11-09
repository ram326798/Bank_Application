import unittest
import json

from app import app
from database.db import db


class SignupTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = db.get_db()
    
    def test_SignupApi(self):
        # Given
        payload = json.dumps({
	            "username":"ramakrishna",
                "password":"ramakrishna",
                "address":"8/121,p.k. ramaya street,jammalamadugu",
                "state":"andhrapradesh",
                "country":"India",
                "emailAddress":"chimmaniramakrishna25@gmail.com",
                "pan":"CWEPR7923F",
                "contactNo":9440921058,
                "DOB":"17/12/1995",
                "accountType":"savings"
                        })

        # When
        response = self.app.post('/accounts/signup', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        
        self.assertEqual(200, response.status_code)

    def test_LoginApi(self):
        #given
        
        payload = json.dumps({
                    "username" : "ramakrishna",
                     "password" : "ramakrishna"
                    })
       # When
        response = self.app.post('/accounts/login', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(200, response.status_code)
    
    def test_LoginApi3(self):
        #given

        payload = json.dumps(
                {
                "username":"krishna",
                "password":"krishna",
                "address":"8/121,p.k. ramaya street,jammalamadugu",
                "state":"andhrapradesh",
                "country":"India",
                "emailAddress":"chimmaniramakrishna25@gmail.com",
                "pan":"CWEPR7923F",
                "contactNo":9440921058,
                "DOB":"17/12/1995",
                "accountType":"savings" 
                    })


       # When
        response = self.app.put('/accounts/login/5fa914d0c5088d93fab6e5df', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(201, response.status_code)    
    def test_LoginApi4(self):
        #given

        payload = json.dumps(
                {
                "username":"krishna",
                "password":"krishna",
                "address":"8/121,p.k. ramaya street,jammalamadugu",
                "state":"andhrapradesh",
                "country":"India",
                "emailAddress":"chimmaniramakrishna25@gmail.com",
                "pan":"CWEPR7923F",
                "contactNo":9440921058,
                "DOB":"17/12/1995",
                "accountType":"savings"  
                    })


       # When
        response = self.app.put('/accounts/login/5fa914d0c5088d93fab6e5df', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(500, response.status_code)    

    

    def test_LoanApi(self):
        #given

        payload2 = json.dumps({
                    
                    "username" : "krishna",
                    "loan_type" : "Bike loan",
                    "loan_Amount": 200000,
                    "date": "17/12/1995",
                    "rate_of_interest" :1,
                    "duration_of_loan" : 12
                    
                            })
       # When
        response = self.app.post('/accounts/login/krishna/loans', headers={"Content-Type": "application/json"}, data=payload2)

        # Then
        self.assertEqual(200, response.status_code)