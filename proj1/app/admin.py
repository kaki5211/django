from django.contrib import admin

# Register your models here.

from .models import Manage, Member, Category



# admin.site.register(Manage)
# admin.site.register(Category)
admin.site.register(Member)


 
 
# class MwmberInline(admin.TabularInline):
#     model = Member
#     extra = 3
 
class ManageAdmin(admin.ModelAdmin):
    list_display = ('youtube_video_title', 'youtube_video_episode', 'youtube_video_day', 'category_id')
    # fieldsets = [
    #     (None, {'fields': ['youtube_video_title']}),
    #     ('メンバー', {'fields': ['members'],}),
    #     ('#', {'fields': ['youtube_video_episode'],}),
    # ]

    search_fields = ['youtube_video_title']
    # search_fields = ['youtube_video_category']
    # list_filter = ['members']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_id", "category_jp", "category_eng")
    # fieldsets = [
    #     ("カテゴリーjp", {'fields':['category_jp']}),
    #     ("カテゴリーeng", {'fields':['category_eng']}),

    # ]

admin.site.register(Manage, ManageAdmin)

admin.site.register(Category, CategoryAdmin)




# class ManageAdmin(admin.ModelAdmin):

