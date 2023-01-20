import mysql.connector
database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='saketh@123',
    port='3306',
    database='online_food_order'
)
cursor1 = database.cursor()

def func():
    print("________Online Food Order Databse Management provides the following options:__________ ")
    print("""
            (1) VIEW CUSTOMER DETAILS
            (2) UPDATE CUSTOMER DETAILS
            (3) VIEW ORDERS DETAILS
            (4) UPDATE ORDERS DETAILS
            (5) VIEW FOOD DETAILS
            (6) UPDATE FOOD DETAILS
            (7) VIEW CATEGORY DETAILS 
            (8) UPDATE CATEGORY DETAILS
            (9) VIEW PAYMENT DETAILS
            (10)UPDATE PAYMENT DETAILS
            (0) EXIT
                    """)
    print("  ..............  Select one from the above options  ..............  ")
    option = input("Enter Your Choice No.: ")
    if option == "1":
        view_customerdetails()
    elif option == "2":
        update_customerdetails()
    elif option == "3":
        view_orderdetails()
    elif option == "4":
        update_orderdetails()
    elif option == "5":
        view_fooddetails()
    elif option == "6":
        update_fooddetails()
    elif option == "7":
        view_categorydetails()
    elif option == "8":
        update_categorydetails()
    elif option == "9":
        view_paymentdetails()
    elif option == "10":
        update_paymentdetails()
    elif option == "0":
        endprogram()
    else:
        print("Try Again! Please, chose from the given options ")


def view_customerdetails():
    cursor1.execute("select * from customer")
    users = cursor1.fetchall()
    for user in users:
        print(user)
    return


def view_orderdetails():
    cursor1.execute("select * from orders")
    users=cursor1.fetchall()
    for user in users:
        print(user)
    return


def view_fooddetails():
    cursor1.execute("select * from food")
    users=cursor1.fetchall()
    for user in users:
        print(user)
    return


def view_categorydetails():
    cursor1.execute("select * from category")
    users=cursor1.fetchall()
    for user in users:
        print(user)
    return


def view_paymentdetails():
    cursor1.execute("select * from payment")
    users=cursor1.fetchall()
    for user in users:
        print(user)
    return



#code for updating customer details

def update_customerdetails():
    print('''
        (1)ADD DETAILS
        (2)DELETE DETAILS
        (3)EXIT
        ''')
    option=input('enter valid option for updating:')
    if option=='1':
        add_customerdetails()
    elif option=='2':
        del_customerdetails()
    elif option=="3":
        func()
    else:
        print("consider the given options")

def add_customerdetails():
    customer_id=input("enter customer_id: ")
    name=input("enter name:")
    ph_no=input("enter ph_no: ")
    email =input("enter email :")
    t=(customer_id,name,ph_no,email)
    add='insert into customer values(%s,%s,%s,%s);'
    cursor1.execute(add,t)
    database.commit()
    view_customerdetails()
def del_customerdetails():
    Del_id=int(input("Enter the customer_id: "))
    delete="Delete from customer where customer_id={}".format(Del_id)
    cursor1.execute(delete)
    database.commit()
    view_customerdetails()



#code for updating order details
def update_orderdetails():
    print('''
        (1)ADD DETAILS
        (2)DELETE DETAILS
        (3)EXIT
        ''')
    option=input('enter valid option for updating:')
    if option=='1':
        add_orderdetails()
    elif option=='2':
        del_orderdetails()
    elif option=="3":
        func()
    else:
        print("consider the given options")

def add_orderdetails():
    order_no=input("enter order_no: ")
    date=input("enter date (yyyy-mm-dd): ")
    time=input("enter time(hh:mm) :")
    cls=input("Enter type of cusine: ")
    t=(order_no,date,time,cls)
    add='insert into orders values(%s,%s,%s,%s)'
    cursor1.execute(add,t)
    database.commit()
    view_orderdetails()
def del_orderdetails():
    Del_id=input("enter order_no:")
    delete="Delete from orders where order_no={}".format(Del_id)
    cursor1.execute(delete)
    database.commit()
    view_orderdetails()




#code for updating food details
def update_fooddetails():
    print('''
        (1)ADD DETAILS
        (2)DELETE DETAILS
        (3)EXIT
        ''')
    option=input('enter valid option for updating:')
    if option=='1':
        add_fooddetails()
    elif option=='2':
        del_fooddetails()
    elif option=="3":
        func()
    else:
        print("consider the given options")

def add_fooddetails():
    food_id=input("enter food_id: ")
    name=input("enter Item Name: ")
    price =input("enter price for each(rupee): ")
    desc=input("enter Description: ")
    qty=input("enter quantity: ")
    t=(food_id,name,price,desc,qty)
    add='insert into food values(%s,%s,%s,%s,%s);'
    cursor1.execute(add,t)
    database.commit()
    view_fooddetails()
def del_fooddetails():
    Del_id=input("enter the item name:")
    delete="delete from food where food_id={}".format(Del_id)
    cursor1.execute(delete)
    database.commit()
    view_fooddetails()



#code for updating category details
def update_categorydetails():
    print('''
        (1)ADD DETAILS
        (2)DELETE DETAILS
        (3)EXIT
        ''')
    option=input('enter valid option for updating:')
    if option=='1':
        add_categorydetails()
    elif option=='2':
        del_categorydetails()
    elif option=="3":
        func()
    else:
        print("consider the given options")

def add_categorydetails():
    food_id=input("enter food_id: ")
    c_id=input("enter category_id: ")
    c_name =input("enter category_name:")
    t=(food_id,c_id,c_name)
    add='insert into category values(%s,%s,%s);'
    cursor1.execute(add,t)
    database.commit()
    view_categorydetails()
def del_categorydetails():
    Del_id=int(input("enter category_id:"))
    delete="Delete from category where c_id={}".format(Del_id)
    cursor1.execute(delete)
    database.commit()
    view_categorydetails()

#code for updating payment details
def update_paymentdetails():
    print('''
        (1)ADD DETAILS
        (2)DELETE DETAILS
        (3)EXIT
        ''')
    option=input('enter valid option for updating:')
    if option=='1':
        add_paymentdetails()
    elif option=='2':
        del_paymentdetails()
    elif option=="3":
        func()
    else:
        print("consider the given options")

def add_paymentdetails():
    pay_id=input("enter Payment_id: ")
    pay_type=input("enter mode of payment: ")
    net_price =input("enter total cost: ")
    t=(pay_id,pay_type,net_price)
    add='insert into payment values(%s,%s,%s);'
    cursor1.execute(add,t)
    database.commit()
    view_paymentdetails()
def del_paymentdetails():
    Del_id=int(input("enter the code"))
    delete="Delete from payment where id={}".format(Del_id)
    cursor1.execute(delete)
    database.commit()
    view_paymentdetails()

ID=input('enter login id:')
password=input("password:")
if ID=='dbms project':
    if password == 'Madansai@2002':
        print("       welcome to the Online Food Order managment system      ")
        func()
    else:
        print("please enter the correct password")
else:
    print("please enter the correct id")