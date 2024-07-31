
#

from tkinter import *
import pickle
import os
from tkinter import ttk
import csv
from tkinter.messagebox import askyesno
from filing import *
from PIL import Image, ImageTk
import PIL.Image
from tkinter.messagebox import askyesno, askquestion, showinfo, showerror
from datetime import datetime
from random import randint
from seller_window_class import *

#
         
class Cart:
    
    Customer_cart = []  #Product: [id, name, shop name, price, quantity,total quantity, details]
    Total_price = 0.0
    
    def check_out(self, customer_info=[], bill_no=None):
        
        # ======================    =====================
        
        self.bil_no = bill_no
        self.date_time = datetime.now()
        self.custom_info = customer_info # [first_name, last_name, contact, address, gender, age, usernam, email, password]
        self.sellers_record = Filing.file_read(dir_name="Accounts Info", file_name="Seller Accounts")
        self.sellers_record = self.sellers_record[1:]
        self.sellers_record = list(map(lambda x: x[1:], self.sellers_record)) # [Name, gender, age, dob, shop_name, contact, username, email, password]
        self.sellers_info = []
        
        # ====================      ========================
    
        if len(Cart.Customer_cart) > 0:
            for i in range(len(Cart.Customer_cart)):
                print(Cart.Customer_cart[i])
                print(Cart.Customer_cart[i][3])
                if os.path.isdir("Shopping History"):
                    self.add_record = Filing(f"Shopping History/{self.customer_info[-3]}")
                    self.add_record.general_filing(file_name=f"{self.bill_no}",
                                                   col_list=["Product ID", "Product Name", "Shop Name", "Product Price", "Quantity", "Total Price"],
                                                   data_list=[Cart.Customer_cart[i][0], Cart.Customer_cart[i][1], Cart.Customer_cart[i][2], Cart.Customer_cart[i][3], Cart.Customer_cart[i][4], str(int(Cart.Customer_cart[i][3])*int(Cart.Customer_cart[i][4]))])
                
                else:
                    os.mkdir("Shopping History")
                    self.add_record = Filing(f"Shopping History/{self.customer_info[-3]}")
                    self.add_record.general_filing(file_name=f"{self.bill_no}",
                                                   col_list=["Product ID", "Product Name", "Shop Name", "Product Price", "Quantity", "Total Price"],
                                                   data_list=[Cart.Customer_cart[i][0], Cart.Customer_cart[i][1], Cart.Customer_cart[i][2], Cart.Customer_cart[i][3], Cart.Customer_cart[i][4], str(int(Cart.Customer_cart[i][3])*int(Cart.Customer_cart[i][4]))])
                
                
            for i in range(len(self.sellers_record)):
                
                for j in range(len(Cart.Customer_cart)):
                    
                    if Cart.Customer_cart[j][2] == self.sellers_record[i][4]:

                
                        if os.path.isdir("Sales"):
                            self.add_record = Filing("Sales/f{self.seller_record[i][-4]}")
                            self.add_record.general_filing(file_name=f"{self.date_time.day}/{self.date_time.month}/{self.date_time.year}",
                                                        col_list=["Bill No", "Product ID", "Product Name", "Customer Name", "Customer Contact", "Customer address", "Quantity", "Total Price"],
                                                        data_list=[self.bill_no, Cart.Customer_cart[j][0], Cart.Customer_cart[j][1], self.customer_info[0]+self.customer_info[1], self.customer_info[2], self.customer_info[3], Cart.Customer_cart[i][4], str(int(Cart.Customer_cart[i][3])*int(Cart.Customer_cart[i][4]))])
                        
                        else:
                            os.mkdir("Sales")
                            self.add_record = Filing("Sales/f{self.seller_record[0][-4]}")
                            self.add_record.general_filing(file_name=f"{self.date_time.day}/{self.date_time.month}/{self.date_time.year}",
                                                        col_list=["Bill No", "Product ID", "Product Name", "Customer Name", "Customer Name", "Customer Contact", "Quantity", "Total Price"],
                                                        data_list=[self.bill_no, Cart.Customer_cart[j][0], Cart.Customer_cart[j][1], self.customer_info[0]+self.customer_info[1], self.customer_info[2], self.customer_info[3], Cart.Customer_cart[i][4], str(int(Cart.Customer_cart[i][3])*int(Cart.Customer_cart[i][4]))])
                        
                
    @classmethod
    def change_value(cls):
        cls.Customer_cart = []
        cls.Total_price = 0.0

