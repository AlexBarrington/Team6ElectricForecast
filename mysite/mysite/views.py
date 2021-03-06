# Create your views here.
from django.views.generic.base import TemplateView
from django.http import *
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext, loader
from electricForcastApp.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from os import listdir
from os.path import isfile, join, abspath
import os
from . import forms

# from django.db.models import Entry

dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\data\\'
opAreaFiles = [f for f in listdir(dir) if isfile(join(dir, f))]
opAreaNames = [f.replace('.csv', '') for f in opAreaFiles]


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/Dashboard/')
    return render_to_response('login.html', context_instance=RequestContext(request))


@login_required
def HomeView(request):
    if not request.user.is_authenticated():
        return redirect('http://127.0.0.1:8000/logout')
    else:
        data_folder = MyUser.objects.get(data_folder=request.user.data_folder)
        dataFolder = str(data_folder)
        dataFolder = dir + dataFolder
        opAreaFiles = [f for f in listdir(dataFolder) if isfile(join(dataFolder, f))]
        opAreaNames = [f.replace('.csv', '') for f in opAreaFiles]
        c = {'opAreas': opAreaNames}
        return render_to_response('index.html', c)


@login_required
def OpAreaView(request, op_area_name=None):
    if not request.user.is_authenticated():
        return redirect('http://127.0.0.1:8000/admin/logout')
    else:
        data_folder = MyUser.objects.get(data_folder=request.user.data_folder)
        dataFolder = str(data_folder)
        dataFolder = dir + dataFolder
        opAreaFiles = [f for f in listdir(dataFolder) if isfile(join(dataFolder, f))]
        opAreaNames = [f.replace('.csv', '') for f in opAreaFiles]
        c = {'pageTitle': "OPAREA NAME", 'opAreas': opAreaNames}
        # c.update(csrf(request))
        return render_to_response('opAreaIndex.html', c)


def opArea(request, op_area_name=None):
    if not request.user.is_authenticated():
        return redirect('http://127.0.0.1:8000/admin/logout')
    else:
        data_folder = MyUser.objects.get(data_folder=request.user.data_folder)
        dataFolder = str(data_folder)
        dataFolder = dir + dataFolder
        opAreaFiles = [f for f in listdir(dataFolder) if isfile(join(dataFolder, f))]
        opAreaNames = [f.replace('.csv', '') for f in opAreaFiles]
    return render_to_response('opAreaIndex.html',
                              {'opArea': op_area_name,
                               'opAreas': opAreaNames},
                              context_instance=RequestContext(request))


def dataView(request, op_area_name=None):
    if not request.user.is_authenticated():
        return redirect('http://127.0.0.1:8000/admin/logout')
    else:
        data_folder = MyUser.objects.get(data_folder=request.user.data_folder)
        dataFolder = str(data_folder)
        dataFolder = dir + dataFolder
        opAreaFiles = [f for f in listdir(dataFolder) if isfile(join(dataFolder, f))]
        opAreaNames = [f.replace('.csv', '') for f in opAreaFiles]
        opAreaName = [n for n in opAreaNames if n == op_area_name]
        opAreaDataPath = dataFolder + '\\' + op_area_name + '.csv'
        file = open(opAreaDataPath, 'r')
        contents = file.read()
        return render_to_response('data.html', {'data': contents})


def register_user(request):
    args = {}
    args.update(csrf(request))

    if request.method == 'POST':
        form = forms.MyRegistrationForm(request.POST)
        if form.is_valid():
            print("Is valid")
            user = form.save()
            return HttpResponseRedirect('/register_success/' + user.data_folder + '/')
        else:
            print("Is invalid")
            print(form.data)
            args = {}
            args.update(csrf(request))
            args['form'] = form
    else:
        args = {}
        args.update(csrf(request))
        args['form'] = forms.MyRegistrationForm()

    return render_to_response('register.html', args, context_instance=RequestContext(request))


def register_success(request, data_folder=None):
    split = [data_folder[0]] + ['/'+l for l in data_folder[1:]]
    data_folder = split[0]
    data_folder = dir + data_folder
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
    return render_to_response('register_success.html')
