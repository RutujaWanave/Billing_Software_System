from tkinter import *
from tkinter import ttk
import random, os
from tkinter import messagebox
import tempfile
from time import strftime
import re

from PIL import ImageTk

from Product import Inventory
import pyodbc

connection = pyodbc.connect('DRIVER={SQL Server};'
'SERVER=DESKTOP-R5569UO\SQLEXPRESS;'
                            ' DATABASE=MVC; Trusted_Connection=yes;')

Cursor = connection.cursor()

class Bill_App:
    def __init__(self, root):

        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")




        # =======================Variable=============================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        z = random.randint(1000, 9999)
        self.bill_no.set(z)
        self.c_email = StringVar()
        self.search_bill = StringVar()
        self.product = StringVar()
        # self.sub_categoris=StringVar()
        self.prices = IntVar()
        self.sub_total = StringVar()
        self.tax_input = StringVar()
        self.total = StringVar()
        self.qty = IntVar()


        lbl_title = Label(self.root, text="Billing Software using Python", font=("times new roman", 35, "bold"),
                          bg="white", fg="red")
        lbl_title.place(x=0, y=130, width=1530, height=50)  # label Size



        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(lbl_title, font=('times new roman', 16, 'bold'), background='white', foreground='blue')
        lbl.place(x=0, y=0, width=120, height=45)
        time()

        Main_Frame = Frame(self.root, bd=5, relief=GROOVE, bg='white')
        Main_Frame.place(x=0, y=175, width=1530, height=620)
