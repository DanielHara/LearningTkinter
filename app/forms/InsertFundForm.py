import tkinter as tk
from Form import Form


class InsertFundForm(Form):
    def __init__(self, master):
        self.master = master

        self.fund_bovespa_code_entry = self.makeentry(master, 'Fund Bovespa Code:')
        self.master_bovespa_code_entry = self.makeentry(master, 'Master Bovespa Code:')
        self.fund_name_entry = self.makeentry(master, 'Fund name:')
        self.description_entry = self.makeentry(master, 'Description:')


        self.insert_client_button = tk.Button(master, text="Insert Fund", command=self.insert_fund)
        self.insert_client_button.pack()
    
    def insert_fund(self):
        pass


root = tk.Tk()
insert_fund_form = InsertFundForm(root)
root.mainloop()
