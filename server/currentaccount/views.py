from django.http import HttpResponse
from django.contrib.auth.models import User
from currentaccount.models import CurrentAccount
from django.contrib.auth.decorators import login_required
from django.shortcut import render

def index(request):
    return HttpResponse("Welcome to Bank Current Account simulation for PubNub AES encrypted real time notifications.")

@login_required
def detail(request):
    curaccount = CurrentAccount.objects.get(owner=request.user)
    context = {'username' : request.user.username, 'balance' : unicode(curaccount.balance)}
    return render(request, 'currentaccount/detail.html')
