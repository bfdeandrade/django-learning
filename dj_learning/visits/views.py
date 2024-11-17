from random import randint
from django.shortcuts import render
from django.http import HttpResponse
from .models import Visits as V

# Create your views here.
def index(request):
    v = V.objects.first()
    v.count += 1
    v.save()
    
    context = {
        'num_visits': v.count, 
    }
    return render(request, 'index.html', context=context)