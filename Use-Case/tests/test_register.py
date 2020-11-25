import json

from tests.BaseCase import BaseCase


class SignupTest(BaseCase):  
    #  Testcase Registering with proper schema
    def test_successful_signup(self):
        user = json.dumps({
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
        
        response = self.app.post('/accounts/signup', headers={"Content-Type": "application/json"}, data=user)
        self.assertEqual(200, response.status_code)
    # Test Case registering with non existing fields
    def test_signup_with_non_existing_field(self):
        #Given
        payload = json.dumps({
            "user":"ramakrishna",
            "password":"ramakrishna",
            "address":"8/121,p.k. ramaya street,jammalamadugu",
            "state":"andhrapradesh",
            "country":"India",
            "emailAddress":"chimmaniramakrishna25@gmail.com",
            "pan":"CWEPR7923F",
            "contactNo":9440921058,
            "DOB":"17/12/1995",
            "accountType":"savings",
 
        })

        #When
        response = self.app.post('/accounts/signup', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual('Request is missing required fields', response.json['message'])
        self.assertEqual(500, response.status_code)
# Testcase Registering without username
    def test_signup_without_username(self):
        #Given
        payload = json.dumps({
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
        response = self.app.post('/accounts/signup', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual('Request is missing required fields', response.json['message'])
        self.assertEqual(500, response.status_code)

# Test case registering without giving passworrd
    def test_signup_without_password(self):
        #Given
        payload = json.dumps({
            "username":"ramakrishna",
            "address":"8/121,p.k. ramaya street,jammalamadugu",
            "state":"andhrapradesh",
            "country":"India",
            "emailAddress":"chimmaniramakrishna25@gmail.com",
            "pan":"CWEPR7923F",
            "contactNo":9440921058,
            "DOB":"17/12/1995",
            "accountType":"savings"
        })
        response = self.app.post('/accounts/signup', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual('Request is missing required fields', response.json['message'])
        self.assertEqual(500, response.status_code)

# Test case registering with existing username
    def test_creating_already_existing_user(self):
        #Given
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
        response = self.app.post('/accounts/signup', headers={"Content-Type": "application/json"}, data=payload)
        response = self.app.post('/accounts/signup', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual('User with given username already exists', response.json['message'])
        self.assertEqual(500, response.status_code)
        