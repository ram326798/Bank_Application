class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class UserNameAlreadyExistsError(Exception):
    pass
class LoanTypeAlreadyExistsError(Exception):
    pass

class UnauthorizedError(Exception):
    pass
errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "UserNameAlreadyExistsError": {
         "message": "User with given username already exists",
         "status": 400
     },
     "LoanTypeAlreadyExistsError": {
         "message": "User with given Loan type already exists",
         "status": 400
     },
     "UnauthorizedError": {
         "message": "Invalid username or password",
         "status": 401
     }
}