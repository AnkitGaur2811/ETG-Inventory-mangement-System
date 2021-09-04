import json
from datetime import date
import pandas as pd


def new_prod():
    '''
    Makes a dictionary for the new product

    Returns
    -------
    None.

    '''
    print("========================================================")
    print("Enter Details of new product:")
    new_product={}
    id=int(input("Enter product Id for new entry:"))
    new_product[id]={}
    new_product[id]["Name"]=input("Enter the name of product:")
    new_product[id]["Company"]=input("Product is manufactured by:")
    new_product[id]["Exp_date"]=input("Enter product Expiry date:")
    new_product[id]["Price"]=float(input("Enter price of Product:"))
    new_product[id]["Quantity"]=int(input("Enter The qunatity of product:"))
    print(new_product)
    
    try: 
        with open("records.json","r+") as record:
            data=json.load(record)
            print(data)
            data.update(new_product)
            print(data)
            record.seek(0)
            json.dump(data,record)
    except:
        with open("records.json","w") as record:
            json.dump(new_product,record)
    Invetory()
        
def table_printer():
    '''
    print whole inventory as a table

    Returns
    -------
    None.

    '''
    record=open("records.json","r")
    data=json.load(record)
    
    df=pd.DataFrame(data)
    df=df.transpose()
    print(df)
    record.close()
    
def bill_printer():
    '''
    print all bills in tabular form

    Returns
    -------
    None.

    '''
    record=open("billing.json","r")
    data=json.load(record)
    
    df=pd.DataFrame(data)
    df=df.transpose()
    print(df)
    record.close()

    

def new_bill():
    '''
    Bill making function

    Returns
    -------
    None.

    '''
    print("=============================================================")
    print("Creating New bill Enter all details:")
    new_cust={}
    bill=0.00
    id=int(input("Enter Id for new customer:"))
    new_cust[id]={}
    new_cust[id]["Name"]=input("Enter Name of customer:")
    new_cust[id]["Mobile"]=input("Enter customer mobile Number:")
    new_cust[id]["Bill_Date"]=str(date.today())
    print("Now you can start shoping")
    
    while(1):
       record=open("records.json","r+")
       data=json.load(record)
       df=pd.DataFrame(data)
       df=df.transpose()
       print(df)
       record.close()
       
       product=(input("Enter product Id for item needed:"))
       if product not in data.keys():
           print("wrong Entry try again")
           continue
       
       quant=int(input("Enter Quantity needed:"))
       bill=bill+(data[product]["Price"]*quant)
       
       record2=open("records.json","r+") 
       data=json.load(record2)
       data[product]["Quantity"]=data[product]["Quantity"]-quant
       
       record2.seek(0)
       json.dump(data,record2)
       record2.truncate()
       record2.close()
       
       
       c=input("Do you want to continue purchase(Y/N):")
       if c=="N" or c == "n":
           print("Your bill Amount is "+str(bill))
           break
       
       
       
    new_cust[id]["bill"]=bill
    
    try: 
        with open("billing.json","r+") as bills:
            data=json.load(bills)
            data.update(new_cust)
            bills.seek(0)
            json.dump(data,bills)
    
    except:
        with open("billing.json","w") as bills:
            json.dump(new_cust,bills)
    billing()
    


def Invetory():
    '''
    This is the function which gives options what you can do with inventory bsic functions
    like: insert, update, delete

    Returns nothing just gives us the view for inventory
    -------

    '''
    print("\t\t ___________________________________________")
    print("\t\t|            Inventory Format               |")
    print("\t\t|___________________________________________|")
    print("\t\t Select Action to perform: \n\t\t 1. Enter New product \n\t\t 2. Show the inventory \n\t\t 3. All bills  \n\t\t 4. BACK ")
    n=int(input("\t\tEnter your choice of action:"))
    if n==1:
        new_prod()
    elif n==2:
        table_printer()
    elif n==3:
        bill_printer()
    elif n==4:
        print("\t\t Exiting...")
        print("\n\n\n")
        first_view()
    else:
        print("\t\t wrong choice restarting...")
        print("\n\n\n")
        Invetory()
def billing():
    '''
    This function just save all the billing things
    save all the billing things in billing files

    Returns nothing just gives view for the billing things
    -------

    '''
    print("\t\t ___________________________________________")
    print("\t\t|               Billing format              |")
    print("\t\t|___________________________________________|")
    print("\t\t Select Action to perform: \n\t\t 1. Make NEW Bill \n\t\t 2. BACK")
    n=int(input("\t\tEnter your choice of action:"))
    if n==1:
        new_bill()
    elif n==2:
        print("\t\t Exiting...")
        print("\n\n\n")
        first_view()
    else:
        print("\t\t wrong choice restarting...")
        print("\n\n\n")
        billing()

def first_view():
    '''
    This is the First thing you see when you run the program it gives choice of actions to that can
    be done by the system

    Returns nothing just gives proper work flow 
    -------

    '''
    print("\t\t ___________________________________________")
    print("\t\t|        Inventory Mangement System         |")
    print("\t\t|___________________________________________|")
    print("\t\t Select Action to perform: \n\t\t 1. Update the Inventory \n\t\t 2. Make the bill\n\t\t 3.Exit")
    n=int(input("\t\tEnter your choice of action:"))
    if n==1:
        Invetory()
    elif n==2:
        billing()
    elif n==3:
        return None
    else:
        print("\t\t wrong choice restarting...")
        print("\n\n\n")
        first_view()
    

first_view()
table_printer()