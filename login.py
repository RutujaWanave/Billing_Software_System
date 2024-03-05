
from tkinter import *
from tkinter import messagebox

from project3 import Bill_App
import pyodbc

# ============================================
"""root = Tk()
root.geometry("1366x768")
root.title("Inventory")
root.title("Retail Manager(ADMIN)")
"""
""""""""
class xyz:
  def __init__(self,root):

   self.root = root
   self.root.geometry("1530x800+0+0")
   self.root.title("Billing Software")
   self.root.configure(background="#333333")

   frame =Frame(background="#333333")


   self.label1 = Label(frame)
#  self.label1.place(relx=0, rely=0, width=1366, height=768)
   self.label1.grid(row=0,column=0,columnspan=2,pady=40)
   self.label1.configure(text="Admin Login",background="#333333",foreground="#ff3399")
   self.label1.configure(font = ("Arial", 30))

  #self.img = PhotoImage(file="./images/admin_login.png")
 # self.label1.configure(image=self.img)
   self.label2 = Label(frame)
 #  self.label2.place(relx=0, rely=0, width=1100, height=370)
   self.label2.grid(row=1,column=0)
   self.label2.configure(text="Username",background="#333333",foreground="#ffffff")
   self.label2.configure(font="-family {Poppins SemiBold} -size 16")
 #  self.label2.configure(background="pink")

   self.entry1 = Entry(frame, highlightthickness=4)
#   self.entry1.place(relx=0.373, rely=0.273, width=374, height=30)
   self.entry1.grid(row=1,column=1,pady=20)
   self.entry1.configure(font="-family {Poppins} -size 10")
   self.entry1.configure(relief="flat")
   #self.entry1.configure(highlightbackground="black")
   self.entry1.configure(borderwidth=4)
   self.entry1.configure(font = ("Arial", 16))


#  self.entry1.configure(textvariable=user)
   self.label3 = Label(frame)
#   self.label3.place(relx=0.300, rely=0.300, width=300, height=90)
   self.label3.grid(row=2,column=0)
   self.label3.configure(text="Password",background="#333333",foreground="#ffffff")
   self.label3.configure(font="-family {Poppins SemiBold} -size 16")
#   self.label3.configure(background="pink")

   self.entry2 = Entry(frame,highlightthickness=4)
 #  self.entry2.place(relx=0.373, rely=0.384, width=374, height=30)
   self.entry2.grid(row=2,column=1,pady=20)
   self.entry2.configure(font="-family {Poppins} -size 10")
   self.entry2.configure(relief="flat")
   self.entry2.configure(show="*")
   self.entry2.configure(highlightbackground="black")
   self.entry2.configure(borderwidth=4)
   self.entry2.configure(font=("Arial", 16))
  # self.entry2.configure(background="pink")
  #self.entry2.configure(textvariable=passwd)

   self.button1 = Button(frame)
 #  self.button1.place(relx=0.366, rely=0.685, width=356, height=43)
   self.button1.grid(row=3,column=0,columnspan=2,pady=20)
   self.button1.configure(relief="flat")
   self.button1.configure(overrelief="flat")
   self.button1.configure(activebackground="#D2463E")
   self.button1.configure(cursor="hand2")
   self.button1.configure(foreground="#ffffff")
   self.button1.configure(background="#ff3399")
   self.button1.configure(font="-family {Poppins SemiBold} -size 20")
   self.button1.configure(borderwidth="0")
   self.button1.configure(text="""LOGIN""")
   self.button1.configure(command=self.project3)

   """self.button2 = Button(frame)
   #  self.button1.place(relx=0.366, rely=0.685, width=356, height=43)
   self.button2.grid(row=3, column=3, columnspan=10, pady=20)
   self.button2.configure(relief="flat")
   self.button2.configure(overrelief="flat")
   self.button2.configure(activebackground="#D2463E")
   self.button2.configure(cursor="hand2")
   self.button2.configure(foreground="#ffffff")
   self.button2.configure(background="#ff3399")
   self.button2.configure(font="-family {Poppins SemiBold} -size 20")
   self.button2.configure(borderwidth="0")
   self.button2.configure(text="Clear")"""
  # self.button2.configure(command=self.clear)
   frame.pack()

  # def clear(self):
   #    self.entry1.get("")
    #   self.entry2.get("")



   def login1(self, root):

       connection = pyodbc.connect('DRIVER={SQL Server};'
                                   'SERVER=DESKTOP-R5569UO\SQLEXPRESS;'
                                   ' DATABASE=MVC; Trusted_Connection=yes;')
       Cursor = connection.cursor()
       ss = "select * from login where userId='" + self.entry1.get() + "' and password='" + self.entry2.get() + "'"
       Cursor.execute(ss)
       result = Cursor.fetchall()
       if result:
           messagebox.showinfo("", "login succesfully")
       # mainform()
       else:
           messagebox.showinfo("", "Invalid username and password")



  def project3(self):
       connection = pyodbc.connect('DRIVER={SQL Server};'
                                  'SERVER=DESKTOP-R5569UO\SQLEXPRESS;'
                                  ' DATABASE=MVC; Trusted_Connection=yes;')
       Cursor = connection.cursor()
       ss = "select * from login where userId='" + self.entry1.get() + "' and password='" + self.entry2.get() + "'"
       Cursor.execute(ss)
       result = Cursor.fetchall()


       if result:
           messagebox.showinfo("", "login succesfully")

           self.new_win = Toplevel(self.root)
           self.new_obj = Bill_App(self.new_win)

      #mainform()

       else:
          messagebox.showinfo("", "Invalid username and password")
          connection.commit()







  #     if  self.entry1.get=='' and  self.entry1.get==''  :
        # self.entry1.get=='' self.entry1.get==''
   #      messagebox.showerror("enter userid and password")
   #    self.new_win = Toplevel(self.root)
   #    self.new_obj = Bill_App(self.new_win)

