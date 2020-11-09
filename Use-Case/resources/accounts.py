from flask import Response, request,jsonify
from database.models import User,Loan
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist,ValidationError,NotRegistered
from resources.errors import SchemaValidationError,LoanTypeAlreadyExistsError,UserNameAlreadyExistsError, UnauthorizedError,InternalServerError,UserDoesNotExist



class SignupApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user =  User(**body)
            user.save()
            # id = user.id
            return 'User Registered sucessfully', 200         
        except FieldDoesNotExist:
            raise SchemaValidationError
        except ValidationError:
            raise SchemaValidationError        
        except NotUniqueError:
            raise UserNameAlreadyExistsError
        except Exception as e:
            raise InternalServerError

class LoginApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user = User.objects.get(username=body.get('username'))
            authorized = User.objects.get(password=body.get('password'))
            return 'User Login Sucessfully', 200
            if not authorized:
                raise UnauthorizedError
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception as e:
            raise InternalServerError
        
    def put(self,id):
        body = request.get_json()
        # user = User(**body)
        User.objects.get(id=id).update(**body)
        return "User Updated successfully", 201
    
    def get(self,id):
        user=User.objects.get(id=id).to_json()
        return Response(user, mimetype="application/json", status=200)
    
class LoanApi(Resource):
    def post(self,username):
        try:
            body = request.get_json()
            user = User.objects.get(username=body.get('username'))
            loan =  Loan(**body)
            loan.save()
            return 'loan updated sucessfully', 200
            if not user:
                raise UserDoesNotExist
        except (NotRegistered):
            raise UserDoesNotExist
        except NotUniqueError:
            raise LoanTypeAlreadyExistsError
        except Exception as e:
            raise InternalServerError
    def put(self,username):
        body = request.get_json()
        # user = User(**body)
        Loan.objects.get(username=username).update(**body)
        return "User Updated successfully", 201
    
    def get(self,username): 
            loan=Loan.objects.get(username=username).to_json()       
            # loan=Loan.objects().to_json()
            return Response(loan, mimetype="application/json", status=200)