from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Category

def index(request):
    categories = Category.objects.all()
    beauty_form = [cat.name + ", " for cat in categories]
    return HttpResponse(beauty_form)