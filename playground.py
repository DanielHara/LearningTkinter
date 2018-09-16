from tkinter import Tk, Label, Button, StringVar, Entry, LEFT

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.text_entry = Entry(master)
        self.text_entry.pack()

        self.user_entry = self.makeentry(master, 'User name:', 10)
        
        self.insert_client_button = Button(master, text="Insert Client", command=self.insert_client)
        self.insert_client_button.pack()

    def print_text_in_entry(self):
        text = self.text_entry.get()
        print(str(text))
    
    def insert_client(self):
        bovespa_code = self.text_entry.get()
        print('Bovespa code:' + bovespa_code)
        print('Client inserted!')
    

    def makeentry(self, parent, caption, width=None, **options):
        Label(parent, text=caption).pack(side=LEFT)
        entry = Entry(parent, **options)
        if width:
            entry.config(width=width)
        entry.pack(side=LEFT)
        return entry

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()

