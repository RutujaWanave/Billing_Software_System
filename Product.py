from operator import inv
from time import strftime
from tkinter import *
from tkinter import ttk, messagebox

from addProduct2 import add


import pyodbc



connection = pyodbc.connect('DRIVER={SQL Server};'
                                    'SERVER=DESKTOP-R5569UO\SQLEXPRESS;'
                                    ' DATABASE=MVC; Trusted_Connection=yes;')
Cursor = connection.cursor()
class Inventory:
    def __init__(self, root):

        #Cursor.execute("select * from Product")
        #connection.commit()
        self.root = root
        self.root.geometry("1366x786")
        self.root.title("Inventory")
        self.root.configure(bg="#000000")


    #    root.geometry("1366x768")
     #   root.resizable(0, 0)
      #  root.title("Inventory")
        self.label1 = Label(root)
        """self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/inventory.png")
        self.label1.configure(image=self.img)"""

        self.label2=Label(root)
        self.label2.place(relx=0.500, rely=0.100, width=300, height=25)
        self.label2.configure(text="Product Management")
        self.label2.configure(foreground="white")
        self.label2.configure(font="-family {Poppins Light} -size 25")
        self.label2.configure(background="black")

        self.message = Label(root)
        self.message.place(relx=0.046, rely=0.055, width=136, height=30)
        self.message.configure(font="-family {Poppins} -size 10")
        self.message.configure(foreground="#000000")
        self.message.configure(background="#ffffff")
        self.message.configure(text="""ADMIN""")
        self.message.configure(anchor="w")
        def time():
            string = strftime('%H:%M:%S %p')
            self.clock.config(text=string)
            self.clock.after(1000, time)
        self.clock = Label(root)
        self.clock.place(relx=0.84, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 13")
        self.clock.configure(background='pink')
        self.clock.configure(foreground='blue')
        time()
       # self.clock = Label(root)
       # self.clock.place(relx=0.9, rely=0.065, width=102, height=36)
       # self.clock.configure(font="-family {Poppins Light} -size 12")
       # self.clock.configure(foreground="#000000")
       # self.clock.configure(background="#ffffff")

        self.entry1 = Entry(root)
        self.entry1.place(relx=0.040, rely=0.286, width=240, height=28)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")

        self.button1 = Button(root)
        self.button1.place(relx=0.229, rely=0.289, width=76, height=23)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#CF1E14")
        self.button1.configure(font="-family {Poppins SemiBold} -size 10")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Search""")
        self.button1.configure(command=self.search)

     #   self.button2 = Button(root)
     #   self.button2.place(relx=0.035, rely=0.106, width=76, height=23)
     #   self.button2.configure(relief="flat")
     #   self.button2.configure(overrelief="flat")
     #   self.button2.configure(activebackground="#CF1E14")
     #   self.button2.configure(cursor="hand2")
      #  self.button2.configure(foreground="#ffffff")
      #  self.button2.configure(background="#CF1E14")
      #  self.button2.configure(font="-family {Poppins SemiBold} -size 12")
      #  self.button2.configure(borderwidth="0")
      #  self.button2.configure(text="""Logout""")
       # self.button2.configure(command=self.Logout)
        self.button3 = Button(root)
        self.button3.place(relx=0.052, rely=0.432, width=306, height=28)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#CF1E14")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#ffffff")
        self.button3.configure(background="#CF1E14")
        self.button3.configure(font="-family {Poppins SemiBold} -size 12")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""ADD PRODUCT""")
        self.button3.configure(command=self.addProduct2)
       # self.button3.configure(command=self.add_product)
        #self.button4 = Button(root)
       # self.button4.place(relx=0.052, rely=0.5, width=306, height=28)
       # self.button4.configure(relief="flat")
       # self.button4.configure(overrelief="flat")
        #self.button4.configure(activebackground="#CF1E14")
       # self.button4.configure(cursor="hand2")
       # self.button4.configure(foreground="#ffffff")
       # self.button4.configure(background="#CF1E14")
       # self.button4.configure(font="-family {Poppins SemiBold} -size 12")
       # self.button4.configure(borderwidth="0")
      #  self.button4.configure(text="""UPDATE PRODUCT""")
       # self.button4.configure(command=self.update_product)
   #     self.button4.configure(command=self.addProduct2)

        self.button5 = Button(root)
        self.button5.place(relx=0.052, rely=0.57, width=306, height=28)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="#CF1E14")
        self.button5.configure(cursor="hand2")
        self.button5.configure(foreground="#ffffff")
        self.button5.configure(background="#CF1E14")
        self.button5.configure(font="-family {Poppins SemiBold} -size 12")
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="""DELETE PRODUCT""")
        self.button5.configure(command=self.database)

        self.Proid = IntVar()
        self.entry2=Entry(root,textvariable=self.Proid)
        self.entry2.place(relx=0.052, rely=0.65, width=306, height=28)

      #  self.button5.configure(command=self.delete_product)
        self.button6 = Button(root)
        self.button6.place(relx=0.135, rely=0.885, width=76, height=23)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#CF1E14")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#ffffff")
        self.button6.configure(background="#CF1E14")
        self.button6.configure(font="-family {Poppins SemiBold} -size 12")
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""EXIT""")
        self.button6.configure(command=self.exitt)
        self.scrollbarx = Scrollbar( orient=HORIZONTAL)
        self.scrollbary = Scrollbar( orient=VERTICAL)

        self.tree = ttk.Treeview(root)
 #       self.tree['show']='heading'
        s=ttk.Style(root)
        s.theme_use("clam")
        s.configure(".",font=('Helvetica',11))
        s.configure("Treeview.Heading",foreground='red',font=('Helvetica',11,'bold'))



        self.tree.place(relx=0.307, rely=0.203, width=880, height=550)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")
    #    self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)
        self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
        self.scrollbarx.place(relx=0.307, rely=0.924, width=884, height=22)
        self.tree.configure(
            columns=(
                "Product ID",
                "Name",
                "Category",
                "Sub-Category",

            )
        )
        self.tree.heading("Product ID", text="Product ID", anchor=W)
        self.tree.heading("Name", text="Name", anchor=W)
        self.tree.heading("Category", text="Category", anchor=W)
        self.tree.heading("Sub-Category", text="Sub-Category", anchor=W)


        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=80)
        self.tree.column("#2", stretch=NO, minwidth=0, width=180)
        self.tree.column("#3", stretch=NO, minwidth=0, width=180)
        self.tree.column("#4", stretch=NO, minwidth=0, width=180)
        self.DisplayData()

    def database(self):

        if (self.Proid == " "):
            messagebox.showinfo("plsese enter name")

        Proid = self.Proid.get()
        connection = pyodbc.connect('DRIVER={SQL Server};'
                                    'SERVER=DESKTOP-R5569UO\SQLEXPRESS;'
                                    ' DATABASE=MVC; Trusted_Connection=yes;')
        Cursor = connection.cursor()
        query = "delete from Product where Proid=?"

        val = (Proid)
        Cursor.execute(query, val)

        connection.commit()
       # messagebox.showinfo("Success!!", "Products deleted from database.")
        selected_item = self.tree.selection()
        if selected_item:
            x = selected_item[0]
            self.tree.delete(x)

    def addProduct2(self):
      self.new_win = Toplevel(self.root)
      self.new_obj = add(self.new_win)

    def deleteProduct(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = add(self.new_win)

   # def del(self):
    #    selected_item=self.Treeview.selection()[0]





    #using treeview delete Record
  #selected_item=[]   Conform delete
    def delete(self):
        selected_item = self.tree.selection()[0]
        Cursor.execute('')
        connection.commit()
    #1   selected_item=self.tree.selection()
      #1  if selected_item:
       #1   x=selected_item[0]
       #     self.tree.delete(x)
            #sql='delete from Product where Proid=?'
      #      Cursor.execute('delete from Product where Proid=x')
         #   connection.commit()
     #   print(self.tree(selected_item)['values'])
       # #uid=self.tree(selected_item)['values'][0]
        #del_query="delete from Product where Proid=?"
    #    sel_data=(uid,)
     #   Cursor.execute(del_query,selected_item)
      #  connection.commit()
       # self.tree.delete(selected_item)




    def DisplayData(self):
        Cursor.execute("SELECT * FROM Product")
        fetch = Cursor.fetchall()
        for data in fetch:
    #self.tree.insert('',"end", values=(data))
          i=0
        #for ro in connection:
          self.tree.insert('',i+100,text="",values=(data[0],data[1],data[2],data[3]))
          i=i+1




        #self.tree.pack()


    # self.button6.configure(command=self.Exit)
    sel = []

    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def delete_product(self):
        val = []
        to_delete = []
        for k in to_delete:
            delete = "DELETE FROM Product WHERE Proid = ?"
            Cursor.execute(delete, [k])
            connection.commit()
            messagebox.showinfo("Success!!", "Products deleted from database.", parent=inv)
            self.sel.clear()
            self.tree.delete(*self.tree.get_children())
            self.DisplayData()

    def exitt(self):
       # sure = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        #if sure == True:
            self.root.destroy()

    def search(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)
        try:
            to_search = int(self.entry1.get())
        except ValueError:
            messagebox.showerror("Oops!!", "Invalid Product Id.")
        else:
            for search in val:
                if search == to_search:
                    self.tree.selection_set(val[val.index(search) - 1])
                    self.tree.focus(val[val.index(search) - 1])
              #      messagebox.showinfo("Success!!", "Product ID: {} found.".format(self.entry1.get()))
                    break
            else:
              messagebox.showerror("Oops!!", "Product ID: {} not found.".format(self.entry1.get()))


if __name__ == '__main__':
    root = Tk()
    obj = Inventory(root)
    root.mainloop()