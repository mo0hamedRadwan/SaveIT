from django.shortcuts import render
from django.http import HttpResponse
from .downloader import YoutubeVideo

def youtube(request):
    return render(request, 'youtube/youtube.html')

def details(request):
    url = request.POST['url']

    yt_video = YoutubeVideo(url)
    yt_video.video_details()

    context = {
        'title': yt_video.title,
        'thumbnail': yt_video.thumbnail,
        'resolutions': yt_video.resolutions,
        'audios': yt_video.audios,
    }
    
    return render(request, 'youtube/download.html', context= context)