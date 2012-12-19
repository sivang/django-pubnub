from django.http import HttpResponse
from django.contrib.auth.models import User
from currentaccount.models import CurrentAccount
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from hashlib import sha512

def index(request):
    return HttpResponse("Welcome to Bank Current Account simulation for PubNub AES encrypted real time notifications.")

@login_required
def detail(request):
    curaccount = CurrentAccount.objects.get(owner=request.user) # assuming one account per user
    context = {'username' : request.user.username, 
                'balance' : unicode(curaccount.balance),
                'notification_channel' : , curaccount.get_notif_channel(),
                'subkey' : 'sub-31c9765c-c453-11e1-b76c-1b01c696dab3',
                'ckey' : curaccount.get_ckey(),
                }
    return render(request, 'currentaccount/detail.html', context)
