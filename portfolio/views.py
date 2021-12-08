from django import template
from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import Skills




# Create your views here.

def index(request):
    all_skills = Skills.objects.all()
    
    context = {
    'Skills':all_skills
    }
    return render(request, 'index.html', context)

# def new(request):
#     new = request.POST['email']
#     return render(request,'new.html', {'email': new})