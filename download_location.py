import pathlib
import tkinter.filedialog as fd
import tkinter as tk
from tkinter.messagebox import showinfo


class DownloadLocation(tk.Frame):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.path = tk.StringVar()
        self.path.set(pathlib.Path().resolve())

        tk.Label(self, text="Please select the download location:",
                 justify='center').grid(row=0, columnspan=2, sticky="we")

        self.pathEntry = tk.Entry(self, text=self.path, width=100)
        self.pathEntry.grid(row=1, padx=5, pady=10, column=0, sticky='we')

        tk.Button(self, text="Choose Location", command=self.get_path).grid(row=1, padx=10, pady=10, column=1)

    def get_path(self):
        self.path = fd.askdirectory()
        if self.path is None:
            return
        self.pathEntry.delete(0, tk.END)
        self.pathEntry.insert(0, self.path)

    def get_location(self):
        return self.pathEntry.get()


class Success:
    def __init__(self, title, msg):
        showinfo(title, msg)
