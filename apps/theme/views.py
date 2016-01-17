from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

def home(request, template_name='home.html'):
    return render(request, template_name)
