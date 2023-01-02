import tkinter as tk
from tkinter import *


class RadioUrl(tk.Frame):
    def __init__(self, parent, **kw):
        super().__init__(master=parent, **kw)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.var = StringVar()

        tk.Label(self, text="Choose the format please: ").grid(row=0, column=0, padx=5)

        video_radio = tk.Radiobutton(self, text="Video", variable=self.var, value="video")
        video_radio.grid(row=0, column=1, padx=5)
        video_radio.select()

        audio_radio = tk.Radiobutton(self, text="Audio", variable=self.var, value="audio")
        audio_radio.grid(row=0, column=2, padx=5)

    def get_format(self):
        return self.var.get()
