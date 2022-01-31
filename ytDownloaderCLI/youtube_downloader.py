from pytube import YouTube
import sys
import os
from pathlib import Path

class YoutubeDownloader:

    def __init__(self, link, resolution):
        self.__link = link
        self.__resolution = resolution

    def downloadVideo(self):
        # Salva o vídeo na pasta de Downloads
        SAVE_PATH = os.path.join(Path.home(), 'Downloads')

        try:
            yt = YouTube(self.__link)
        except Exception as error:
            print('Error: {}'.format(error))
            sys.exit()

        files = yt.streams
        #print(files)

        mp4files = files.filter(file_extension='mp4', progressive=True)

        if self.__resolution:
            file = mp4files.get_by_resolution(self.__resolution)
        else:
            file = mp4files.get_highest_resolution()

        print(file)
        try:
            file.download(SAVE_PATH)
        except Exception as error:
            print('Resolution not available for this video')
            sys.exit()
        print(f'The video {file.title} was downloaded successfully!')
