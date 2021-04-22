#django.forms.ModelFormを継承する場合
from .models import Manage, Category, Member
from django import forms

class VideosearchFrom(forms.ModelForm):

    def __init__(self, *args, **kwd):
        super(VideosearchFrom, self).__init__(*args, **kwd)
        self.fields["youtube_video_title"].required = False
        self.fields["category_id"].required = False
        self.fields["youtube_video_episode"].required = False
        self.fields["youtube_video_day"].required = False
        self.fields["members"].required = False
        self.fields['category_id'].empty_label = '未選択'
        self.fields['members'].widget = forms.CheckboxSelectMultiple()  # 引数にattrs={'class': 'form-control'}も勿論できる。
        self.fields['members'].queryset = Member.objects
        # self.fields['members'].widget.attrs["class"] = "checkbox-inline radio-inline w-100"

    class Meta:
        model = Manage
        fields = ('youtube_video_title','category_id','youtube_video_episode','youtube_video_day','members') 

class CategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwd):
        super(CategoryForm, self).__init__(*args, **kwd)
        self.fields["contents"].required = False

    class Meta:
        model = Category
        fields = ("contents",)
        widgets = {
            'contents': forms.Textarea(attrs={'rows':15, 'cols':60}),
        }




