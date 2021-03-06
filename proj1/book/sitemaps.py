# from django.contrib.sitemaps import Sitemap
# from django.urls import reverse

# from .models import Book


# class BlogPostSitemap(Sitemap):
#     """
#     ブログ記事のサイトマップ
#     """
#     changefreq = "never"
#     priority = 0.8

#     def items(self):
#         return Book.objects.filter(is_public=True)

#     # モデルに get_absolute_url() が定義されている場合は不要
#     def location(self, obj):
#         data_info=(obj.post_day).strftime("%Y-%m-%d")
#         return resolve_url('book:book_info', data_info=data_info)
        

#     def lastmod(self, obj):
#         return obj.pub_date


# class StaticViewSitemap(Sitemap):
#     """
#     静的ページのサイトマップ
#     """
#     changefreq = "daily"
#     priority = 0.5

#     def items(self):
#         return ['blog:index', 'blog:category_list', 'blog:tag_list']

#     def location(self, item):
#         return reverse(item)