from django.shortcuts import render
import datetime as dt

# Create your views here.
def home_page(request):
    return render ("index.html")

