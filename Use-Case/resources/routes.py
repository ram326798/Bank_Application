<<<<<<< HEAD
from .accounts import SignupApi, LoginApi,LoanApi

def initialize_routes(api):
    # we declare routes for all pages
    api.add_resource(SignupApi, '/accounts/signup')
    api.add_resource(LoginApi, '/accounts/login','/accounts/login/<username>')
    api.add_resource(LoanApi, '/accounts/login/<username>/loans')    
=======
from .accounts import SignupApi, LoginApi,LoanApi

def initialize_routes(api):
    
    api.add_resource(SignupApi, '/accounts/signup')
    api.add_resource(LoginApi, '/accounts/login','/accounts/login/<username>')
    api.add_resource(LoanApi, '/accounts/login/<username>/loans')    
>>>>>>> 48340382ef8281ae3a621d3983a13a68de3dd902
