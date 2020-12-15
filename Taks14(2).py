#Bismillah
import tkinter as tk
from tkinter import messagebox
import Modules as md
root=tk.Tk()
root.title("KOFE CAFE")
root.configure(bg="dark blue")
top_label=tk.Label(root,text="Hello!! Welcome to KOFE CAFE",font=("Arial Bold",30),bg="black",fg="white").pack()
#Top Frame
top_frame=tk.LabelFrame(root,text="PLACE ORDER",font=("Arial Bold",20),padx=50,pady=10,bd=10)
top_frame.pack(pady=10)
#Bottom Frame
bottom_frame=tk.LabelFrame(root,text="INSERT COINS",font=("Arial Bold",20),bd=10)
bottom_frame.pack(pady=5)
bottom_most=tk.LabelFrame(root)
bottom_most.pack(pady=5)
#===========================================================================================================================================================================================
def clicker() :
    global money
    global quarter_ent
    global dimes_ent
    global nickles_ent
    global pennies_ent
    global  name
    quarter = quarter_ent.get()
    dimes = dimes_ent.get()
    nickles = nickles_ent.get()
    pennies = pennies_ent.get()
    if (quarter.isdigit() and dimes.isdigit() and nickles.isdigit() and pennies.isdigit()) :
        a=md.calcu(quarter,dimes,nickles,pennies,money)
        if a==1:
            val_label = tk.Label(bottom_frame, text=f"Payment Successful\nCollect Your change {md.val:.2f}\nHere is your {name} .Enjoy!",font=("Arial Bold", 10))
            val_label.grid(column=3, row=15)
        elif a==2:
            val_label = tk.Label(bottom_frame, text="Payment successful", font=("Arial Bold", 10))
            val_label.grid(column=3, row=15)
        else:
            val_label = tk.Label(bottom_frame, text=f"Sorry!!! you don't have enough money \n Refunded money {md.cus_money:.2f}",font=("Arial Bold", 10))
            val_label.grid(column=3, row=15)
    else :
        tk.messagebox.showwarning("Wrong data", "Invalid data,Numbers Only")

    def report():
        global water
        global milk
        global coffee
        global coins
        water=tk.Label(bottom_frame,text=f"Water :{md.Tot_water}ml",font=("Arial Bold", 10),bg="black", fg="white")
        water.grid(column=4, row=1)
        milk = tk.Label(bottom_frame, text=f"Milk :{md.Tot_milk}ml", font=("Arial Bold", 10), bg="black", fg="white")
        milk.grid(column=4, row=2)
        coffee = tk.Label(bottom_frame, text=f"Coffee :{md.Tot_coffee}gm", font=("Arial Bold", 10), bg="black", fg="white")
        coffee.grid(column=4, row=3)
        coins = tk.Label(bottom_frame, text=f"Money :${money:.2f}", font=("Arial Bold", 10), bg="black", fg="white")
        coins.grid(column=4, row=4)

    report = tk.Button(bottom_most, text="Report", width=10, font=("Arial Bold", 20), bd=5, command=report, bg="black",
                       fg="white").grid(column=0, row=1)
    def reset():
        try:
            val_label.grid_forget()
            water.grid_forget()
            milk.grid_forget()
            coffee.grid_forget()
            coins.grid_forget()

        except NameError:
            pass

    reset=tk.Button(bottom_frame, text="Reset", width=10, font=("Arial Bold", 15), bd=5, command=reset,bg="black", fg="white").grid(column=4, row=6)


def insert_coins():
    global quarter_ent
    global dimes_ent
    global nickles_ent
    global pennies_ent
    a=tk.StringVar()
    b=tk.StringVar()
    c = tk.StringVar()
    d = tk.StringVar()
    quat_label = tk.Label(bottom_frame, text="QUARTER", font=("Arial Bold", 15), pady=9)
    quat_label.grid(column=2, row=1)
    quarter_ent = tk.Entry(bottom_frame,textvariable="a", width=15)
    quarter_ent.grid(column=3, row=1)
    dimes_label = tk.Label(bottom_frame, text="DIMES", font=("Arial Bold", 15), pady=9)
    dimes_label.grid(column=2, row=2)
    dimes_ent = tk.Entry(bottom_frame,textvariable="b", width=15)
    dimes_ent.grid(column=3, row=2)
    nick_label = tk.Label(bottom_frame, text="NICKLES", font=("Arial Bold", 15), pady=9)
    nick_label.grid(column=2, row=3)
    nickles_ent = tk.Entry(bottom_frame,textvariable="c", width=15)
    nickles_ent.grid(column=3, row=3)
    pen_label = tk.Label(bottom_frame, text="PENNIES", font=("Arial Bold", 15), pady=9)
    pen_label.grid(column=2, row=4)
    pennies_ent = tk.Entry(bottom_frame,textvariable="d", width=15)
    pennies_ent.grid(column=3, row=4)

    def resetvalue():
        quarter_ent.delete(0,'end')
        dimes_ent.delete(0,'end')
        nickles_ent.delete(0,'end')
        pennies_ent.delete(0,'end')
    resetval=tk.Button(bottom_frame, text="Reset Value", width=10, font=("Arial Bold", 15), bd=5, command=resetvalue,bg="black", fg="white").grid(column=2, row=6)

#==========================================================================================================================================================================================
def espfun():
    global money
    global name
    if md.resource_check(100,100,100)==True:
        insert_coins()
        money=3.5
        name="ESPRESSO"
        pro = tk.Button(bottom_frame, text="Proceed", width=10, font=("Arial Bold", 15), bd=5, command=clicker,bg="black", fg="white").grid(column=3, row=6)

def latfun():
    global money
    global name
    if md.resource_check(200, 300, 100) == True :
        insert_coins()
        money = 6.5
        name = "LATTE"
        pro = tk.Button(bottom_frame, text="Proceed", width=10, font=("Arial Bold", 15), bd=5, command=clicker,bg="black", fg="white").grid(column=3, row=6)

def capfun():
    global money
    global name
    if md.resource_check(100, 200, 100) == True :
        insert_coins()
        money = 7.5
        name = "CAPPUCCINO"
        pro = tk.Button(bottom_frame, text="Proceed", width=10, font=("Arial Bold", 15), bd=5, command=clicker, bg="black", fg="white").grid(column=3, row=6)
#===========================================================================================================================================================================================
def order():
    like_label = tk.Label(top_frame, text="What would you like?",font=("Arial Bold",20)).grid(column=3, row=3)
    esp_button=tk.Button(top_frame,text="ESPRESSO",padx=10,pady=5,width=10,font=("Arial Bold",15),bd=5,fg="white",bg="black",command=espfun).grid(column=3,row=4)
    lat_button = tk.Button(top_frame, text="LATTE",padx=10,pady=5,width=10,font=("Arial Bold",15),bd=5,fg="white",bg="black",command=latfun).grid(column=3, row=5)
    capp_button = tk.Button(top_frame, text="CAPPUCCINO",padx=10,pady=5,width=10,font=("Arial Bold",15),fg="white",bg="black",bd=5,command=capfun).grid(column=3, row=6)
    off_button = tk.Button(bottom_most, text="OFF",  font=("Arial Bold", 20), fg="white",bg="black", bd=5, command=root.quit).grid(column=1, row=1)





on_button=tk.Button(top_frame,text="ON",font=("Arial Bold",20),bg="black",fg="white",command=order,bd=5,width=5).grid(column=3,row=0)







root.mainloop()
