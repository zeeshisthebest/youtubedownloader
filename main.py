import media_downloader
import radiobutton as rb
import download_location as dl
import tkinter as tk
from tkinter import *
import urls_frame as uf


def main():
    def download_now():
        url_list = url_frame.get_each_url()
        format_type = format_radio.get_format()
        path_to = location_frame.get_location()
        media_downloader.DownloadingWindow(urls_list=url_list, path=path_to, media_format=format_type)

    root = tk.Tk()
    root.title("Youtube Downloader")

    root.columnconfigure(0, weight=1)

    tk.Label(master=root, text="").grid(row=0)  # Empty row for padding

    title = tk.Label(master=root, text="YOUTUBE DOWNLOADER", font=('bold', 15))
    title.grid(row=1, sticky=E + W)

    url_frame = uf.UrlFrame(root)
    url_frame.grid(padx=10, sticky=E + W)

    tk.Label(master=root, text="").grid()  # Empty row for padding

    format_radio = rb.RadioUrl(root)
    format_radio.grid()

    tk.Label(master=root, text="").grid()  # Empty row for padding

    location_frame = dl.DownloadLocation(master=root)
    location_frame.grid(padx=5)

    tk.Label(master=root, text="").grid(row=0)  # Empty row for padding

    tk.Button(root, text="Download Now", command=download_now).grid()

    tk.Label(master=root, text="").grid()  # Empty row for padding

    root.mainloop()


if __name__ == "__main__":
    main()
