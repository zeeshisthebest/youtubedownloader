
# from future.moves import tkinter as tk
import tkinter as tk


class SaveFile(tk.Toplevel):
    def __init__(self, path, format_type, **kw):
        super().__init__(**kw)
        self.grab_set()
        self.resizable(width=False, height=False)
        self.format_type = format_type
        tk.Label(self, text=f"saving to: {path}").grid(padx=20, pady=10)

        self.name = tk.Label(self, text=f"{self.format_type} Name: ----")
        self.name.grid(padx=20, pady=10)

        self.length = tk.Label(self, text="00:00")
        self.length.grid(padx=20, pady=10)

    def set_info(self, name, length):
        self.name['text'] = f"{self.format_type} Name: {name}"
        self.length['text'] = f"{length // 60}:{length % 60}"
