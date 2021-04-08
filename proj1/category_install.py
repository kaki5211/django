import sys
# プロジェクトのパッケージを sys.path に追加する
sys.path.append(r'C:\Users\katsuki\Desktop\arikui_blog\django\proj1\proj1')
sys.path.append(r'django_project.app')
import django
import os
import jaconv
# 環境変数 DJANGO_SETTINGS_MODULE にプロジェクトの settings をセット
os.environ['DJANGO_SETTINGS_MODULE'] = 'proj1.settings'
django.setup()
# Model モジュールをインポートする
from app.models import Manage, Category
# データベースを操作可能になる

import re

categorys = Category.objects.all()
manages = Manage.objects.all()


# エピソードインストール------------------------------------------------
# for i in range(260):
#     manageq_title = manages[i].youtube_video_title
#     flag = 0
#     try:
#         manageq_title_han = jaconv.z2h(manageq_title,digit=True, ascii=True)
#         ep = re.search('#[0-9]+', manageq_title_han)
#     except:
#         continue
#     if ep == None:
#         continue
#     episode = ep.group().replace("#", "")
#     episode = int(episode)
#     q = Manage.objects.filter(youtube_video_title=manageq_title)
#     q.update(youtube_video_episode=episode)
# エピソードインストール------------------------------------------------



# ※※※※※※未完成※※※※※※
# カテゴリーインストール------------------------------------------------
# for i in range(10):
#     manageq_title = manages[i].youtube_video_title
#     for a in range(5):
#         categoryq_jp = categorys[a].category_jp
#         ct = re.search(categoryq_jp, manageq_title)
#         if ct != None:
#             break

#     if ct != None:
#         q = manages[i]
#         q.update(youtube_video_category.categoryq_jp=category)
# カテゴリーインストール------------------------------------------------




