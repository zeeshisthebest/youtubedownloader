import threading

from pytube import YouTube
from pytube.exceptions import VideoUnavailable
from downloadprogress import SaveFile as sf

import download_location as dl


class DownloadingWindow:
    def __init__(self, urls_list, path, media_format):
        self.path = path
        self.format = media_format
        self.list = urls_list
        self.t1 = sf(self.path, self.format)

        t2 = threading.Thread(target=self.download_each)
        if t2.start():
            dl.Success("Downloaded All", "Download completed!")

    def select_stream_type(self, media):
        if self.format == "video":
            return media.streams.filter(progressive=True)
        elif self.format == "audio":
            return media.streams.filter(only_audio=True)

    def download_each(self):

        for link in self.list:
            print(link)
            try:
                media = YouTube(link)
                self.t1.set_info(media.title, media.length)
            except VideoUnavailable:
                dl.Success("Error", f"Unable to download {link}")
                return False
            except Exception:
                dl.Success("Error", "The link is not correct")
                return False
            else:
                # self.select_stream_type(media).first().download(self.path)
                self.select_stream_type(media).get_highest_resolution().download(self.path)
        self.t1.destroy()
        return True
