from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def index(request):
    
    return render (request,"index.html")

def wall(request):
    images = Image.objects.all()
    location = Location.objects.all()
    return render(request, 'wall.html',{"images":images, "location":location})    


