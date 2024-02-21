from pytube import YouTube
import os


class YoutubeVideo:
    def __init__(self, url):
        self.yt = YouTube(url)
        self.url = url
        self.title = self.yt.title
        self.thumbnail = self.yt.thumbnail_url
        self.streams = self.yt.streams.filter(file_extension= 'mp4')
        self.resolutions = []
        self.audios = []

    def video_details(self):
        for res in ['144p', '240p', '360p', '480p', '720p', '1080p']:
            self.resolutions.append({
                'resolution' : res,
                'stream' : self.streams.get_by_resolution(res),
            })


        for abr in ['32kbps', '64kbps', '128kbps', '192kbps']:
            self.audios.append({
                'abr' : abr,
                'stream' : self.streams.filter(only_audio= True, abr= abr)
            })