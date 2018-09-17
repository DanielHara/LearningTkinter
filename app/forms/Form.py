import tkinter as tk

class Form:
    def __init__(self):
        pass

    def makeentry(self, parent, caption, width=None, **options):
        tk.Label(parent, text=caption).pack(side=tk.TOP)
        entry = tk.Entry(parent, **options)
        if width:
            entry.config(width=width)
        entry.pack(side=tk.TOP)
        return entry

