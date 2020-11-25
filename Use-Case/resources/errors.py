<<<<<<< HEAD
class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class UserNameAlreadyExistsError(Exception):
    pass
class LoanTypeAlreadyExistsError(Exception):
    pass
class UserDoesNotExist(Exception):
    pass

class UnauthorizedError(Exception):
    pass
errors = {
    "InternalServerError": {
        "message": "Something went wrong",        
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
     },
     "UserNameAlreadyExistsError": {
         "message": "User with given username already exists",
     },
     "LoanTypeAlreadyExistsError": {
         "message": "User with given Loan type already exists",
     },
     "UserDoesNotExist": {
         "message": "User Does not exist register to apply loan",
     },
     "UnauthorizedError": {
         "message": "Invalid username or password",
     }
=======
class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class UserNameAlreadyExistsError(Exception):
    pass
class LoanTypeAlreadyExistsError(Exception):
    pass
class UserDoesNotExist(Exception):
    pass

class UnauthorizedError(Exception):
    pass
errors = {
    "InternalServerError": {
        "message": "Something went wrong",        
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
     },
     "UserNameAlreadyExistsError": {
         "message": "User with given username already exists",
     },
     "LoanTypeAlreadyExistsError": {
         "message": "User with given Loan type already exists",
     },
     "UserDoesNotExist": {
         "message": "User Does not exist register to apply loan",
     },
     "UnauthorizedError": {
         "message": "Invalid username or password",
     }
>>>>>>> 48340382ef8281ae3a621d3983a13a68de3dd902
}