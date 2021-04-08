from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
# from django.contrib.staticfiles.urls import static
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('top/', views.ManageView.as_view(), name="top"),
    path('video/', views.VideosView.as_view(), name="videos"),
    path('videoserch/', views.VideosearchView.as_view(), name="video_search"),

    path('video/member/', views.MembersView.as_view(), name="members"),
    path('video/category/', views.CategorysView.as_view(), name="categorys"),
    path('video/<slug:category_eng>', views.CategoryinfoView.as_view(), name="ctegory_info"),

    path('video/member/<slug:member_eng>', views.MemberinfoView.as_view(), name="member_info"),
    path('video/uncategorize/<int:pk>/', views.VideoView.as_view(), name="video_info_un"),
    path('video/<slug:category_eng>/<int:youtube_video_episode>/', views.VideoView.as_view(), name="video_info"),

    path('videos/', views.VideolistView.as_view(), name="videolist"),
]

#  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})



#     path('', views.BookView.as_view(), name="book"),
