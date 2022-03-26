from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def my_Photo(request):
    return HttpResponse("welcome to your gallery")