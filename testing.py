from yt_dlp import YoutubeDL

URLS = ['https://www.youtube.com/watch?v=dQw4w9WgXcQ']

output = {
  'outtmpl': 'C:/Users/Emile/OneDrive/Proj/Python/Video_Downloader/VidOutput/%(uploader)s/%(title)s.%(ext)s'
}

with YoutubeDL(output) as ydl:
    ydl.download(URLS)