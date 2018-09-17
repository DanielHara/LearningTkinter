import tkinter as tk


class InsertFundForm:
    def __init__(self, master):
        self.master = master
        self.DEFAULT_SPACING = 10

        self.fund_bovespa_code_entry = self.makeentry(master, 'Fund Bovespa Code:', self.DEFAULT_SPACING)
        self.master_bovespa_code_entry = self.makeentry(master, 'Master Bovespa Code:', self.DEFAULT_SPACING)
        self.fund_name_entry = self.makeentry(master, 'Fund name:', self.DEFAULT_SPACING)
        self.description_entry = self.makeentry(master, 'Description:', self.DEFAULT_SPACING)


        self.insert_client_button = tk.Button(master, text="Insert Fund", command=self.insert_fund)
        self.insert_client_button.pack()
    
    def insert_fund(self):
        pass

    def makeentry(self, parent, caption, width=None, **options):
        tk.Label(parent, text=caption).pack(side=tk.TOP)
        entry = tk.Entry(parent, **options)
        if width:
            entry.config(width=width)
        entry.pack(side=tk.TOP)
        return entry


root = tk.Tk()
insert_fund_form = InsertFundForm(root)
root.mainloop()
