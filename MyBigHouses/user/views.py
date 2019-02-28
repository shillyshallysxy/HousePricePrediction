from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

# Create your views here.


def user(request):
    return HttpResponse("page of user info!")


def register(request):
    pass


def f2():
    pass


def login(request):
    if request.method == 'POST':
        username = request.POST.get('')
    return render(request, 'login.html')