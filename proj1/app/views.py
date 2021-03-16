from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Manage

# Create your views here.

class ManageView(ListView):
    model = Manage
    paginate_by=10
    template_name = 'app/base.html'
    