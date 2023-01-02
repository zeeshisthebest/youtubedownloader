import threading
import traceback

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
        t2.daemon = True
        t2.start()

    def select_stream_type(self, media):
        if self.format == "video":
            return media.streams.filter(progressive=True).get_highest_resolution()
        elif self.format == "audio":
            return media.streams.filter(only_audio=True).get_audio_only()
            # return media.streams.filter(only_audio=True)[0]

    def download_each(self):

        for link in self.list:
            print("Downloading " + link)
            try:
                media = YouTube(link)
                self.t1.set_info(media.title, media.length)
            except VideoUnavailable as e:
                print(e)
                dl.Success("Error", f"Unable to download {link}")
            except Exception:
                dl.Success("Error", "The link is not correct")
            else:
                try:
                    self.select_stream_type(media).download(self.path)
                except Exception as e:
                    print(e)
                    print(f"unable to download: " + link)

        self.t1.destroy()
        dl.Success("Downloaded All", "Download completed!")
