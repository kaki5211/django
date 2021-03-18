from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.aggregates import Count
from django.db.models.enums import Choices
from django.db.models.fields import SmallIntegerField, TimeField


# Create your models here.
class Manage(models.Model):
    youtube_video_id = models.CharField(max_length=10, null=True)
    youtube_video_title = models.CharField(max_length=100, null=True)
    youtube_video_day = models.DateTimeField(null=True)
    youtube_video_episode = models.SmallIntegerField(null=True)

    # info_category = Choices(Video_category.category)
    # info_parson = Choices(Parson.parson)

    manage_twitter_already = models.BooleanField(default=False)

    def __str__(self):
        return self.youtube_video_title
    

class Video_category():
    category = models.CharField()
    def __str__(self):
        return Count()

class Parson():
    parson = models.CharField()

# class Accounts_a(models.Model):
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
