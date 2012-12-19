from server.currentaccount.models import CurrentAccount
from django.contrib.auth.models import User

from tastypie.authentication import Authentication, BasicAuthentication
from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie.resources import ModelResource
from tastypie import fields

from django.contrib.auth import authenticate, login, logout


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        allowed_methods = ['get', ]
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()

class CurrentAccountResource(ModelResource):
    owner = fields.ForeignKey(UserResource, 'owner')
    class Meta:
        queryset = CurrentAccount.objects.all()
        resource_name = 'account'
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()
