from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, TemplateView
from django.views.generic.edit import ModelFormMixin, UpdateView
from django.http import Http404
from django.db.models import Prefetch
from django.db.models import Q
# from . import forms


from .models import Book, Category, Author, Publisher, Series, Templates



def common(request):
    context = {}
    # context['primary'] = Category.objects.all().first()
    context['category'] = Category.objects.all().order_by('category')
    context['author_Aa'] = [Author.objects.filter(word_oder='Aa').order_by("author"),
                                Author.objects.filter(word_oder='Ka').order_by("author"),
                                Author.objects.filter(word_oder='Sa').order_by("author"),
                                Author.objects.filter(word_oder='Ta').order_by("author"),
                                Author.objects.filter(word_oder='Na').order_by("author"),
                                Author.objects.filter(word_oder='Ha').order_by("author"),
                                Author.objects.filter(word_oder='Ma').order_by("author"),
                                Author.objects.filter(word_oder='Ya').order_by("author"),
                                Author.objects.filter(word_oder='Ra').order_by("author"),
                                Author.objects.filter(word_oder='Wa').order_by("author")
                                ]
    context['author'] = Author.objects.all()
    context['publisher'] = Publisher.objects.all()
    context['templates'] = Templates.objects.all()

    #---  パンくずリスト作成　---
    url_path = request.path
    url_split = url_path.split('/')
    url_path = ""
    url_dict = {}
    flag = 0
    url_path = "{0}://{1}/".format(request.scheme, request.get_host())
    try:
        context["url_main"] = None
        for item in url_split[1:]:
            if item == "":
                continue
            url_path += item + "/"

            if flag != 0 :
                if flag == 1:
                    item = Book.objects.get(post_day=item).title
                if flag == 2:
                    item = Category.objects.get(category=item).get_category_display
                if flag == 3:
                    item = Author.objects.get(author_eng=item).author
                if flag == 4:
                    item = Publisher.objects.get(publisher_eng=item).publisher
                # context["url_main"] = item
                url_dict.update({item:url_path})
                context['breadcrumb'] = url_dict # パンくずリスト完成
                return context

            if item == "book":
                item = "HOME"
            if item == "books":
                item = '書籍一覧'
                flag = 1
                context['nav_active'] = flag
            if item == "categorys":
                item = "カテゴリー一覧"
                flag = 2
                context['nav_active'] = flag
            if item == "authors":
                item = "著者一覧"
                flag = 3
                context['nav_active'] = flag
            if item == "publishers":
                item = "出版社一覧"
                flag = 4
                context['nav_active'] = flag

            url_dict.update({item:url_path})
            context["url_sub"] = item

        context['breadcrumb'] = url_dict # パンくずリスト完成
    except:
        pass

    


    return context
