from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sahweg(request):
    return render(request,'sahweg.html')
