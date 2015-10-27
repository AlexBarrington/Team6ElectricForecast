from django.shortcuts import render, render_to_response
# Create your views here.
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext, loader
from django.shortcuts import redirect
from os import listdir
from os.path import isfile, join

# from django.db.models import Entry

myPath = "C:\\Users\\britt.ahlgrim\\Desktop\\Junior\\Semester 1\\software methodologies\\Project\\data"
opAreaFiles = [f for f in listdir(myPath) if isfile(join(myPath, f))]
opAreaNames = [f.replace('.csv', '') for f in opAreaFiles]

def Login(TemplateView):
    c = {}
    c.update(TemplateView)
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

@csrf_exempt
def HomeView(request):
    if not request.user.is_authenticated():
        return redirect('http://127.0.0.1:8000/admin/logout')
    else:
       c = {'opAreas':opAreaNames}
       #c.update(csrf(request))
       return render_to_response('index.html', c)

@csrf_exempt
def OpAreaView(request):
    if not request.user.is_authenticated():
        return redirect('http://127.0.0.1:8000/admin/logout')
    else:
        c = {'pageTitle': 'OP AREA NAME', 'opAreas': opAreaNames}
        #c.update(csrf(request))
        return render_to_response('opAreaIndex.html', c)
