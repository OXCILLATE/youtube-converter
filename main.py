import flet as ft
from pytube import YouTube

link = "https://youtu.be/v8Upf5fz0AE"
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()