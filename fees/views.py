from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
def fees_django(request):
    return HttpResponse("<h1>500</h1>")
def fees_python(request):
    return HttpResponse("<h1>200</h1>")