#

class ShowCart(Cart):
    
    def __init__(self, root=None, title="", max_width=1000, max_height=600, c_width=300, c_height=300, rightframebg="pink", windowbg="white", customer_info=[]):
       
        # ==========================================    =====================================
    
        self.root = root
        self.root.title(title)
        
        self.root.geometry(f"{max_width}x{max_height}+{c_width}+{c_height}")              
        self.root.maxsize(max_width, max_height)
        self.root.minsize(max_width, max_height)
        
        self.root.grab_set()
        self.root.protocol("WM_DELETE_WINDOW", lambda: SellerGui.callback(self.root))
        self.root.config(bg=windowbg)
        
        # ========================================    ====================================
        
        self.customer_info = customer_info # ["First Name","Last Name","Contact No.","Address","Gender","Age","Date of Birth","Username","Email","Password"]
        self.quant_select = StringVar()
        self.bill_no = str(randint(1000000000000,9999999999999))
       
       # =========================================     =====================================
        
        self.head_lab = Label(self.root, text="Cart", font=("Times", 24, "bold", "italic"), bg="lightgrey").pack(fill=X)
        
        # =======================================      =======================================
        
        self.price_desc_frame = Frame(self.root, bg=rightframebg,
                                      bd=1, relief=RIDGE, width=300, padx=5)
        self.price_desc_frame.pack(side=RIGHT, fill=Y)
        
        self.des_frame = Frame(self.price_desc_frame, bg=rightframebg)
        self.des_frame.pack(pady=20)
        
        # ==================================    =============================
        
        self.bill_label = Label(self.des_frame, text="Shipping & Billing",
                                font=("Times", 20, "bold"), bg=rightframebg)
        self.bill_label.grid(row=0, column=0)
        
        self.bil_no_label = Label(self.des_frame, text=f"Bill No. {self.bill_no}",
                                font=("Times", 13), wraplength=310,
                                anchor=W, bg=rightframebg).grid(row=1, column=0, pady=3)
        
        self.address_label = Label(self.des_frame, text=f"Address: {self.customer_info[3]}",
                                   font=("Times", 13), wraplength=310,
                                   anchor=W, bg=rightframebg).grid(row=2, column=0, pady=3)

        # self.call = ImageTk.PhotoImage(PIL.Image.open("images/call_icon.jpg").resize((30, 30), PIL.Image.ANTIALIAS))

        self.contact_label = Label(self.des_frame, text=f"Contact: {self.customer_info[2]}",
                                   font=("Times", 13), anchor=W, bg=rightframebg)
        self.contact_label.grid(row=3, column=0, pady=3)
        self.email_lab = Label(self.des_frame, text=f"Email: {self.customer_info[-1]}",
                               font=("Times", 13), anchor=W, bg=rightframebg)
        self.email_lab.grid(row=4, column=0, pady=3)

        self.details_frame = Frame(self.price_desc_frame,
                                   width=300, padx=5, bg=rightframebg)
        self.l1 = Label(self.details_frame, text="Order Details",
                        font=("Times", 20, "bold"), anchor=W, bg=rightframebg)
        self.l1.grid(row=0, column=0, pady=20)

        self.items_total = Label(self.details_frame, text=f"Total Items: ",
                                 font=("Times", 13), anchor=W, bg=rightframebg)
        self.items_total.grid(row=1, column=0, pady=3, columnspan=2)

        # --------------------------     -----------------------------
        
        self.total_price = 0.0
        for i in Cart.Customer_cart:
            
            self.total_price += (int(i[-3])*int(i[-4]))
        
        # ------------------------    --------------------------------

        self.price_lab = Label(self.details_frame, text=f"Total Price: Rs.{self.total_price}",
                               font=("Times", 13), anchor=W, bg=rightframebg)
        self.price_lab.grid(row=2, column=0, pady=3, columnspan=2)

        self.fee_lab = Label(self.details_frame, text=f"Shipping Fee Rs.99.0",
                               font=("Times", 13), anchor=W, bg=rightframebg)
        self.fee_lab.grid(row=3, column=0, pady=3, columnspan=2)

        self.place_order_button = Button(self.details_frame, text=f"Place Order", font=("Comic Sans MS", 16),
                                         bg="green", fg="white", command=self.check_out)
        self.place_order_button.grid(row=4, column=0, pady=20, columnspan=5)

        self.details_frame.pack()
        
        # ================================    =======================================
        
        self.cart_products_frame = Frame(self.root, bg=windowbg)       
        self.cart_products_frame.pack(anchor=NW, fill=BOTH, expand=True)
        self.products_pic = []
        self.prod_show()
        
    # ================================   ===================================    
        
    def prod_show(self):
        
        # ==============================     =====================================
        
        # inside product frame
        self.canvas_prod_show = Canvas(self.cart_products_frame, bg="khaki")
        self.canvas_prod_show.pack(side=LEFT, fill=BOTH, expand=1, padx=10, pady=20)
        
        self.scroll_bar = ttk.Scrollbar(self.cart_products_frame, orient="vertical", command=self.canvas_prod_show.yview)
        self.scroll_bar.pack(side=RIGHT, fill=Y)
        
        self.canvas_prod_show.config(yscrollcommand=self.scroll_bar.set)
        self.canvas_prod_show.bind("<Configure>", lambda e: self.canvas_prod_show.configure(scrollregion=self.canvas_prod_show.bbox("all")))
        
        self.in_product_frame = Frame(self.canvas_prod_show, bg="khaki")
        self.canvas_prod_show.create_window((0,0), window=self.in_product_frame, anchor=NW)
       
       # ====================================   ============================
        
        self.products_pic = []
        if len(Cart.Customer_cart)>0:
            for i in range(len(Cart.Customer_cart)):
                self.product_pic = ""
                if os.path.isdir("Product Pics"):
                    if os.path.exists(f"Product Pics/{Cart.Customer_cart[i][0]}.pkl"):
                        self.product_pic = Filing.pic_file_read(dir_name="Product Pics",
                                                                file_name=Cart.Customer_cart[i][0])


                        if self.product_pic.startswith("C:/Users/Imran Hussain/PycharmProjects/main/CEP"):
                            self.product_pic = os.getcwd() + self.product_pic[47:]

                        self.product_pic = PIL.Image.open(self.product_pic)
                        self.product_pic = self.product_pic.resize((120, 120), PIL.Image.ANTIALIAS)
                        self.product_pic = ImageTk.PhotoImage(self.product_pic)

                if self.product_pic == "":
                    self.product_pic = "images/addpic.png"
                    self.product_pic = ImageTk.PhotoImage(PIL.Image.open(self.product_pic).resize((120, 120), PIL.Image.ANTIALIAS))

                self.products_pic.append(self.product_pic)

                self.prod_button = Button(self.in_product_frame, image=self.products_pic[i], text=f"Product: {Cart.Customer_cart[i][1]}\nShop: {Cart.Customer_cart[i][2]}\nQuantity: {Cart.Customer_cart[i][4]}\t\t\t\t\t\nPrice: Rs.{int(Cart.Customer_cart[i][3])*int(Cart.Customer_cart[i][4])}", font=("Times", 15), compound=RIGHT, justify=LEFT, padx=2, pady=3, width=560, wraplength=500)
                self.prod_button.pack(padx=15, pady=5, fill=X, expand=True, ipadx=30)
                self.prod_button.bind("<Button-1>", self.prod_details)
        
        
    def prod_details(self, event):
        
        self.prod_info_text = event.widget.cget("text")
        self.prod_info_text = self.prod_info_text.strip().split("\n")
        self.cart_products_frame.destroy()   
        self.price_desc_frame.destroy()
        self.prod_info = []
        for i in self.prod_info_text:
            self.prod_string = ""
            
            if "Product:" in i:
                i = i[9:]
            elif "Shop:" in i:
                i = i[6:]
            elif "Quantity:" in i:
                i = i[10:]
            elif "Price: Rs." in i:
                i = i[10:]
            for j in i:
                if j != "\t":
                     self.prod_string += j
            self.prod_info.append(self.prod_string)
        
        for data in Cart.Customer_cart:
            if data[1] == self.prod_info[0] and data[2] == self.prod_info[1] and data[4] == self.prod_info[2]:
                self.prod_info = data  #["9878789789", "Shop & Careuhuhkjooiejighoujiogherjij", "Hello world", "1000", "300"]
                print(data)
        
        self.quant_select = StringVar()
        self.quant_select.set(f"{self.prod_info[-3]}")
        
        # ====================================    ===========================================
        
        self.prod_pic = ""
        if os.path.isdir("Product Pics"):
            if os.path.exists(f"Product Pics/{self.prod_info[0]}.pkl"):
                self.prod_pic = Filing.pic_file_read(dir_name="Product Pics",
                                                        file_name=self.prod_info[0])


                if self.prod_pic.startswith("C:/Users/Imran Hussain/PycharmProjects/main/CEP"):
                    self.prod_pic = os.getcwd() + self.prod_pic[47:]

                self.prod_pic = PIL.Image.open(self.prod_pic)
                self.prod_pic = self.prod_pic.resize((270, 230), PIL.Image.ANTIALIAS)
                self.prod_pic = ImageTk.PhotoImage(self.prod_pic)

        if self.prod_pic == "":
            self.prod_pic = "images/addpic.png"
            self.prod_pic = ImageTk.PhotoImage(PIL.Image.open(self.prod_pic).resize((270, 230), PIL.Image.ANTIALIAS))

        
        
        # ===========================================     =================================

        self.pic_prod_frame = Frame(self.root, bg="white", pady=3)
        self.pic_prod_frame.pack(pady=17, padx=10, anchor=NW, fill=X)

        # -----------------------------    -------------------------------

        self.pic_canvas = Canvas(self.pic_prod_frame, width=270, height=230, bg="white")
        self.pic_canvas.pack(side=LEFT, anchor=NW, padx=7)
        self.pic_canvas.create_image(0, 0, image=self.prod_pic, anchor=NW)

        # ------------------------------    ---------------------------------------

        self.pic_des_frame = Frame(self.pic_prod_frame, pady=5, padx=5, width=50, height=50, bg="white")

        self.prod_name_label = Label(self.pic_des_frame, text=f"{self.prod_info[1]}", font="Times 17",
                                     wraplength=620, anchor=NW, justify=LEFT, bg="white").pack(anchor=W)
        self.prod_price_lab = Label(self.pic_des_frame, text=f"Rs.{self.prod_info[3]}", font="Times 17 bold",
                                    fg="dark orange", bg="white").pack(pady=15, anchor=W)

        ####################################    #########################################

        self.quant_frame = Frame(self.pic_des_frame, pady=3, bg="white")
        self.quant_label = Label(self.quant_frame, text="Quantity:", font="Times 16", bg="white").grid(row=0, column=0)
        self.quant_selection = Spinbox(self.quant_frame, from_=1, to=int(self.prod_info[-2]), font="Times 12",
                                    textvar=self.quant_select, state="readonly", readonlybackground="white",
                                    selectbackground="white", selectforeground="black").grid(row=0, column=1, padx=50)
        self.quant_frame.pack(anchor=W, fill=X)

        self.pic_des_frame.pack(fill=X, anchor=NW, padx=7)

        # ----------------------------------    ---------------------------------------
        self.buttons_frame = Frame(self.pic_des_frame, bg="white")
        self.buttons_frame.pack(pady=32)
        self.upd_cart_button = Button(self.buttons_frame, text="Update Cart", font="Times 15", width=15, relief=FLAT,
                                      bg="DarkOrange1", command=self.update_cart).grid(row=0, column=0, padx=10)
        self.remove_prod_button = Button(self.buttons_frame, text="Remove Product", font=("Times 15"), width=15, relief=FLAT, bg="DarkOrange1", command=self.remove_prod).grid(row=0, column=1, padx=10)
        
        # ======================================    =======================================

        self.prod_des_frame = Frame(self.root, pady=3, padx=5, bg="white")

        self.prod_head_lab = Label(self.prod_des_frame, text=f"Product Details of {self.prod_info[1]}",
                                   font="Times 15 bold", anchor=NW, justify=LEFT, bg="white").pack(fill=X, pady=5,
                                                                                                    anchor=NW)
        self.prod_desc = Label(self.prod_des_frame, text=f"{self.prod_info[-1]}", font="Times 13", anchor=NW,
                               justify=LEFT, wraplength=720, bg="white").pack(pady=5, anchor=W, fill=X)

        self.prod_des_frame.pack(pady=20, fill=BOTH, padx=10, anchor=NW, side=LEFT)
    
    # =====================================    =======================
    
    def update_cart(self):
        
        for i in range(len(Cart.Customer_cart)):
            if Cart.Customer_cart[i][0] == self.prod_info[0]:
                Cart.Customer_cart[i] = [self.prod_info[0], self.prod_info[1], self.prod_info[2], self.prod_info[-4], self.quant_select.get(), self.prod_info[-2], self.prod_info[-1]]      
    
    # ===========================================      ========================
    
    def remove_prod(self):
        
        # self.ask_remove = askyesno 
        self.prod_rem = []
        for i in range(len(Cart.Customer_cart)):
            if Cart.Customer_cart[i][0] == self.prod_info[0]:
                self.prod_rem = Cart.Customer_cart[i] 
        Cart.Customer_cart.remove(self.prod_rem)
        self.back_button()
    
    def back_button(self, windowbg="white", rightframebg="pink"):
        
        self.pic_prod_frame.destroy()
        self.prod_des_frame.destroy()
        
        
        # =======================================      =======================================
        
        self.price_desc_frame = Frame(self.root, bg=rightframebg,
                                      bd=1, relief=RIDGE, width=300, padx=5)
        self.price_desc_frame.pack(side=RIGHT, fill=Y)
        
        self.des_frame = Frame(self.price_desc_frame, bg=rightframebg)
        self.des_frame.pack(pady=20)
        
        self.bill_label = Label(self.des_frame, text="Shipping & Billing",
                                font=("Times", 20, "bold"), bg=rightframebg)
        self.bill_label.grid(row=0, column=0)
        
        self.bil_no_label = Label(self.des_frame, text=f"Bill No. {self.bill_no}",
                                font=("Times", 13), wraplength=310,
                                anchor=W, bg=rightframebg).grid(row=1, column=0, pady=3)
        
        self.address_label = Label(self.des_frame, text=f"Address: {self.customer_info[3]}",
                                   font=("Times", 13), wraplength=300,
                                   anchor=W, bg=rightframebg).grid(row=2, column=0, pady=3)

        # self.call = ImageTk.PhotoImage(PIL.Image.open("images/call_icon.jpg").resize((30, 30), PIL.Image.ANTIALIAS))

        self.contact_label = Label(self.des_frame, text=f"Contact: {self.customer_info[2]}",
                                   font=("Times", 13), anchor=W, bg=rightframebg)
        self.contact_label.grid(row=3, column=0, pady=3)
        self.email_lab = Label(self.des_frame, text=f"Email: {self.customer_info[-1]}",
                               font=("Times", 13), anchor=W, bg=rightframebg)
        self.email_lab.grid(row=4, column=0, pady=3)

        self.details_frame = Frame(self.price_desc_frame,
                                   width=300, padx=5, bg=rightframebg)
        self.l1 = Label(self.details_frame, text="Order Details",
                        font=("Times", 20, "bold"), anchor=W, bg=rightframebg)
        self.l1.grid(row=0, column=0, pady=20)

        self.items_total = Label(self.details_frame, text=f"Total Items: ",
                                 font=("Times", 13), anchor=W, bg=rightframebg)
        self.items_total.grid(row=1, column=0, pady=3, columnspan=2)

        # --------------------------     -----------------------------
        
        self.total_price = 0.0
        for i in Cart.Customer_cart:
            
            self.total_price += (int(i[-3])*int(i[-4]))
        
        # ------------------------    --------------------------------

        self.price_lab = Label(self.details_frame, text=f"Total Price: Rs.{self.total_price}",
                               font=("Times", 13), anchor=W, bg=rightframebg)
        self.price_lab.grid(row=2, column=0, pady=3, columnspan=2)

        self.fee_lab = Label(self.details_frame, text=f"Shipping Fee Rs.99.0",
                               font=("Times", 13), anchor=W, bg=rightframebg)
        self.fee_lab.grid(row=3, column=0, pady=3, columnspan=2)

        self.place_order_button = Button(self.details_frame, text=f"Place Order", font=("Comic Sans MS", 16),
                                         bg="green", fg="white", command=self.check_out)
        self.place_order_button.grid(row=4, column=0, pady=20, columnspan=5)

        self.details_frame.pack()
        
        # ================================    =======================================
        
        self.cart_products_frame = Frame(self.root, bg=windowbg)       
        self.cart_products_frame.pack(anchor=NW, fill=BOTH, expand=True)
        self.products_pic = []
        self.prod_show()
        
    # =========================      ==============================

    def checking_out(self):
        
        print(self.bill_no)
        print(self.customer_info)
        super().check_out(customer_info=self.customer_info, bill_no=self.bill_no)  



if __name__ == '__main__':

    root = Tk()
    Gui = ShowCart(root, customer_info=["Hamza", "Malik", "hamzamalik", "hamzamalik@gmail.com","hello"])
    root.mainloop()
    