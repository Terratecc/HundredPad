from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.mail import send_mail
from django.conf import settings
from .forms import *

# Create your views here.

def homepage(request):
	context = {}
	template = loader.get_template('main/index.html')
	return HttpResponse(template.render(context, request))

def error404(request, slug):
	context = {}
	template = loader.get_template('main/error404.html')
	return HttpResponse(template.render(context, request))


