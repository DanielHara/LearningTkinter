import tkinter as tk
from tkinter import StringVar
import tkinter.ttk as ttk

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
        var = StringVar()
        combo_box = tk.OptionMenu(parent, var, *choices)
        combo_box.pack(side=tk.TOP)

        return combo_box, var

    def make_combo_box_2(self, parent, values):
        number = tk.StringVar()
        numberChosen = ttk.Combobox(parent, textvariable=number)
        numberChosen['values'] = values
        numberChosen.pack()
        numberChosen.current(0)

        return numberChosen, number
