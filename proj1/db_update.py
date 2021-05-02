import sys
# プロジェクトのパッケージを sys.path に追加する
sys.path.append(r'C:\Users\katsuki\Desktop\arikui_blog\django\proj1\proj1')
sys.path.append(r'django_project.app')
import django
import os
# 環境変数 DJANGO_SETTINGS_MODULE にプロジェクトの settings をセット
os.environ['DJANGO_SETTINGS_MODULE'] = 'proj1.settings'
django.setup()
# Model モジュールをインポートする
from app.models import Manage
# データベースを操作可能になる
Manage.objects.all()

from django.utils.timezone import make_aware

# -*- coding:utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options

# import pandas as pd
from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
import datetime

import re
import jaconv

import tweepy



dt_now = datetime.datetime.now()
API_KEY = 'AIzaSyBW_xwprJfz-yO-dmv4wX7CTqJ48CiY8cw'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
CHANNEL_ID = 'UCe14cApK5chdxcWewhMZR7g'
EL_ID = CHANNEL_ID
channels = [] #チャンネル情報を格納する配列
searches = [] #videoidを格納する配列
videos = [] #各動画情報を格納する配列
nextPagetoken = None
nextpagetoken = None
d_today = datetime.date.today() #今日の日付を取得
d_today_text = d_today.strftime('%Y-%m-%d') #今日の日付の表現変更
period_day = datetime.timedelta(days=2) #さかのぼりたい日付を取得（デルタ関数）
d_period_day = (d_today - period_day).strftime('%Y-%m-%d') #さかのぼりたい日付を取得

member = ["リク","ハルカ","リュージ","イナムー","ユウ","きよ"]
mem_num = len(member)


def twi(video,video_id):
    # 取得した各種キーを格納-----------------------------------------------------
    consumer_key ="CTZmmUUap52PyD9wxVGF1Uxte"
    consumer_secret ="njMacFCMmXXPQQ7441aehWwqrlftzO9y5tIRuqexJQNOzGMuOh"
    access_token="1230775413686718464-2ShCxUlLC1gpEjp31oZXUM0iQJ9Rdy"
    access_token_secret ="ec9qAwHJXykfjJ72JMO6LX4yZA9llLDwviOPEprX8P2IN"

    # Twitterオブジェクトの生成
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    #-------------------------------------------------------------------------
    # ツイートを投稿
    api.update_status("""こんばんは！アリクイチャンネルです！
    本日の動画はこちら、

     「{}」

    よかったら見ていってください！
    https://www.youtube.com/watch?v={}""".format(video, video_id))
    return

def epi(video):
    try:
        manageq_title_han = jaconv.z2h(video,digit=True, ascii=True)
        ep = re.search('#[0-9]+', manageq_title_han)
    except:
        episode = None
    try:
        episode = ep.group().replace("#", "")
        episode = int(episode)
    except:
        pass
    return episode


#YoutubeのAPIを登録
youtube = build(
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    developerKey=API_KEY
    )

#Youtubeのチャンネル情報登録
channel_response = youtube.channels().list(
    part = 'snippet,statistics',
    id = CHANNEL_ID
    ).execute()

#登録したチャンネルの動画情報を格納
for channel_result in channel_response.get("items", []):
    if channel_result["kind"] == "youtube#channel":
        channels.append([channel_result["snippet"]["title"],channel_result["statistics"]["subscriberCount"],channel_result["statistics"]["videoCount"],channel_result["snippet"]["publishedAt"]])

#一度に50個まで動画を取得できる？そのため複数回行う？
while True:
    if nextPagetoken != None:
        nextpagetoken = nextPagetoken

#チャンネルの動画情報を取得
    search_response = youtube.search().list(
      part = "snippet",
      channelId = CHANNEL_ID,
      maxResults = 50,
      order = "date", #日付順にソート
      pageToken = nextpagetoken, #再帰的に指定
      publishedAfter = d_period_day + "T00:00:00Z",
      publishedBefore = d_today_text + "T00:00:00Z",
      ).execute()


    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            searches.append(search_result["id"]["videoId"])

    try:
        nextPagetoken =  search_response["nextPageToken"]
    except:
        break
i = 0
for result in searches:
    video_response = youtube.videos().list(
      part = 'snippet,statistics',
      id = result
      ).execute()

    for video_result in video_response.get("items", []):
        if video_result["kind"] == "youtube#video":
            i = i + 1
            videos.append([result, video_result["snippet"]["title"],video_result["statistics"]["viewCount"],video_result["statistics"]["commentCount"],video_result["snippet"]["publishedAt"]])

a = 0
for video in videos:

    video_time = video[4]
    video_time = datetime.datetime.strptime(video_time, '%Y-%m-%dT%H:%M:%SZ')
    td = datetime.timedelta(hours=9)
    video_time = video_time + td
    video_time = make_aware(video_time)


    # if Manage.objects.filter(youtube_video_title=video[1]):
        # continue
    q = Manage.objects.filter(youtube_video_id=video[0]).count()
    if q == 0 and a <= 1:
        twi(video[1], video[0])
        try:
            episode = epi(video[1])
            q = Manage(youtube_video_id=video[0], youtube_video_title=video[1], youtube_video_day=video_time, youtube_video_episode=episode)
        except:
            q = Manage(youtube_video_id=video[0], youtube_video_title=video[1], youtube_video_day=video_time)
        q.save()
        a += 1
        break

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