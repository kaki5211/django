from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import ModelFormMixin
from .models import Manage, Category, Member
from django.http import Http404
from django.db.models import Prefetch
from . import forms

# Create your views here.


class ManageView(ListView):
    model = Manage
    paginate_by=7
    template_name = 'app/top.html'
    def get_queryset(self):
        return Manage.objects.all().order_by('-youtube_video_day')
    # quaryset = Manage.objects.order_by('-youtube_video_day')
    ordering = '-youtube_video_day' # order_by('-title')
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['category'] = Category.objects.all()
        context['member'] = Member.objects.all()
        context['new_flag'] = Manage.objects.order_by('-youtube_video_day').first().youtube_video_id
        return context


class VideolistView(ListView):
    model = Manage
    template_name = 'app/video_list.html'


class VideoView(DetailView):
    model = Manage
    template_name = 'app/video_info.html'
    def get_object(self, queryset=None):
        try:
            video_q = Manage.objects.filter(youtube_video_episode=self.kwargs['youtube_video_episode'], category_id__category_eng=self.kwargs['category_eng']).first()
        except:
            video_q = Manage.objects.filter(pk=self.kwargs['pk']).first()
        return video_q

    # def get_queryset(self):
    #     try:
    #         video_q = Manage.objects.filter(youtube_video_episode=self.kwargs['youtube_video_episode'], category_id__category_eng=self.kwargs['category_eng'])
    #     except:
    #         video_q = Manage.objects.filter(pk=self.kwargs['pk'])
    #     return video_q

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['category'] = Category.objects.all()
        context['member'] = Member.objects.all()
        return context

class CategorysView(ListView):
    model = Category
    template_name = 'app/categorys.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['category'] = Category.objects.all()
        context['member'] = Member.objects.all()
        return context
        
class CategoryinfoView(DetailView):
    model = Category
    template_name = 'app/category_info.html' 
    context_object_name = 'category_'
    def get_object(self, queryset=None):
        try:
            video_q = Category.objects.filter(category_eng=self.kwargs['category_eng']).first()
        except:
            video_q = Category.objects.filter(pk=self.kwargs['pk'])
        return video_q
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['category'] = Category.objects.all()
        context['member'] = Member.objects.all()
        context['episode_max'] = Manage.objects.filter(category_id__category_eng=self.kwargs['category_eng']).count()
        return context

class MembersView(ListView):
    model = Member
    template_name = 'app/members.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['category'] = Category.objects.all()
        context['member'] = Member.objects.all()
        return context

class MemberinfoView(DetailView):
    model = Member
    template_name = 'app/member_info.html'
    def get_object(self, queryset=None):
        try:
            video_q = Member.objects.filter(member_eng=self.kwargs['member_eng']).first()
        except:
            video_q = Member.objects.filter(pk=self.kwargs['pk'])
        return video_q
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['category'] = Category.objects.all()
        context['member'] = Member.objects.all()
        return context

class VideosearchView(ListView, ModelFormMixin):
    model = Manage
    template_name = 'app/video_search.html'
    form_class=forms.VideosearchFrom
    success_url = '/videoserch'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['category'] = Category.objects.all()
        context['member'] = Member.objects.all()
        return context
    
    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)        

    def post(self, request, *args, **kwargs):
        self.object = None
        self.object_list = self.get_queryset()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

        
class VideosView(ListView):
    model = Manage
    template_name = 'app/videos.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['category'] = Category.objects.all()
        context['member'] = Member.objects.all()
        return context
# class Video_info(DetailView):
    

# class Category_info(DetailView):




# def get_queryset(self):
#     return super().get_queryset()

