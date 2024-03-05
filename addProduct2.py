from time import strftime
from tkinter import *
from tkinter import messagebox


import pyodbc


class add:
    def __init__(self, root):

        #Cursor.execute("select * from Product")
        #connection.commit()
        self.root = root
        self.root.geometry("1366x786")
        self.root.title("Add Product")
        self.root.configure(bg="#000000")

        self.name=StringVar()
        self.category=StringVar()
        self.subcategory=StringVar()


     #   self.label1 = Label(root)
      #  self.label1.place(relx=0, rely=0, width=2000, height=500)
       # self.label1.configure(text="Product Name")
        #   self.img = PhotoImage(file="./images/add_product.png")
        #    self.label1.configure(image=self.img)
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

        self.label2 = Label(root)
        self.label2.place(relx=0.200, rely=0.100, width=800, height=50)
        self.label2.configure(text="Add Product")
        self.label2.configure(font="-family {Poppins} -size 30")
        self.label2.configure(foreground="#DC143C", background="#000000")

        self.label3 = Label(root)
        self.label3.place(relx=0.100, rely=0.250, width=300, height=20)
        self.label3.configure(font="-family {Poppins} -size 15")
        self.label3.configure(text="Product Name")
        self.label3.configure(foreground="#ffffff",background="#000000")
        self.entry1 = Entry(root, textvariable=self.name)
        self.entry1.place(relx=0.132, rely=0.296, width=400, height=35)
        self.entry1.configure(font="-family {Poppins} -size 15")
        self.entry1.configure(relief="flat")
        self.entry1.configure(highlightbackground="black")
        self.entry1.configure(borderwidth=4)

        self.label2 = Label(root)
        self.label2.place(relx=0.100, rely=0.340, width=310, height=50)
        self.label2.configure(text="Product cat")
        self.label2.configure(font="-family {Poppins} -size 15")
        self.label2.configure(foreground="#ffffff",background="#000000")
        self.entry2 = Entry(root, textvariable=self.category)
        self.entry2.place(relx=0.132, rely=0.413, width=400, height=35)
        self.entry2.configure(font="-family {Poppins} -size 15")
        self.entry2.configure(relief="flat")

        #   self.r2 = root.register(self.testint)
        #   self.r2 = p_add.register(self.testint)
        self.label4 = Label(root)
        self.label4.place(relx=0.100, rely=0.450, width=310, height=50)
        self.label4.configure(text="Product sub cat")
        self.label4.configure(font="-family {Poppins} -size 15")
        self.label4.configure(foreground="#ffffff",background="#000000")
        self.entry3 = Entry(root, textvariable=self.subcategory)
        self.entry3.place(relx=0.132, rely=0.529, width=400, height=35)
        self.entry3.configure(font="-family {Poppins} -size 14")
        self.entry3.configure(relief="flat")
        #     self.entry3.configure(validate="key", validatecommand=(self.r2, "%P"))

      #  self.label5 = Label(root)
     #   self.label5.place(relx=0.100, rely=0.570, width=310, height=50)
     #   self.label5.configure(text="Product Quantity")
    #    self.label5.configure(font="-family {Poppins} -size 12")
   #     self.entry4 = Entry(root)
   #     self.entry4.place(relx=0.132, rely=0.646, width=374, height=30)
   #     self.entry4.configure(font="-family {Poppins} -size 12")
   #     self.entry4.configure(relief="flat")

     #   self.entry6 = Entry(root)
     #   self.entry6.place(relx=0.527, rely=0.413, width=374, height=30)
     #   self.entry6.configure(font="-family {Poppins} -size 12")
     #   self.entry6.configure(relief="flat")

     #   self.entry7 = Entry(root)
     #   self.entry7.place(relx=0.527, rely=0.529, width=374, height=30)
     #   self.entry7.configure(font="-family {Poppins} -size 12")
    #    self.entry7.configure(relief="flat")

   #     self.entry8 = Entry(root)
  #      self.entry8.place(relx=0.527, rely=0.646, width=374, height=30)
 #       self.entry8.configure(font="-family {Poppins} -size 12")
#        self.entry8.configure(relief="flat")

        #  self.entry8.configure(validate="key", validatecommand=(self.r2, "%P"))

        self.button1 = Button(root)
        self.button1.place(relx=0.400, rely=0.700, width=96, height=34)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#CF1E14")
        self.button1.configure(font="-family {Poppins SemiBold} -size 14")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="ADD")
        self.button1.configure(command=self.database)

        self.button2 = Button(root)
        self.button2.place(relx=0.526, rely=0.700, width=86, height=34)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#CF1E14")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#CF1E14")
        self.button2.configure(font="-family {Poppins SemiBold} -size 14")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="Clear")
        self.button2.configure(command=self.clear)


    def clear(self):
        self.name.set(" ")
        self.category.set(" ")
        self.subcategory.set("")

    def database(self):

        #  name1 = self.name.get()
         # category1 = self.category.get()
         # subcategory1 =self.subcategory.get()
          connection = pyodbc.connect('DRIVER={SQL Server};'
                                    'SERVER=DESKTOP-R5569UO\SQLEXPRESS;'
                                    ' DATABASE=MVC; Trusted_Connection=yes;')
          Cursor = connection.cursor()
          Cursor.execute("insert into Product values(?,?,?)",(
              self.name.get(),
              self.category.get(),
              self.subcategory.get()
          ))
               #        (name1, category1, subcategory1))
                         #(name, category, subcategory)
          connection.commit()
          messagebox.showinfo("Success!!", "Products Added Succefully.")
          self.root.destroy()




    # name1 = name.get()
            # category1 = category.get()
            # subcategory1 = subcategory.get()




   #     frame=Frame(self.root,bg="black")
   #     frame.place(x=520,y=100,width=800,height=550)



if __name__ == '__main__':
    root = Tk()
    obj = add(root)
    root.mainloop()