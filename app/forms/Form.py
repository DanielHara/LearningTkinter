import tkinter as tk

DEFAULT_SPACING = 10

class Form:
    def __init__(self):
        self.DEFAULT_SPACING = DEFAULT_SPACING

    def makeentry(self, parent, caption, width=DEFAULT_SPACING, **options):
        tk.Label(parent, text=caption).pack(side=tk.TOP)
        entry = tk.Entry(parent, **options)
        if width:
            entry.config(width=width)
        entry.pack(side=tk.TOP)
        return entry

    # choices deve ser um dict
    def make_combo_box(self, parent, caption, choices, **options):
        tk.Label(parent, text=caption).pack(side=tk.TOP)
        combo_box = tk.OptionMenu(parent, None, *choices)
        combo_box.pack(side=tk.TOP)

        return combo_box
