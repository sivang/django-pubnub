from server.currentaccount.models import CurrentAccount

from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource, Resource, Bundle
from tastypie.validation import FormValidation, Validation
from tastypie import fields

from django.contrib.auth import authenticate, login, logout

def django_login(u, p , req):
    user = authenticate(u, p)
    if user and user.is_active:
        login(req, user)
        return True
    else:
        return False
       

class LoginResponse():
    username = 'username'
    password = 'password'
    success = 'false'
    def __init__(self, pk):
        self.username = pk


class LoginValidation(Validation):
    def is_valid(self, bundle, request=None):
        valid = bundle.data and 'username' in bundle.data and 'password' in bundle.data \
                and django_login(bundle.data['username'], bundle.data['password'], request)
        if DEBUG: print valid
        if valid: 
            bundle.data['success'] = True
            return {}
        else:
            bundle.data['success'] = False
            return {"authentication error" : "Bad login."}
        

class LoginResource(Resource):
    username = fields.CharField(attribute='username')
    password = fields.CharField(attribute='password')
    class Meta:
        fields = ['success', 'username', ]
        always_return_data = True
        resource_name = 'login'
        authentication = Authentication() # anybody can try login
        authorization = Authorization() # anybody can try login
        validation = LoginValidation()
    def get_resource_uri(self, bundle_or_obj):
        kwargs = {'resource_name': self._meta.resource_name,}
        if self._meta.api_name is not None:
            kwargs['api_name'] = self._meta.api_name
        return self._build_reverse_url("api_dispatch_detail", kwargs=kwargs)
    def obj_get(self, request, pk):
        return LoginResponse(pk)
    def get_object_list(self, request):
        results = [LoginResponse('username')]
        return results
    def obj_get_list(self, request=None, **kwargs):
        return self.get_object_list(request)
    def obj_create(self, bundle, request=None, **kwargs):
        return bundle
    def obj_update(self, bundle, request=None, **kwargs):
        return self.obj_create(bundle, request, **kwargs)
