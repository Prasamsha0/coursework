from datetime import datetime
from read import buy_land,land_info
from write import invoices,change
def rent_land():
    land_data={}
    user_land=[]
    grand_total=0
    name = input("Enter your name: ")
    phone = int(input("Enter your phone number: "))
    print("The details are given below:")
    print("\n")
    print("Kitta no \t District \t Direction \t Anna \t Price \t Availability")
    land_info()# calling the function which displays only the land's information
    land_data=buy_land() #storing the dictionary's values in land)_data
    continue_loop = True
    while continue_loop:
        kitta = int(input("Enter a kitta number: "))
        if kitta < 1 or kitta > len(land_data) + 100:
            print("this option is not valid")
            kitta = int(input("Enter a valid kitta: "))
        availability = land_data[kitta][4]
        anna_land = int(land_data[kitta][2])
        if availability == 'Not Available': 
            print(availability)
            print("This land is not available for rent.") 
            continue  # Skip this entry and continue to the next iteration of the loop available = (availability)
        else:
            print("\n",kitta, "kitta number has", anna_land, "anna of land")
            month = int(input("Enter the number of months you want to rent for: "))
            per_month_price = int(land_data[kitta][3])
            bill_kitta = kitta
            anna = anna_land
            month_ = month
            per_month_price_land = per_month_price
            total_price = month_ * per_month_price_land
            user_land.append(list([bill_kitta, anna, month_, per_month_price_land, total_price]))
            land_data[kitta][4] = "Not Available" 
            change(land_data)
        more = input("Do you want more (y/n): ")
        print(user_land)
        if more.lower() != 'y':
            for i in user_land:
                grand_total += i[4]
            today_date=str(datetime.now())
            print("\n")
            print("\t \t \t \t \t TechnoRental Property \t \t \t\t\t")
            print("\n")
            print(" \t \t \t \t Kathmandu \t \t \t \t ")
            print("\t \t \t Contact no: 97458436 || Email: dfhv@gmail.com")
            print("\n")
            print("Name of the customer:", name, "\n")
            print("Phone of the customer:", phone, "\n")
            print("-" * 90)
            print("\t \t  Kitta no \t \t Anna \t \t Month \t \t Price \t\t Total")
            print("-" * 90)
            for i in user_land:
                print("\t \t", i[0], "\t \t", i[1], "\t \t", i[2], "\t \t", i[3], "\t \t", i[4])
            print("The grand total is", grand_total)
            print("Date:",today_date)
            print("Thank you for renting!")
            invoices(name,phone,bill_kitta, anna,month_ , grand_total)
            continue_loop=False
            
def return_land():
    land_data={}
    user_land=[]
    grand_total=0
    name = input("Enter your name: ")
    phone = int(input("Enter your phone number: "))
    print("The details are given below:")
    print("\n")
    print("Kitta no \t District \t Direction \t Anna \t Price \t Availability")
    land_info()# calling the function which displays only the land's information
    land_data=buy_land() #storing the dictionary's values in land)_data
    continue_loop = True
    while continue_loop:
        kitta = int(input("Enter the land you want to return "))
        if kitta < 1 or kitta > len(land_data) + 100:
            print("this option is not valid")
            kitta = int(input("Enter a valid kitta: "))
        availability = land_data[kitta][4]
        anna_land = int(land_data[kitta][2])


