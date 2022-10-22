from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def firstView(request):
    return render(request, "subApp/index.html")

def welcome(request,name):
    return render(request,"subApp/greet.html",{"name":name})
    # return render(request,"subApp/greet.html")