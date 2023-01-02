import tkinter as tk
from tkinter import *


class UrlFrame(tk.Frame):
    def __init__(self, parent, **kw):
        super().__init__(master=parent, **kw)

        tk.Label(master=self, text="Enter the urls, one per each line only!!").pack(side="top", fill='x')

        self.scrollbar_x = tk.Scrollbar(master=self, orient="horizontal")
        self.scrollbar_y = tk.Scrollbar(master=self, orient="vertical")

        self.scrollbar_x.pack(side='bottom', fill='x')
        self.scrollbar_y.pack(side='right', fill='y')

        self.url_box = tk.Text(master=self, bd=2, height=12, highlightthickness=1,
                               xscrollcommand=self.scrollbar_x.set,
                               yscrollcommand=self.scrollbar_y.set,
                               wrap='none')
        self.url_box.pack(side='left', fill=BOTH, expand=True)

        self.scrollbar_x.config(command=self.url_box.xview)
        self.scrollbar_y.config(command=self.url_box.yview)

    def get_each_url(self):
        all_lines = self.url_box.get("1.0", "end-1c")
        all_lines = all_lines.split("\n")

        while "" in all_lines:
            all_lines.remove("")

        return all_lines
