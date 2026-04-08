import os
import random
import datetime
import subprocess

START_DATE = datetime.date(2024, 12, 1)  # ← измени на дату, когда начал ждать
TODAY = datetime.date.today()
days_waiting = (TODAY - START_DATE).days

# выбираем случайное фото
photos = os.listdir("photos")
photo = "photos/" + random.choice(photos)

# текст
text = f"Жду запчасти уже {days_waiting} дней"

# создаём видео
output = "output.mp4"

cmd = [
    "ffmpeg",
    "-loop", "1",
    "-i", photo,
    "-vf", f"drawtext=text='{text}':fontcolor=white:fontsize=48:x=(w-text_w)/2:y=h-100",
    "-t", "10",
    "-y",
    output
]

subprocess.run(cmd)
print("Видео создано:", output)
