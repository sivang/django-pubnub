from server.models import CurrentAccount
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource, Resource, Bundle
from tastypie.validation import FormValidation, Validation


def django_login(u, p , req):
    user = authenticate(u, p)
    if user and user.is_active:
        login(req, user)
        return True
    else:
        return False
        

class LoginValidation(Validation):
    def is_valid(self, bundle, request=None):
        valid = bundle.data and 
            'username' in bundle.data and 'password' in bundle.data and
            django_login(bundle.data['username'], bundle.data['password'], request)
        if valid: 
            bundle.data['success'] = True
            return {}
        else:
            bundle.data['success'] = False
            return {"authentication error" : "Bad login."}
        

