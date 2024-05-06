from datetime import datetime
from read import buy_land,land_info
from write import invoices,change, return_invoices

def rent_land():
    land_data={} #creating an empty dicitonary  
    user_land=[] #creating an empty list 
    grand_total=0 #initializing the value of grandtotal as zero

    name = valid_name()
    phone = valid_phone()
    print("The details are given below:")
    print("\n")
    print("Kitta no \t District \t Direction \t Anna \t Price \t Availability")
    land_info()# calling the function which displays only the land's information
    land_data=buy_land() #storing the dictionary's values in land)_data
    continue_loop = True
    while continue_loop:
        kitta = valid_kitta(land_data)
        availability = land_data[kitta][4]
        anna_land = int(land_data[kitta][2])
        if availability == 'Not Available': 
            print(availability)
            print("This land is not available for rent.")
            exit_=input("do you want to exit?")
            if exit_=='y':
                continue_loop=False
            else:
                continue_loop=True 
            continue  # Skip this entry and continue to the next iteration of the loop available = (availability)
        else:
            print("\n",kitta, "kitta number has", anna_land, "anna of land")
            month = valid_month()
            per_month_price = int(land_data[kitta][3])
            bill_kitta = kitta
            anna = anna_land
            month_ = month
            per_month_price_land = per_month_price
            total_price = month_ * per_month_price_land
            land_data[kitta][4] = "Not Available" 
            change(land_data)
            user_land.append(list([bill_kitta, anna, month_, per_month_price_land, total_price]))
        more = input("Do you want more (y/n): ")
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
            invoices(name,phone,grand_total,user_land)
            continue_loop=False
    #return bill_kitta, anna_land, month_, per_month_price_land, total_price, grand_total, __name__

       
def return_land():
    land_data={} #creating an empty dicitonary  
    user_land=[] #creating an empty list 
    grand_total=0 #initializing the value of grandtotal as zero

    name = valid_name()
    phone = valid_phone()
    print("The details are given below:")
    print("\n")
    print("Kitta no \t District \t Direction \t Anna \t Price \t Availability")
    land_info()# calling the function which displays only the land's information
    land_data=buy_land() #storing the dictionary's values in land)_data
    continue_loop = True
    while continue_loop:
        kitta = valid_kitta(land_data)
        if land_data[kitta][4]=="Available":
            print("this land hasn't been rented")
            exit_=input("do you want buy a land first?")
            if exit_=='y':
                continue_loop=False
            else:
                continue_loop=True
        else:
            availability = land_data[kitta][4]
            district = land_data[kitta][0]
            direction = land_data[kitta][1]
            anna_land = int(land_data[kitta][2])
            per_month_price = int(land_data[kitta][3])
            per_month_price_land = per_month_price
            land_data[kitta][4] = "Not Available" 
            bill_kitta = kitta
            anna = anna_land
            month_rented = valid_return_month()
            month_returned = valid_return_months() 
            total_price = month_rented * per_month_price_land
            land_data[kitta][4]="Available"
            
            #incase the user returns the land late
            if month_rented < month_returned:
                delay = float(month_returned-month_rented)
                fine_price = 10/100* (delay*per_month_price_land)
                total_price_fine=fine_price+total_price
                fine=str(fine_price)
            else:
                total_price_fine = total_price
                fine = "Returned on time"
            user_land.append(list([bill_kitta,district,direction,month_returned,anna, total_price,total_price_fine, fine]))
            more=input("Do you want to rent more? \n Press Y to continue and any other key to exit")
            if more.lower() !="y":
                for i in user_land:
                    grand_total += i[6]
                today_date=str(datetime.now())
                print("\n")
                print("\t \t \t \t \t TechnoRental Property \t \t \t\t\t")
                print("\n")
                print(" \t \t \t \t Kathmandu \t \t \t \t ")
                print("\t \t \t Contact no: 97458436 || Email: dfhv@gmail.com")
                print("\n")
                print("Name of the customer:", name, "\n")
                print("Phone of the customer:", phone, "\n")
                print("-" * 110)
                print("Kitta no \t district \t direction \t months rented \t anna \t Total \t fined price \t total fined price")
                print("-" * 110)
                for i in user_land:
                    print(i[0], "\t", i[1], " \t", i[2], "\t", i[3], "\t", i[4], "\t", i[5], "\t", i[7], "\t",i[6])
                print("The grand total is", grand_total)
                print("Date:",today_date)
                print("Thank you for renting!")
                return_invoices(name,phone,grand_total,total_price_fine,user_land)
                continue_loop=False
        #return bill_kitta, anna_land, month_, per_month_price_land, total_price, grand_total, __name__

    
#checking if the kitta is valid or not 
def valid_kitta(kitta_):
        loop_=True #the loop runs till the user enters correct value
        while loop_:
            try:
                kitta=int(input("Enter kitta no.:"))
                if kitta < 1 or kitta > len(kitta_) + 100:
                    print("Please enter the kitta no. between 1 and","\t", len(kitta_))
                    kitta = int(input("Enter a valid kitta: "))
                    loop=True
                elif kitta not in kitta_:
                    print("this kitta does not exists")
                    kitta = int(input("Enter a valid kitta: "))
                    loop=True
                else:
                    loop_=False
                    return kitta
            except:
                print("invalid kitta! try again")

#checking if the phone number entered is exactly ten digits
def valid_phone():
        loop_=True #the loop runs till the user enters correct value
        while loop_:
            try:
                phone=input("Enter phone no.:")
                if phone.isdigit() and len(phone)==10:
                    loop_=False
                    return phone
                else:
                    print("enter valid phone no!")
                    loop_=True
    
            except:
                print("invalid phone number! try again")


#checking if the phone number entered is exactly ten digits
def valid_name():
        loop_=True #the loop runs till the user enters correct value
        while loop_:
            try:
                name=input("Enter name:")
                if name.isalpha():
                    loop_=False
                    return name
                else:
                    print("Invalid Name")
                    loop_=True
    
            except:
                print("invalid name! try again")


#checking the user is not renting the land for more than 12 months or less than one month
def valid_month():
        loop_=True #the loop runs till the user enters correct value
        while loop_:
            try:
                month=int(input("Enter the number of months you want to rent for: "))
                if month>=1 and month<=12:
                    loop_=False
                    return month
                else:
                    print("You can't rent for more than 12 months")
                    loop_=True
    
            except ValueError:
                print("invalid month! try again")

def valid_return_month():
    loop_=True #the loop runs till the user enters correct value
    while loop_:
        try:
            month=int(input("how many months did you rent the land for"))
            if month>=1 and month<=12:
                loop_=False
                return month
            else:
                print("You can't rent for more than 12 months")
                loop_=True

        except ValueError:
            print("invalid month! try again")
    
def valid_return_months():
    loop_=True #the loop runs till the user enters correct value
    while loop_:
        try:
            month=int(input("how many months did you rented the land"))
            if month>=1 and month<=12:
                loop_=False
                return month
            else:
                print("You can't rent for more than 12 months")
                loop_=True

        except ValueError:
            print("invalid month! try again")
    