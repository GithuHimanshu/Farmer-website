from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def farmerlogin(request):
  return render(request,"farmer/farmerlogin.html",{})

def scholarlogin(request):
  return render(request,"scholar/scholarlogin.html",{})