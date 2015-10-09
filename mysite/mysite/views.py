from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
# from django.db.models import Entry


class HomeView(TemplateView):
    template_name = 'index.html'
    # queryset = Entry.objects.order_by('-created_at')
