from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, FormView, TemplateView
from django.views.generic.edit import ModelFormMixin, UpdateView

from django.http import Http404
from django.db.models import Prefetch
from django.db.models import Q
import re, datetime
from django_middleware_global_request.middleware import get_request
# import django.django_middleware_global_request.middleware
# from django.
from .forms import BookForm, CategoryForm, AuthorForm
from . import forms
# from . import forms


from .models import Book, Category, Author, Publisher, Series

# Create your views here



class MyListView(ListView):
    template_list = ['authors', 'categorys', 'publishers', 'top', 'books']
    # request = get_request()
    def my_get_data(self, *args, **kwargs):
        # get_data = super().aet_data(self, request, *args, **kwargs)
        request = get_request()
        get_data = {}
        get_data['url_sub'] = None
        get_data['url_main'] = None
        
        url_path = request.path
        url_split = url_path.split('/')
        url_dict = {}
        flag = 0
        url_path = "{0}://{1}/".format(request.scheme, request.get_host())
        # try:
        get_data['contents'] = None
        get_data['book_info'] = None
        get_data['category_info'] = None
        get_data['author_info'] = None
        get_data['publisher_info'] = None
        for item in url_split[1:]:
            if item == "":
                continue

            if flag != 0 :
                if flag == 1:
                    q = Book.objects.get(post_day=item)
                    get_data['book_info'] = q.title
                    get_data['contents'] = q.contents
                if flag == 2:
                    q = Category.objects.get(category=item)
                    get_data['category_info'] = q.get_category_display
                    get_data['contents'] = q.contents
                if flag == 3:
                    q = Author.objects.get(author_eng=item)
                    get_data['author_info'] = q.author
                    get_data['contents'] = q.contents
                    get_data['author_info_q'] = Book.objects.filter(Author_info=q.id)
                if flag == 4:
                    q = Publisher.objects.get(publisher_eng=item)
                    get_data['publisher_info'] = q.publisher
                    get_data['contents'] = q.contents
                get_data["url_main"] = item
                return get_data

            if item == "books":
                flag = 1
            if item == "categorys":
                flag = 2
            if item == "authors":
                flag = 3
            if item == "publishers":
                flag = 4

            get_data["url_sub"] = item
        return get_data

    def my_get_context_data(self, *args, **kwargs):
        #---  テンプレートブロック選択---
        context = super().get_context_data()
        get_data = self.my_get_data(self, **kwargs)
        try:
            context['contents'] = get_data['contents']
            context['book_info'] = get_data['book_info']
            context['category_info'] = get_data['category_info']
            context['author_info'] = get_data['author_info']
            context['publisher_info'] = get_data['publisher_info']
        except:
            pass
        context['view'] = [1,1,1,1,1] # [ブログ紹介, メインコンテンツ+サイドバー, メインコンテンツのみ, トピックス] 
        # context['author'] = {}
        # context['author']['author_in_category'] = [Book.objects.filter(Author_info=a).count for a in Author.objects.all()]
        return context

    def my_get_template_names(self, *args, **kwargs):
        # ■■■ urlの文字列で、テンプレートの分岐 ■■■
        # get_rquest = super().get_request()
        get_data = self.my_get_data(self, **kwargs)
        url_sub = [s for s in self.template_list if get_data['url_sub'] in s][0]
        template_name = 'book/{}_err.html'.format(url_sub)
        judge = dict()
        url_main = get_data['url_main']

        # try:
        if get_data['url_main'] == None:
            template_name = 'book/{}.html'.format(url_sub)
        else:
            try:
                hensu = "{}.objects.get({}_eng='{}')".format(url_sub.capitalize()[:-1], url_sub[:-1], url_main)
                exec("aiueo = {}".format(hensu), globals(), judge)
                judge_info = judge["aiueo"]
                template_name = 'book/{}_info.html'.format(url_sub)
            except:
                pass
        return template_name




