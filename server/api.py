from server.currentaccount.models import CurrentAccount

from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource, Resource, Bundle
from tastypie.validation import FormValidation, Validation
from tastypie import fields

from django.contrib.auth import authenticate, login, logout

class LoginResponse:
    success = False
    username = 'none'
    password = 'none'
    pk = 'something'
    def __init__(self, username='none', password='none', pk='none'):
        self.username = username
        self.password = password
        self.pk = pk
        self.success = False

def tlogin(username, password, request):
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return True

class LoginValidation(Validation):
    def is_valid(self, bundle, request=None):
        if not bundle.data:
            return {'__all__' : 'Bad request'}


        if 'username' in bundle.data and 'password' in bundle.data and tlogin(bundle.data['username'], bundle.data['password'], request):
            bundle.data['success'] = True
            return {}
        else:
            bundle.data['success'] = False
            return {'__all__' : 'Bad login.'}

class LoginResource(Resource):
    username = fields.CharField(attribute='username')
    password = fields.CharField(attribute='password')
    class Meta:
        fields = ['success', 'username', ]
        always_return_data = True
        resource_name = 'login'
        authentication = Authentication()
        authorization = Authorization()
        object_class = LoginResponse
        validation = LoginValidation()
    def get_resource_uri(self, bundle_or_obj):
        kwargs = {'resource_name': self._meta.resource_name,}
        if isinstance(bundle_or_obj, Bundle):
            kwargs['pk'] = bundle_or_obj.obj.username
        else:
            kwargs['pk'] = bundle_or_obj.username
        if self._meta.api_name is not None:
            kwargs['api_name'] = self._meta.api_name
        return self._build_reverse_url("api_dispatch_detail", kwargs=kwargs)
    def obj_get(self, request, pk):
        return LoginResponse(username=pk)
    def get_object_list(self, request):
        results = [LoginResponse()]
        return results
    def obj_get_list(self, request=None, **kwargs):
        return self.get_object_list(request)
    def obj_create(self, bundle, request=None, **kwargs):
        return bundle
    def obj_update(self, bundle, request=None, **kwargs):
        return self.obj_create(bundle, request, **kwargs)