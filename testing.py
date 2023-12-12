from yt_dlp import YoutubeDL

URLS = ['https://www.youtube.com/watch?v=dQw4w9WgXcQ']
with YoutubeDL() as ydl:
    ydl.download(URLS)