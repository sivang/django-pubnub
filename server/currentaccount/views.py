from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the Current Account landing page.")

def detail(request, curaccount_id):
    return HttpResponse("Balance for current account %s:", curaccount_id)
