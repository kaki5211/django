from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
# from django.contrib.staticfiles.urls import static
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('base/', views.ManageView.as_view(), name="manage"),
    path('videos/', views.VideolistView.as_view(), name="videolist"),
]

#  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})



#     path('', views.BookView.as_view(), name="book"),
