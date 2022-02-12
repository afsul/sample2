
from django.shortcuts import render
from . models import list2

# Create your views here.
def index(request):
    list = list2.objects.all()
    
    return render(request, 'index.html',{'ls':list})
