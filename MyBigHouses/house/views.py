from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from utils.login import login_required


# Create your views here.
@login_required
def index(request):
    return JsonResponse({"code": 0 ,"msg": "hello index"})