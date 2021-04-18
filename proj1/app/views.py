from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import ModelFormMixin
from .models import Manage, Category, Member
from django.http import Http404
from django.db.models import Prefetch
from . import forms
from django.db.models import Q

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
    success_url = '/videoserch/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['category'] = Category.objects.all()
        context['member'] = Member.objects.all()
        return context
    
    def get_queryset(self):
            # sessionに値がある場合、その値でクエリ発行する。
            if 'form_value' in self.request.session and self.request.session['form_value'] != None:
                form_value = self.request.session['form_value']
                youtube_video_title = form_value['youtube_video_title']
                youtube_video_day = form_value['youtube_video_day']
                youtube_video_episode = form_value['youtube_video_episode']
                category_id = form_value['category_id']
                members = form_value['members']

                # 検索条件
                condition_youtube_video_title = Q()
                condition_youtube_video_day = Q()
                condition_youtube_video_episode = Q()
                condition_category_id = Q()
                condition_members = Q()
                if len(youtube_video_title) != 0 and youtube_video_title[0]:
                    condition_youtube_video_title = Q(youtube_video_title__icontains=youtube_video_title)
                if len(youtube_video_day) != 0 and youtube_video_day[0]:
                    condition_youtube_video_day = Q(youtube_video_day__contains=youtube_video_day)
                if len(youtube_video_episode) != 0 and youtube_video_episode[0]:
                    condition_youtube_video_episode = Q(youtube_video_episode=youtube_video_episode)
                if category_id != None:
                    if len(category_id) != 0 and category_id[0]:
                        condition_category_id = Q(category_id=category_id)
                if members != None:
                    if len(members) != 0 and members[0]:
                        condition_members = Q(members=members)
                return Manage.objects.select_related().filter(condition_youtube_video_title & condition_youtube_video_day & condition_youtube_video_episode & condition_category_id & condition_members)

            else:
                return Manage.objects.all()        
        

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)        

    def post(self, request, *args, **kwargs):
        self.object = Manage
        form_value = {
            'youtube_video_title':self.request.POST.get('youtube_video_title', None),
            'youtube_video_day':self.request.POST.get('youtube_video_day', None),
            'youtube_video_episode':self.request.POST.get('youtube_video_episode', None),
            'category_id':self.request.POST.get('category_id', None),
            'members':self.request.POST.get('members', None),
        }
        request.session['form_value'] = form_value
        # 検索時にページネーションに関連したエラーを防ぐ
        self.request.POST = self.request.POST.copy()
        self.request.POST.clear()
        return self.get(request, *args, **kwargs)        # youtube_video_title = None
        

    # def get_form(self, form_class=None):
    #     # user_data_input.hmltで、データを送信した場合はここ
    #     if 'youtube_video_title' in self.request.POST:
    #         form_data = self.request.POST

    #     # 確認画面(user_data_confirm.html)から戻るリンクを押した場合や
    #     # 初回の入力欄表示はここ。セッションにユーザーデータがあれば、それをフォームに束縛させる
    #     else:
    #         form_data = self.request.session.get('youtube_video_title', None)

    #     return self.form_class(form_data)
        

class VideosView(ListView):
    model = Manage
    template_name = 'app/videos.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['category'] = Category.objects.all()
        context['member'] = Member.objects.all()
        return context


