from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def RCB(request):
    return render(request,'RCB.html')