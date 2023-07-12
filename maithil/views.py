from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
	return render(request,"home.html")

def signup(request):
	return render(request,"signup.html")
