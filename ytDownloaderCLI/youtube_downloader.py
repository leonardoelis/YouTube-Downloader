from pytube import YouTube
import sys

class YoutubeDownloader:

    def __init__(self):
        pass

    def downloadVideo(self):
        SAVE_PATH = "C:\\Users\\leona\\Downloads"

        link = 'https://www.youtube.com/watch?v=mpWVjiFUihc'

        try:
            yt = YouTube(link)
        except:
            print('Connection Error!')

        mp4files = yt.streams
        print(mp4files)

        files = mp4files.filter(file_extension='mp4', progressive=True)

        file = files.get_by_resolution('720p')
        print(file)
        try:
            file.download(SAVE_PATH)
        except Exception as e:
            print('Error: {}'.format(e))
            sys.exit()
        print('Video downloaded successfully!')