#Admin Button



        # Customer Label Frame

        Cust_Frame = LabelFrame(Main_Frame, text="Customer", font=("arial", 12, "bold"), bg="white", fg="red")
        Cust_Frame.place(x=10, y=5, width=330, height=140)

        self.lbl_mob = Label(Cust_Frame, text='Mobile No.', font=("arial", 12, "bold"), bg="white")
        self.lbl_mob.grid(row=0, column=0, padx=5, pady=2)

        self.entry_mob = ttk.Entry(Cust_Frame, textvariable=self.c_phone, font=("arial", 10, "bold"), width=24)
        self.entry_mob.grid(row=0, column=1)

        self.lblCustName = Label(Cust_Frame, text='Customer Name', font=("arial", 12, "bold"), bg="white", bd=4)
        self.lblCustName.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.txtCustName = ttk.Entry(Cust_Frame, textvariable=self.c_name, font=("arial", 10, "bold"), width=24)
        self.txtCustName.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.lblEmail = Label(Cust_Frame, text='Email', font=("arial", 12, "bold"), bg="white", bd=4)
        self.lblEmail.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txtEmail = ttk.Entry(Cust_Frame, textvariable=self.c_email, font=("arial", 10, "bold"), width=24)
        self.txtEmail.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        # Product Label Frame

        Product_Frame = LabelFrame(Main_Frame, text="Product", font=("arial", 12, "bold"), bg="white", fg="red")
        Product_Frame.place(x=370, y=5, width=630, height=140)

        # Category
        self.lblCategory = Label(Product_Frame, text='Select Categories', font=("arial", 12, "bold"), bg="white", bd=4)
        self.lblCategory.grid(row=0, column=0, sticky=W, padx=5, pady=2)
        text_font = ("Poppins", "8")
        self.Combo_Category = ttk.Combobox(Product_Frame,font=("arial", 10, "bold"),width=24)
        self.Combo_Category.place(relx=0.250, rely=0.100, width=190, height=19)
        #self.Combo_Category.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        find_category = "select category from Product"
        Cursor.execute(find_category)
        result1 = Cursor.fetchall()
        cat = []
        for i in range(len(result1)):
            if (result1[i][0] not in cat):
                cat.append(result1[i][0])
                self.Combo_Category.configure(values=cat)
                self.Combo_Category.configure(state="readonly")
                self.Combo_Category.configure(font="-family {Poppins} -size 8")
                self.Combo_Category.option_add("*TCombobox*Listbox.font",text_font)
                self.Combo_Category.option_add("*TCombobox*Listbox.selectBackground", "#D2463E")
                self.Combo_Category.bind("<<ComboboxSelected>>",  self.Categories)

     #   self.Combo_Category = ttk.Combobox(Product_Frame, value=self.category, font=("arial", 10, "bold"), width=24,
                                           #state="readonly")
     #   self.Combo_Category.current(0)
       # self.Combo_Category.grid(row=0, column=1, sticky=W, padx=5, pady=2)
       # self.Combo_Category.bind("<<ComboboxSelected>>", self.Categories)

        # SubCategory
        self.lblSubCategory = Label(Product_Frame, text='SubCategories', font=("arial", 12, "bold"), bg="white", bd=4)
        self.lblSubCategory.grid(row=1, column=0, sticky=W, padx=5, pady=2)
        self.Combo_SubCategory = ttk.Combobox(Product_Frame,font=("arial", 10, "bold"), width=24)
        self.Combo_SubCategory.place(relx=0.250, rely=0.350, width=190, height=20)
        self.Combo_SubCategory.bind("<<ComboboxSelected>>", self.add_product)


        #self.Combo_SubCategory = ttk.Combobox(Product_Frame, value=[""], font=("arial", 10, "bold"), width=24,
                   #                           state="readonly")
        #self.Combo_SubCategory.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        #self.Combo_SubCategory.bind("<<ComboboxSelected>>", self.sub_categoris)

        # Product Name
        self.lblProduct = Label(Product_Frame, text='Product', font=("arial", 12, "bold"), bg="white", bd=4)
        self.lblProduct.grid(row=2, column=0, sticky=W, padx=5, pady=2)
        self.ComboProduct = ttk.Combobox(Product_Frame,textvariable=self.product, font=("arial", 10, "bold"), width=24,) #textvariable=self.product,
        self.ComboProduct.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>", self.add_product)
        # self.ComboProduct.bind("<<ComboboxSelected>>",self.pro_prices)
        # textvariable=self.product,

        # Price

        self.lblprice = Label(Product_Frame, text='Price', font=("arial", 12, "bold"), bg="white", bd=4)
        self.lblprice.grid(row=0, column=2, sticky=W, padx=5, pady=2)

        self.txtprice = ttk.Entry(Product_Frame, textvariable=self.prices, font=("arial", 10, "bold"), width=26)
        self.txtprice.grid(row=0, column=3, sticky=W, padx=5, pady=2)
        #
        # self.lblPrice = Label(Product_Frame, text='Price', font=("arial", 12, "bold"), bg="white", bd=4)
        # self.lblPrice.grid(row=0, column=2, sticky=W, padx=5, pady=2)

        # self.ComboPrice = ttk.Combobox(Product_Frame,font=("arial", 10, "bold"), width=24, state="readonly")
        # self.ComboPrice.grid(row=0, column=3, sticky=W, padx=5, pady=2)

        # Qty

        self.lblQty = Label(Product_Frame, text='Quntity', font=("arial", 12, "bold"), bg="white", bd=4)
        self.lblQty.grid(row=1, column=2, sticky=W, padx=5, pady=2)

        self.ComboQty = ttk.Entry(Product_Frame, textvariable=self.qty, font=("arial", 10, "bold"), width=26)
        self.ComboQty.grid(row=1, column=3, sticky=W, padx=5, pady=2)

        # Middle Frame
        MiddleFrame = Frame(Main_Frame, bd=10)
        MiddleFrame.place(x=10, y=150, width=980, height=340)

        # Image

        # Search
        Search_Frame = Frame(Main_Frame, bd=2, bg='white')
        Search_Frame.place(x=1020, y=15, width=500, height=40)

        self.lblBill = Label(Search_Frame, text='Bill Number', font=("arial", 12, "bold"), bg="red", fg='white')
        self.lblBill.grid(row=0, column=0, sticky=W, padx=1)

        self.txt_Entry_Search = ttk.Entry(Search_Frame, textvariable=self.search_bill, font=("arial", 10, "bold"),
                                          width=24)
        self.txt_Entry_Search.grid(row=0, column=1, sticky=W, padx=5)

        self.BtnSearch = Button(Search_Frame, command=self.find_bill, text="Search", font=("arial", 10, "bold"),
                                bg='orangered', fg='white', width=13, cursor='hand2')
        self.BtnSearch.grid(row=0, column=2)

        # RightFrame Bill Area

        RightLabelFrame = LabelFrame(Main_Frame, text="Bill Area", font=("arial", 12, "bold"), bg="pink", fg="red")
        RightLabelFrame.place(x=1000, y=50, width=480, height=440)

        Scroll_y = Scrollbar(RightLabelFrame, orient=VERTICAL)
        self.textarea = Text(RightLabelFrame, yscrollcommand=Scroll_y.set, bg='pink', fg='blue',
                             font=("times new roman", 12, "bold"))
        Scroll_y.pack(side=RIGHT, fill=Y)
        Scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # Bill Counter Frame

        Bottom_Frame = LabelFrame(Main_Frame, text="Bill Counter", font=("arial", 12, "bold"), bg="white", fg="red")
        Bottom_Frame.place(x=0, y=485, width=1520, height=150)

        # Sub Total
        self.lblSubTotal = Label(Bottom_Frame, text='Sub Total', font=("arial", 12, "bold"), bg="white", bd=4)
        self.lblSubTotal.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.EntySubTotal = ttk.Entry(Bottom_Frame,textvariable=self.sub_total, font=("arial", 10, "bold"), width=24, state="readonly")
        self.EntySubTotal.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        # Tax

        self.lbl_tax = Label(Bottom_Frame, text='Gov Tax', font=("arial", 12, "bold"), bg='white', bd=4)
        self.lbl_tax.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.txt_tax = ttk.Entry(Bottom_Frame,textvariable=self.tax_input, font=("arial", 10, "bold"), width=24, state="readonly")
        self.txt_tax.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        # Total Amount
        self.lblAmountTotal = Label(Bottom_Frame,text='Total', font=("arial", 12, "bold"), bg="white", bd=4)
        self.lblAmountTotal.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.lblAmountTotal = ttk.Entry(Bottom_Frame, textvariable=self.total, font=("arial", 10, "bold"), width=24, state="readonly")
        self.lblAmountTotal.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        # Button Frame
        Btn_Frame = Frame(Bottom_Frame, bd=2, bg='white')
        Btn_Frame.place(x=320, y=0)

        self.BtnAddToCart = Button(Btn_Frame, command=self.AddItem, text="Add To Cart", font=("arial", 15, "bold"),
                                   bg='orangered', fg='white', width=13, cursor='hand2')
        self.BtnAddToCart.grid(row=0, column=0)

        self.Btn_Generate_Bill = Button(Btn_Frame, command=self.gen_bill, text="Generate Bill",
                                        font=("arial", 15, "bold"), bg='orangered', fg='white', width=13,
                                        cursor='hand2')
        self.Btn_Generate_Bill.grid(row=0, column=1)

        self.Btn_Save = Button(Btn_Frame, command=self.save_bill, text="Save Bill", font=("arial", 15, "bold"),
                               bg='orangered', fg='white', width=13, cursor='hand2')
        self.Btn_Save.grid(row=0, column=2)

        self.Btn_Print = Button(Btn_Frame, command=self.print_bill, text="Print", font=("arial", 15, "bold"),
                                bg='orangered', fg='white', width=13, cursor='hand2')
        self.Btn_Print.grid(row=0, column=3)

        self.Btn_Clear = Button(Btn_Frame, command=self.clear, text="Clear", font=("arial", 15, "bold"), bg='orangered',
                                fg='white', width=13, cursor='hand2')
        self.Btn_Clear.grid(row=0, column=4)

        self.Btn_Exit = Button(Btn_Frame, command=self.root.destroy, text="Exit", font=("arial", 15, "bold"),
                               bg='orangered', fg='white', width=13, cursor='hand2')
        self.Btn_Exit.grid(row=0, column=5)

        self.button1 = Button(self.root, text="Admin", command=self.Product, font=("times new roman", 20, "bold"), bg="red",
                              fg="white",
                              cursor='hand2')
        self.button1.place(x=1400, y=100, width=100, height=25)



        self.welcome()
        self.l = []

    # ********************************************************************************

    def AddItem(self):
        Tax = 1
        self.n = self.prices.get()
        self.m = self.qty.get() * self.n
        self.l.append(self.m)
      #  if self.product.get() == "":
      #      messagebox.showerror("Error", "Please Select the Product")
       # else:
        self.textarea.insert(END, f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
        self.sub_total.set(str('RS.%.2f'%(sum(self.l))))
        self.tax_input.set(str('RS.%.2f'%((((sum(self.l)) - (self.prices.get())) * Tax) / 100)))
        self.total.set(str('RS.%.2f'%(((sum(self.l)) + ((((sum(self.l))) - (self.prices.get())) * Tax) / 100))))

    def gen_bill(self):
      if self.product.get() == "":
         messagebox.showerror("Error", "Please Add To cart Product ")
      else:
            text = self.textarea.get(10.0, (10.0 + float(len(self.l))))
            self.welcome()
            self.textarea.insert(END, text)
            self.textarea.insert(END, f"\n{self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.textarea.insert(END, "\n _______________________________________")
            self.textarea.insert(END, f"\n Sub Amount:\t\t\t{self.sub_total.get()} ")
            self.textarea.insert(END, f"\n Tax Amount :\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END, f"\n Total :\t\t\t{self.total.get()}")
            self.textarea.insert(END, "\n-----------------------------------------")

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the Bill")
        if op > 0:
            self.bill_data = self.textarea.get(1.0, END)
            f1 = open(r'D:\17356\bills/' + str(self.bill_no.get()) + '.txt','w')
            f1.write(self.bill_data)
            op = messagebox.showinfo("Saved", f"Bill No:{self.bill_no.get()} Saved Sucessfully")
            f1.close()

    def print_bill(self):
        q = self.textarea.get(1.0, "end-1c")
        filename = tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename, "print")

    def find_bill(self):
        found = "no"
        for i in os.listdir(r'D:\17356\bills'):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f'bills/{i}', 'r')
                self.textarea.delete(1.0, END)
                for d in f1:
                    self.textarea.insert(END, d)
                f1.close()
                found = "yes"
        if found == 'no':
            messagebox.showerror("Error", "Invalid Bill Number")

    def clear(self):
        self.textarea.delete(1.0, END)
        self.c_name.set("")
        self.c_phone.set("")
        self.c_email.set("")
        z = random.randint(1000, 9999)
        self.bill_no.set(str(z))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l = [0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.welcome()
        self.Combo_SubCategory.configure(state="normal")
        self.Combo_SubCategory.delete(0, END)
        self.Combo_Category.configure(state="normal")
        self.Combo_Category.delete(0, END)

    def welcome(self):
        self.textarea.delete(1.0, END)
        self.textarea.insert(END, "\t\t Welcome Lifestyle")
        self.textarea.insert(END, "\n\t\t\t Contact Number:9308561288")
        self.textarea.insert(END, "\n\t\t\tAddress: TC College Road Baramati")
        self.textarea.insert(END, "\n-------------------------------------------")
        self.textarea.insert(END, f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END, f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END, f"\n Phone Number:{self.c_phone.get()}")
        # self.textarea.insert(END, f"\n Customer Email:{self.c_email.get()}")

        self.textarea.insert(END, "\n-------------------------------------------")
        self.textarea.insert(END, f"\nProduct\t\t\tQTY\t\t\tPrice")
        self.textarea.insert(END, "\n--------------------------------------------\n")

    # ****************************************************************
    def Categories(self, event=""):
        self.Combo_SubCategory.configure(state="readonly")
        self.Combo_SubCategory.set('')
        self.ComboProduct.set('')
        find_subcat = "select name from Product where category=?"
        Cursor.execute(find_subcat, [self.Combo_Category.get()])
        result2 = Cursor.fetchall()
        subcat = []
        for j in range(len(result2)):
            if (result2[j][0] not in subcat):
                subcat.append(result2[j][0])
                self.Combo_SubCategory.configure(values=subcat)
              #  self.Combo_SubCategory.bind("<<ComboboxSelected>>", self.get_subcat)
    # **************************************************************
    def add_product(self, event=""):
        self.ComboProduct.configure(state="readonly")
        #self.ComboProduct.set('')
        find_product = "select subcategory from Product where category = ? and name = ?"

        Cursor.execute(find_product, [self.Combo_Category.get(), self.Combo_SubCategory.get()])
        result3 = Cursor.fetchall()
        pro = []
        for k in range(len(result3)):
            pro.append(result3[k][0])
        self.ComboProduct.configure(values=pro)

    def Product(self):

        self.new_win = Toplevel(self.root)
        self.new_obj =Inventory(self.new_win)

    def sub_categoris(self, event=""):

        # Cloth
        if self.Combo_SubCategory.get() == "Pant":
            self.ComboProduct.config(value=self.pant)
            self.ComboProduct.current(0)

        if self.Combo_SubCategory.get() == "T_shirt":
            self.ComboProduct.config(value=self.T_shirt)
            self.ComboProduct.current(0)

        if self.Combo_SubCategory.get() == "Shirt":
            self.ComboProduct.config(value=self.Shirt)
            self.ComboProduct.current(0)

        # Mobiles
        if self.Combo_SubCategory.get() == "Iphone":
            self.ComboProduct.config(value=self.Iphone)
            self.ComboProduct.current(0)

        if self.Combo_SubCategory.get() == "Xiome":
            self.ComboProduct.config(value=self.Xiome)
            self.ComboProduct.current(0)

        if self.Combo_SubCategory.get() == "RealMe":
            self.ComboProduct.config(value=self.RealMe)
            self.ComboProduct.current(0)

        if self.Combo_SubCategory.get() == "One+":
            self.ComboProduct.config(value=self.One)
            self.ComboProduct.current(0)

        # Lifestyle
        if self.Combo_SubCategory.get() == "Bath_Soap":
            self.ComboProduct.config(value=self.Bath_Soap)
            self.ComboProduct.current(0)

        if self.Combo_SubCategory.get() == "Face_Creame":
            self.ComboProduct.config(value=self.Face_Creame)
            self.ComboProduct.current(0)

        if self.Combo_SubCategory.get() == "Hair_Oil":
            self.ComboProduct.config(value=self.Hair_Oil)
            self.ComboProduct.current(0)








if __name__ == '__main__':
    root = Tk()
    obj = Bill_App(root)
    root.mainloop()