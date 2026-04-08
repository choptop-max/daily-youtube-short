from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import datetime
import os

START_DATE = datetime.date(2024, 12, 1)
TODAY = datetime.date.today()
days_waiting = (TODAY - START_DATE).days

title = f"Жду запчасти уже {days_waiting} дней"
description = f"Дилер до сих пор не отправил запчасти. День {days_waiting}."
tags = ["waiting", "dealer", "parts", f"day{days_waiting}", "shorts"]

youtube = build("youtube", "v3")

request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": "22"
        },
        "status": {
            "privacyStatus": "public"
        }
    },
    media_body=MediaFileUpload("output.mp4")
)

response = request.execute()
print("Видео загружено:", response)
