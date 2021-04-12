#django.forms.ModelFormを継承する場合
from .models import Manage
from django import forms

class VideosearchFrom(forms.ModelForm):

    class Meta:
        model = Manage
        fields = ('youtube_video_title','category_id','youtube_video_episode','youtube_video_day',) 