import argparse
from youtube_downloader import YoutubeDownloader


class YoutubeDownloaderCLI:
    __parser = argparse.ArgumentParser()

    def __init__(self):
        self.__run(self.__parser)

    def __run(self, parser):
        self.__createArgs(parser)

        args = parser.parse_args()
        self.__createDownloader(args)

    def __createArgs(self, parser):
        parser.add_argument('link', help='The link of the video from YouTube')
        parser.add_argument('-r', '--resolution', help='The resolution in which the video will be downloaded [144p, 360p, 480p, 720p]')

    def __createDownloader(self, args):
        yt_downloader = YoutubeDownloader(args.link, args.resolution)
        yt_downloader.downloadVideo()
