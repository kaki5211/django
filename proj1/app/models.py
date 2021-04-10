from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.aggregates import Count
from django.db.models.enums import Choices
from django.db.models.fields import SmallIntegerField, TimeField
from django.db.models.fields.reverse_related import ManyToOneRel


# Create your models here.
class Manage(models.Model):
    youtube_video_id = models.CharField(max_length=12, null=True)
    youtube_video_title = models.CharField(max_length=100, null=True)
    youtube_video_day = models.DateTimeField(null=True)
    youtube_video_episode = models.SmallIntegerField(null=True)
    contents = models.CharField(max_length=1023, null=True)

    category_id = models.ForeignKey('Category', db_column='category_id', on_delete=models.CASCADE, default="1")

    members = models.ManyToManyField('Member', related_name="members")

    manage_twitter_already = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.youtube_video_title
    
class Category(models.Model):
    category_id = models.AutoField('category_id', primary_key=True)
    category_jp = models.CharField('カテゴリーjp', max_length=50, null=True)
    category_eng = models.CharField('カテゴリーeng', max_length=50, null=True)
    
    members = models.ManyToManyField('Member', related_name="members_ct")
    contents = models.CharField("コンテンツ", max_length=1024, null=True)
    def __str__(self):
        return self.category_jp


class Member(models.Model):
    member_id = models.AutoField('member_id', primary_key=True)
    member_jp = models.CharField('メンバーjp', max_length=20)
    member_eng = models.CharField('メンバーeng', max_length=20)
    def __str__(self):
        return self.member_jp

#     accounts_a = models.CharField("タイトル", max_length=100)


#     def __str__(self):
#         return self.accounts_a


# class Article(models.Model):
#     gender = ((1, '男'), (2, '女'))
#     name = models.OneToOneField(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     sex = models.IntegerField(null=True, choices=gender)
#     DOB_year = models.SmallIntegerField(null=True, validators=[MinValueValidator(1950),MaxValueValidator(2020)])
#     DOB_mon = models.SmallIntegerField(null=True, validators=[MinValueValidator(1),MaxValueValidator(12)])
#     DOB_day = models.SmallIntegerField(null=True, validators=[MinValueValidator(1),MaxValueValidator(31)])
#     text = models.TextField(null=True)
