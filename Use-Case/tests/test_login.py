<<<<<<< HEAD
import json

from tests.BaseCase import BaseCase

# test file to check whether user able to successfull login
class LoginTest(BaseCase):       
    def test_successful_login(self):
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
        payload = json.dumps({
            "username":"ramakrishna",
            "password":"ramakrishna"
        })
        response = self.app.post('/accounts/signup', headers={"Content-Type": "application/json"}, data=user)
        response = self.app.post('/accounts/login', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual(200, response.status_code)
    
    # Test case to check giving invalid username
    def test_login_with_invalid_username(self):
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
        payload = json.dumps({
            "username":"krishna",
            "password":"ramakrishna"
        })
        response = self.app.post('/accounts/signup', headers={"Content-Type": "application/json"}, data=user)
        response = self.app.post('/accounts/login', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual("Invalid username or password", response.json['message'])
        self.assertEqual(500, response.status_code)
 
#  Test case to check login with invalid password
    def test_login_with_invalid_password(self):
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
        payload = json.dumps({
            "username":"ramakrishna",
            "password":"krishna"
        })
        response = self.app.post('/accounts/signup', headers={"Content-Type": "application/json"}, data=user)
        response = self.app.post('/accounts/login', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual("Invalid username or password", response.json['message'])
        self.assertEqual(500, response.status_code)
=======
import json

from tests.BaseCase import BaseCase


class LoginTest(BaseCase):       
    def test_successful_login(self):
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
        payload = json.dumps({
            "username":"ramakrishna",
            "password":"ramakrishna"
        })
        response = self.app.post('/accounts/signup', headers={"Content-Type": "application/json"}, data=user)
        response = self.app.post('/accounts/login', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual(200, response.status_code)
    
    def test_login_with_invalid_username(self):
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
        payload = json.dumps({
            "username":"krishna",
            "password":"ramakrishna"
        })
        response = self.app.post('/accounts/signup', headers={"Content-Type": "application/json"}, data=user)
        response = self.app.post('/accounts/login', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual("Invalid username or password", response.json['message'])
        self.assertEqual(500, response.status_code)
 
    # def test_login_with_invalid_password(self):
    def test_login_with_invalid_password(self):
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
        payload = json.dumps({
            "username":"ramakrishna",
            "password":"krishna"
        })
        response = self.app.post('/accounts/signup', headers={"Content-Type": "application/json"}, data=user)
        response = self.app.post('/accounts/login', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual("Invalid username or password", response.json['message'])
        self.assertEqual(500, response.status_code)
>>>>>>> 48340382ef8281ae3a621d3983a13a68de3dd902