class TopView(MyListView): # TopView
    model = Book
    template_name = 'book/top.html'

    def get_context_data(self, *args, **kwargs):
        context = super().my_get_context_data(self, *args, **kwargs)
        return context

    def get_queryset(self):
        q = Book.objects.all().order_by("post_day")
        return q

        



class CategoryView(MyListView):
    model = Book
    template_name = 'book/categorys_info.html'
    def get_context_data(self, *args, **kwargs):
        context = super().my_get_context_data(self, *args, **kwargs)
        context['view'] = [0,1,0,1,0] # [ブログ紹介, メインコンテンツ+サイドバー, メインコンテンツのみ, トピックス]
        return context

    def get_template_names(self, *args, **kwargs):
        # ■■■ urlの文字列で、テンプレートの分岐 ■■■
        template_name = self.my_get_template_names(self, *args, **kwargs)
        return template_name

class AuthorView(MyListView):
    model = Book
    template_name = 'book/authors.html'
    def get_context_data(self, **kwargs):
        context = super().my_get_context_data(self, **kwargs)
        context['view'] = [0,1,0,1,0] # [ブログ紹介, メインコンテンツ+サイドバー, メインコンテンツのみ, トピックス]
        return context
    def get_template_names(self, *args, **kwargs):
        # ■■■ urlの文字列で、テンプレートの分岐 ■■■
        template_name = self.my_get_template_names(self, *args, **kwargs)
        return template_name

class PublisherView(MyListView):
    model = Publisher
    template_name = 'book/publishers.html'
    def get_context_data(self, **kwargs):
        context = super().my_get_context_data(self, **kwargs)
        context['view'] = [0,1,0,1,0] # [ブログ紹介, メインコンテンツ+サイドバー, メインコンテンツのみ, トピックス]
        return context
    def get_template_names(self, *args, **kwargs):
        # ■■■ urlの文字列で、テンプレートの分岐 ■■■
        template_name = self.my_get_template_names(self, *args, **kwargs)
        return template_name







class SeriesView(ListView):
    model = Series
    template_name = 'book/base.html'

class ArticlesView(MyListView):
    model = Book
    template_name = 'book/books.html'
    def get_context_data(self, **kwargs):
        context = super().my_get_context_data(self, **kwargs)
        context['view'] = [0,1,0,1,0] # [ブログ紹介, メインコンテンツ+サイドバー, メインコンテンツのみ, トピックス]
        return context
    def get_template_names(self, *args, **kwargs):
        # ■■■ urlの文字列で、テンプレートの分岐 ■■■
        template_name = self.my_get_template_names(self, *args, **kwargs)
        return template_name
    
