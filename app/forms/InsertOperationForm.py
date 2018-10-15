
import tkinter as tk
from Form import Form


class InsertOperationForm(Form):
    def __init__(self, master):
        self.master = master

        self.client_code_entry = self.makeentry(master, 'Client Bovespa Code:')
        self.in_date_entry = self.makeentry(master, 'In-Date:')
        
        self.quantity_entry = self.makeentry(master, 'Quantity:')

        self.expiry_date_entry = self.makeentry(master, 'Expiry-Date:')

        self.listed1_entry = self.makeentry(master, 'Listed 1:')
        self.listed2_entry = self.makeentry(master, 'Listed 2:')
        self.listed3_entry = self.makeentry(master, 'Listed 3:')

        self.flex1_entry = self.makeentry(master, 'Flex 1:')
        self.flex2_entry = self.makeentry(master, 'Flex 2:')
        self.flex3_entry = self.makeentry(master, 'Flex 3:')

        self.premium_in_1_entry = self.makeentry(master, 'Premium In 1:')
        self.premium_in_2_entry = self.makeentry(master, 'Premium In 2:')
        self.premium_in_2_entry = self.makeentry(master, 'Premium In 3:')

        self.revenue_entry = self.makeentry(master, 'Revenue:')

        choices = {'pineapples', 'bananas'}
        self.combo_box = self.make_combo_box(master, 'Strategy:', choices)

        choices_2 = ('C', 'V')
        self.combo_box_2, self.chosen_2 = self.make_combo_box_2(master, choices_2)

        self.insert_operation_button = tk.Button(master, text="Insert Operation", command=self.insert_operation)
        self.insert_operation_button.pack()

    def insert_operation(self):
        print('self.chosen_2=' + self.chosen_2.get())
        pass

root = tk.Tk()
insert_operation_form = InsertOperationForm(root)
root.mainloop()
