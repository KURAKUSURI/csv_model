from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def CSK(request):
    return render(request,'CSK.html')