if __name__ == '__main__':
    root = Tk()
    obj = xyz(root)
    root.mainloop()

























"""
r = Tk()
r.geometry("1366x768")
r.title("Retail Manager(ADMIN)")
user = StringVar()
passwd = StringVar()
fname = StringVar()
lname = StringVar()
#with sqlite3.connect("./Database/store.db") as db:
 # cur = db.cursor()
def random_emp_id(stringLength):
 Digits = string.digits
 strr = ''.join(random.choice(Digits) for i in range(stringLength - 3))
 return ('EMP' + strr)
def valid_phone(phn):
 if re.match(r"[789]\d{9}$", phn):
 return True
 return False
def valid_aadhar(aad):
 if aad.isdigit() and len(aad) == 12:
 return True
 return False
#
r.geometry("1366x768")
 top.resizable(0, 0)
 top.title("Retail Manager(ADMIN)")"""
"""
r.label1 = Label()
r.label1.place(relx=0, rely=0, width=1366, height=768)
#label
r.label2=Label()
r.label2.place(relx=0,rely=0, width=1100, height=370)
r.label2.configure(text="Username")
r.label2.configure(font="-family {Poppins SemiBold} -size 15")
#label
r.label3=Label()
r.label3.place(relx=0.300, rely=0.300,width=300, height=90)
r.label3.configure(text="Password")
r.label3.configure(font="-family {Poppins SemiBold} -size 15")
r.entry1 = Entry()
r.entry1.place(relx=0.373, rely=0.273, width=374, height=24)
r.entry1.configure(font="-family {Poppins} -size 10")
r.entry1.configure(relief="flat")
r.entry1.configure(text=user)
r.entry2 = Entry()
r.entry2.place(relx=0.373, rely=0.384, width=374, height=24)
r.entry2.configure(font="-family {Poppins} -size 10")
r.entry2.configure(relief="flat")
r.entry2.configure(show="*")
r.entry2.configure(textvariable=passwd)
r.button1 = Button()
r.button1.place(relx=0.366, rely=0.685, width=356, height=43)
r.button1.configure(relief="flat")
r.button1.configure(overrelief="flat")
r.button1.configure(activebackground="#D2463E")
r.button1.configure(cursor="hand2")
r.button1.configure(foreground="#ffffff")
r.button1.configure(background="#D2463E")
r.button1.configure(font="-family {Poppins SemiBold} -size 20")
r.button1.configure(borderwidth="0")
r.button1.configure(text="login")
#r.button1.configure(command=r.login)
def login(self, Event=None):
  username = self.entry1.get()
  password = self.entry2.get()
 """ """with sqlite3.connect("./Database/store.db") as db:
 cur = db.cursor()
 find_user = "SELECT * FROM employee WHERE emp_id = ? and password = ?"
 cur.execute(find_user, [username, password])
 results = cur.fetchall()
 if results:
 if results[0][6] == "Admin":
 messagebox.showinfo("Login Page", "The login is successful.")
 page1.entry1.delete(0, END)
 page1.entry2.delete(0, END)
 root.withdraw()
 global admin
 global page2
 adm = Toplevel()
 page2 = Admin_Page(adm)
 # page2.time()
 adm.protocol("WM_DELETE_WINDOW", exitt)
 adm.mainloop()
 else:
 messagebox.showerror("Oops!!", "You are not an admin.")
 else:
 messagebox.showerror("Error", "Incorrect username or password.")
 page1.entry2.delete(0, END)
"""
"""
r.mainloop()"""
