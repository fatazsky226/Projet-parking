#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('members.html')
  return HttpResponse(template.render())

def inscription(request):
  template = loader.get_template('inscription.html')
  return HttpResponse(template.render())

