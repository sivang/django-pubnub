from django.http import HttpResponse
from django.contrib.auth.models import User
from currentaccount.models import CurrentAccount
from django.contrib.auth.decorators import login_required

def index(request):
    return HttpResponse("Welcome to Bank Current Account simulation for PubNub AES encrypted real time notifications.")

@login_required
def detail(request):
    cuaccount_id = CurrentAccount.objects.get(owner=request.user)
    return HttpResponse("Balance for current account %s:", curaccount_id, "is: ", CurrentAccount.objects.get(curaccount_id).balance)
