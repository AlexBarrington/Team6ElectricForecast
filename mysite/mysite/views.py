from django.shortcuts import render
# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.template import RequestContext, loader
from django.conf import settings
from django.shortcuts import redirect
from os import listdir
from os.path import isfile, join

# from django.db.models import Entry

myPath = "C:\\Users\\britt.ahlgrim\\Desktop\\Junior\\Semester 1\\software methodologies\\Project\\data"
opAreaFiles = [f for f in listdir(myPath) if isfile(join(myPath, f))]
opAreaNames = [f.replace('.csv', '') for f in opAreaFiles]

def Login(TemplateView):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())


def HomeView(TemplateView):
    if not TemplateView.user.is_authenticated():
        return redirect('http://127.0.0.1:8000/admin/logout')
    else:
        c = {'opAreas':opAreaNames}
        return render(TemplateView, 'index.html', c)


def OpAreaView(TemplateView):
    if not TemplateView.user.is_authenticated():
        return redirect('http://127.0.0.1:8000/admin/logout')
    else:
        c = {'pageTitle': 'OP AREA NAME', 'opAreas': opAreaNames}
        return render(TemplateView, 'opAreaIndex.html', c)