class BookView(ListView):
    model = Book
    template_name = 'book/books.html'
    success_url = '/books/'    
    # form_class = BookForm
    object_list = Book
    def get_context_data(self, *args, **kwargs):
        # if self.request.method != "POST":
        #     context = super().get_context_data()
        # else:
        #     context = self.context
        #     return context
        context = super().get_context_data()
        data_info = self.get_date()
        context['view'] = [0,1,0,0,1] # [ブログ紹介, メインコンテンツ+サイドバー, メインコンテンツのみ, トピックス, メインコンテンツタイトル]
        context['category_y'] = data_info['category_y']
        context['category_m'] = data_info['category_m']
        context['category_d'] = data_info['category_d']
        context['myform'] = [BookForm(), CategoryForm() ,AuthorForm()]
        # context['form_author'] = AuthorForm()
        # context['form_category'] = CategoryForm()

        try:
            context['date'] = data_info['data_info']
        except:
            pass
        try:
            context['book_info'] = self.model.objects.get(post_day=data_info['data_info'])
        except:
            pass
        return context

    def get_queryset(self, *args, **kwargs):
        # ■■■ urlの文字列で、クエリセットの分岐 ■■■
        data_info = self.get_date()
        if data_info['category_d'] != None:
            q = Book.objects.filter(post_day=datetime.date(int(data_info['category_y']), int(data_info['category_m']), int(data_info['category_d'])))
        else:
            q =  Book.objects.all()
        return q

    

    def get_template_names(self, *args, **kwargs):
        # ■■■ urlの文字列で、テンプレートの分岐 ■■■
        data_info = self.get_date()
        template_name = 'book/books_err.html'
        try:
            if data_info['data_info'] == None:
                template_name = 'book/books.html'
                return template_name
        except:
            pass
        try:
            if Book.objects.get(post_day=datetime.date(int(data_info['category_y']), int(data_info['category_m']), int(data_info['category_d']))):
                template_name = 'book/books_info.html'
                return template_name
        except:
            pass
        return template_name
    
    def get_date(self, *args, **kwargs):
        # ■■■ urlから日付データ取得 ■■■
        data_info = {}
        data_info['category_y'] = None
        data_info['category_m'] = None
        data_info['category_d'] = None
        data_info['data_info'] = None
        try:
            date_kwd = self.kwargs['data_info']
            data_info['data_info'] = date_kwd
            date_split = re.split(r"[-]", date_kwd)
            if len(str(date_split[0])) == 4:
                category_y = date_split[0]
                data_info['category_y'] = category_y
                if len(str(date_split[1])) == 2:
                    category_m = date_split[1]
                    data_info['category_m'] = category_m
                    if len(str(date_split[2])) == 2:
                        category_d = date_split[2]
                        data_info['category_d'] = category_d    
            return data_info
        except:
            return data_info

    # def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        # return render(request, self.template_name, {'form': form})


    # def post(self, request, *args, **kwargs):
    #     self.object = Manage
    #     form_value = {
    #         'youtube_video_title':self.request.POST.get('youtube_video_title', None),
    #         'youtube_video_day':self.request.POST.get('youtube_video_day', None),
    #         'youtube_video_episode':self.request.POST.get('youtube_video_episode', None),
    #         'category_id':self.request.POST.get('category_id', None),
    #         'members':self.request.POST.get('members', None),
    #     }
    #     request.session['form_value'] = form_value
    #     # 検索時にページネーションに関連したエラーを防ぐ
    #     self.request.POST = self.request.POST.copy()
    #     self.request.POST.clear()
    #     return render(request, 'hello/index.html', self.params)

    def post(self, request, *args, **kwargs):
            # 一覧表示からの遷移や、確認画面から戻った時
        context = super().get_context_data()
        data_info = self.get_date()


        context['myform'] = [BookForm(request.POST), CategoryForm(request.POST) ,AuthorForm(request.POST)]
        context2 = context['myform'][1]
        # aa

        # 送信された値が正しかった時の処理
        # BookForm(request.POST)
        # CategoryForm(request.POST)
        # AuthorForm(request.POST)

        # セッションにデータを格納
        request.session['form_data'] = request.POST
        # aa
        # 遷移させるページ
        return redirect('book:book')
        # コンテキストにフォームのオブジェクトを指定してレンダリング
        context = {
            'myform': [BookForm(request.POST), CategoryForm(request.POST) ,AuthorForm(request.POST)],
        }
        return render(request, 'hoge_form.html', context)





class SearchView(ListView):
    model = Book
    temlate_name = 'book/search.html'


def test_(request):
    params = {}
    params["aiueo"] = "aiueo"
    return render(request, 'book/test.html' , params)


# def sitemap(request):
#     return render(request, 'coupon/index.html', "")
    
"""
    'category'
    'author'
    'publisher'
    'series's
"""


"""
●ガジェット必要可否の context 追加
"""

"""
class HogeView(generic.TemplateView):

    template_name = 'app/template.html'

    def get_template_names(self):

        if self.request.user.is_superuser:
            template_name = 'app/template_superuser.html'
        elif self.request.user.is_authenticated:
            template_name = 'app/template_authenticated.html'
        else:
            template_name = self.template_name

        return [template_name]

"""

