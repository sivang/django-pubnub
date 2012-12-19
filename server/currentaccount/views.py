from django.http import HttpResponse
from django.contrib.auth.models import User
from currentaccount.models import CurrentAccount
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def index(request):
    return HttpResponse("Welcome to Bank Current Account simulation for PubNub AES encrypted real time notifications.")

@login_required
def detail(request):
    curaccount = CurrentAccount.objects.get(owner=request.user) # assuming one account per user
    context = {'username' : request.user.username, 
                'balance' : unicode(curaccount.balance),
                'notification_channel' : curaccount.get_notif_channel(),
                'subkey' : 'sub-31c9765c-c453-11e1-b76c-1b01c696dab3',
                'ckey' : curaccount.get_ckey(),
                }
    # render before hooking up signal
    resp = render(request, 'currentaccount/detail.html', context)
    # connect signal for account update push notif
    from django.db.models.signals import post_save
    # using a dispatch_uid to make sure signals are not duplicated
    # in subsequents imports / view calls.
    post_save.connect(curaccount.push_cbk, CurrentAccount, dispatch_uid='current_account_post_save')
    return resp
