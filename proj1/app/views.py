from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Manage

# Create your views here.

class ManageView(ListView):
    model = Manage
    paginate_by=3
    template_name = 'app/top.html'

class VideolistView(ListView):
    model = Manage
    template_name = 'app/video_list.html'

class DetailView(DetailView):
    model = Manage
    template_name = 'app/detail.html'

    # def get_queryset(self):
    #     return super().get_queryset()
    
    