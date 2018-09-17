from tkinter import Tk, Label, Button, StringVar, Entry, LEFT, Checkbutton, IntVar
from database.ClientService import ClientService


class InsertClientForm:
    def __init__(self, master):
        self.master = master
        self.client_service = ClientService('whatever')
        self.DEFAULT_SPACING = 10

        master.title("A simple GUI")

        self.bovespa_code_entry = self.makeentry(master, 'Bovespa code: ', self.DEFAULT_SPACING)
        self.name_entry = self.makeentry(master, 'Name: ', self.DEFAULT_SPACING)
        self.description_entry = self.makeentry(master, 'Description: ', self.DEFAULT_SPACING)
        
        self.master_account_int = IntVar()
        self.master_account_check = Checkbutton(master, text="Is master account?", variable=self.master_account_int)
        self.master_account_check.pack()
        
        self.insert_client_button = Button(master, text="Insert Client", command=self.insert_client)
        self.insert_client_button.pack()
    
    def insert_client(self):
        bovespa_code = self.bovespa_code_entry.get()
        name = self.name_entry.get()
        description = self.description_entry.get()
        is_master_account = not not (self.master_account_int.get())

        if self.client_service.validate_insert_data(bovespa_code, name, description, is_master_account):
            self.client_service.insert_client(bovespa_code, name, description, is_master_account)
        else:
            print('Invalid data')

    def makeentry(self, parent, caption, width=None, **options):
        Label(parent, text=caption).pack(side=LEFT)
        entry = Entry(parent, **options)
        if width:
            entry.config(width=width)
        entry.pack(side=LEFT)
        return entry

root = Tk()
insert_client_form = InsertClientForm(root)
root.mainloop()

