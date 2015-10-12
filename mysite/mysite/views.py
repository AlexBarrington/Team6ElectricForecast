from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.template import RequestContext, loader
# from django.db.models import Entry


class HomeView(TemplateView):
    template_name = 'index.html'

def OpArea1View(TemplateView):
	template = loader.get_template('opArea1Index.html')
	return HttpResponse(template.render())
	# return HttpResponse("<!DOCTYPE html><html><body><h1>Op Area 1 </h1><p>yay</p></body></html>")