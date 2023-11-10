from django.shortcuts import render
from django.http import HttpResponse 

def calculate():
    x = 1
    y = 2
    return x

# Create your views here.
def say_hello(request): 
    x = calculate()
    return render(request,'hello.html',{'name':'mosh'})
    # in this function we do a lot of things like pull data from a db, transform, send email etc 
      