from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.aggregates import Count
from django.db.models.enums import Choices
from django.db.models.fields import SmallIntegerField, TimeField
from django.db.models.fields.reverse_related import ManyToOneRel

# いらないｰｰｰｰｰｰｰｰ
# sex_ = (
#     ("man", '男性'),
#     ("woman", '女性')
# )
# ｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰｰ

# Create your models here.

class Book(models.Model):
    title = models.CharField('タイトル', max_length=100, null=True, blank=True)
    pages = models.SmallIntegerField('ページ数', null=True, blank=True)
    issue = models.DateField('発行日', null=True, blank=True) # [発行日, y m d]

    post_day = models.DateField('投稿日', null=True, blank=True) # [発行日, y m d]

    YOUTH_CHOICES = (('Y', 'Youth'),('O', 'Old'))
    youth_choices = models.CharField('青春/白秋', choices=YOUTH_CHOICES, max_length=10)

    series_info = models.ForeignKey("Series", verbose_name=("シリーズ情報"), on_delete=models.CASCADE, null=True, blank=True)
    Author_info = models.ForeignKey("Author", verbose_name=("著者情報"), on_delete=models.CASCADE, null=True, blank=True)
    category_info = models.ManyToManyField("Category", verbose_name=("カテゴリー情報"), blank=True, related_name="category_info")
    publisher_info = models.ForeignKey("Publisher", verbose_name=("出版社情報"), on_delete=models.CASCADE, null=True, blank=True)

    contents = models.TextField("コンテンツ", null=True, blank=True)

    fin = models.SmallIntegerField('完読', null=True, blank=True)

    amazon_url = models.CharField('アマゾンURL', max_length=1000, null=True, blank=True)
    def __str__(self):
        return self.title



class Author(models.Model):
    GENDER_CHOICES = (('Mon', '男性'),('Womon', '女性'))
    WORD_CHOICES = (('Aa', 'あ行'),('Ka', 'か行'),('Sa', 'さ行'),('Ta', 'た行'),('Na', 'な行'),('Ha', 'は行'),('Ma', 'ま行'),('Ya', 'や行'),('Ra', 'ら行'),('Wa', 'わ行'))

    author = models.CharField('著者', max_length=100, default=None) # 追加していく-----------
    author_eng = models.CharField('著者eng', max_length=100) # 追加していく-----------
    word_oder = models.CharField('五十音', choices=WORD_CHOICES, max_length=10)
    age = models.DateField('生年月日')
    sex = models.CharField('性別', choices=(('', '未選択'),)+GENDER_CHOICES, max_length=10, blank=True)
    contents = models.TextField("コンテンツ")
    contents_lite = models.TextField("コンテンツ", blank=True, null=True)

    post_day = models.DateField('投稿日', null=True) # [発行日, y m d]
    def __str__(self):
        return self.author
    
class Category(models.Model):
    CATEGORY_CHOICES = (('action', 'アクション'),('adventure', 'アドベンチャー'),('youth', '青春'),('love', '恋愛'),('sf', 'SF'),('history', '時代'),('mystery', 'ミステリー'),('comedy', 'コメディー'), ('horror', 'ホラー'))
    # CATEGORYENG_CHOICES = (('Action_eng', 'Action'), ('Youth_eng', 'Youth'), ('Love_eng', 'Love'), ('History_eng', 'History'), ('Mystery_eng', 'Mystery'), ('Horror_eng', 'Horror'))
    CATEGORYENG_CHOICES = (('action', 'アクション'),('adventure', 'アドベンチャー'),('youth', '青春'),('love', '恋愛'),('sf', 'SF'),('history', '時代'),('mystery', 'ミステリー'),('comedy', 'コメディー'), ('horror', 'ホラー'))
    COLOR_CHOICES = (('red', 'red'), ('orange','orange'),('blue', 'blue'), ('pink', 'pink'),('info','info'), ('green', 'green'), ('purple', 'purple'), ('warning','warning'),('dark', 'dark'))

    category = models.CharField("カテゴリー", choices=CATEGORY_CHOICES, max_length=20, default=None) # 追加していく-----------
    category_eng = models.CharField("カテゴリーeng", choices=CATEGORYENG_CHOICES ,max_length=20, null=True, blank=True) # 追加していく-----------
    color = models.CharField("色", choices=COLOR_CHOICES, max_length=20)

    contents = models.TextField("コンテンツ", blank=True)
    contents_keyword = models.TextField("キーワード", blank=True)

    post_day = models.DateField('投稿日', null=True) # [発行日, y m d]
    def __str__(self):
        return self.category

class Publisher(models.Model):
    publisher = models.CharField('出版社', max_length=50)
    publisher_eng = models.CharField('出版社_eng', max_length=50, blank=True, null=True)
    contents = models.TextField("コンテンツ")
    incorporated = models.DateField('設立日')

    post_day = models.DateField('投稿日', null=True) # [発行日, y m d]
    def __str__(self):
        return self.publisher

class Series(models.Model):
    series = models.CharField("シリーズ", max_length=100)
    contents = models.TextField("コンテンツ")

    author = models.ForeignKey("Author", verbose_name=("著者"), on_delete=models.CASCADE)

    post_day = models.DateField('投稿日', null=True) # [発行日, y m d]
    def __str__(self):
        return self.series

class Templates(models.Model):
    breadcrumb = models.TextField("目次")
    





""" 予定 ----------------------------
作品タイトル
出版日
・y
・m
・d
ページ数
画像
感想（コンテンツ）


アマゾンリンク

■集英社
■カテゴリー
　※複数あり
■著者
・男/女
・生まれ年
・
----------------------------"""