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

# -*- coding:utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options

# import pandas as pd
from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
import datetime

dt_now = datetime.datetime.now()
API_KEY = 'AIzaSyA3TijmbZm5Q3ItC9i6sNNOLq77xQTz4b0'
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
period_day = datetime.timedelta(weeks=60) #さかのぼりたい日付を取得（デルタ関数）
d_period_day = (d_today - period_day).strftime('%Y-%m-%d') #さかのぼりたい日付を取得

member = ["リク","ハルカ","リュージ","イナムー","ユウ","きよ"]
mem_num = len(member)





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

for video in videos:
    print(video[0])
    print(video[1])
    print(video[4])
    video_time = video[4]

    video_time = datetime.datetime.strptime(video_time, '%Y-%m-%dT%H:%M:%SZ')

    try:
        dammy = Manage.objects.filter(body_text__contain=video[0])
        continue
    except:
        pass
        
    q = Manage(youtube_video_id=video[0], youtube_video_title=video[1], youtube_video_day=video_time)
    q.save()