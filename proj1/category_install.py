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
from app.models import Manage, Category, Member
# データベースを操作可能になる

import re

categorys = Category.objects.all().order_by('-category_id')
manages = Manage.objects.all()
members = Member.objects.all()



# エピソードインストール------------------------------------------------
for i in range(len(manages)):
    manageq_title = manages[i].youtube_video_title
    flag = 0
    try:
        manageq_title_han = jaconv.z2h(manageq_title,digit=True, ascii=True)
        ep = re.search('#[0-9]+', manageq_title_han)
    except:
        continue
    if ep == None:
        continue
    episode = ep.group().replace("#", "")
    episode = int(episode)
    q = Manage.objects.filter(youtube_video_title=manageq_title)
    q.update(youtube_video_episode=episode)
# エピソードインストール------------------------------------------------



# カテゴリーインストール------------------------------------------------
for manage in manages:
    ct = None
    ct_id = None
    for category in categorys:
        if None != re.search(jaconv.z2h(category.category_jp,digit=True, ascii=True), jaconv.z2h(manage.youtube_video_title,digit=True, ascii=True), flags=re.IGNORECASE):
            ct = re.search(category.category_jp, manage.youtube_video_title, flags=re.IGNORECASE)
            ct_id = category.category_id
        if re.search("ブリトニー", manage.youtube_video_title, flags=re.IGNORECASE) or re.search("キャプテンが", manage.youtube_video_title, flags=re.IGNORECASE)\
            or re.search("ピクミン3", manage.youtube_video_title, flags=re.IGNORECASE):
            ct_id = 1
            break
        if re.search("あつまれ　どうぶつの森", manage.youtube_video_title, flags=re.IGNORECASE):
            ct_id = 21
            break
        if re.search("ドラマ", manage.youtube_video_title, flags=re.IGNORECASE) and re.search("龍が如く", manage.youtube_video_title, flags=re.IGNORECASE):
            ct_id = 12
            break
        if re.search("ビューティフル ジョー", manage.youtube_video_title, flags=re.IGNORECASE):
            ct_id = 22
        if re.search("バイオハザード　アンブレラクロニクルズ", manage.youtube_video_title, flags=re.IGNORECASE):
            ct_id = 23
        if ct_id == None:
            ct_id = 25
    manage_q = Manage.objects.filter(youtube_video_title=manage.youtube_video_title)
    manage_q.update(category_id=ct_id)
# カテゴリーインストール------------------------------------------------


# メンバーインストール------------------------------------------------
for manage in manages:
    mem_id = None
    # 一回メンバークリア
    manage_q = Manage.objects.get(youtube_video_title = manage.youtube_video_title)
    manage_q.members.clear()

    for category in categorys:
        if str(manage.category_id) == str(category.category_jp):
            category_q = Category.objects.filter(category_id=category.category_id)
            member_qs = category_q[0].members.all()
            for member_q in member_qs:
                print(member_q, manage_q)
                manage_q.members.add(member_q)

    # 保留保留保留保留保留保留※※※※※※※※※※※※titleから該当するメンバーを抽出
    # for member in members:
    #     flag = 0
    #     member_judge = [" "+member.member_jp, "、"+member.member_jp, "["+member.member_jp, member.member_jp+"]", "【"+member.member_jp, member.member_jp+"】"]
    #     for judge in member_judge:
    #         if None != re.search(jaconv.z2h(judge,digit=True, ascii=True), jaconv.z2h(manage.youtube_video_title,digit=True, ascii=True), flags=re.IGNORECASE):
    #             flag == 1
        # 該当するメンバーがいた場合追加する
        # if flag == 1
        #     mem_id = category.category_id
        # member_q = Member.objects.filter(member_id=mem_id)
        # category_q = Manage.objects.filter(category_jp=category.category_jp)
        # category_q.members.add(member_q)
    # ※※※※※※※※※※※※※※※※※※※※※※※※※※
# メンバーインストール------------------------------------------------



# カテゴリーインストール【応急処置】------------------------------------------------
# for manage in manages:
#     ct = None
#     ct_id = None
#     for category in categorys:
#         if i == 0 :
#             print(category.category_jp)
#         if re.search("ブリトニー", manage.youtube_video_title, flags=re.IGNORECASE) or re.search("キャプテンが", manage.youtube_video_title, flags=re.IGNORECASE)\
#             or re.search("デラックス", manage.youtube_video_title, flags=re.IGNORECASE):
#             ct_id = 1
#             break
#         if re.search("ドラマ", manage.youtube_video_title, flags=re.IGNORECASE) and re.search("龍が如く", manage.youtube_video_title, flags=re.IGNORECASE):
#             ct_id = 12
#             break
#         if re.search("ビューティフル ジョー", manage.youtube_video_title, flags=re.IGNORECASE):
#             ct_id = 22
            # if re.search("アンブレラクロニクルズ", manage.youtube_video_title, flags=re.IGNORECASE):
                # ct_id = 23
#         if None != re.search(jaconv.z2h(category.category_jp,digit=True, ascii=True), jaconv.z2h(manage.youtube_video_title,digit=True, ascii=True), flags=re.IGNORECASE):
#             ct = re.search(category.category_jp, manage.youtube_video_title, flags=re.IGNORECASE)
#             ct_id = category.category_id
#     manage_q = Manage.objects.filter(youtube_video_title=manage.youtube_video_title)
#     manage_q.update(category_id=ct_id)
# カテゴリーインストール------------------------------------------------








