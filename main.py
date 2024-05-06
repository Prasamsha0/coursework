from datetime import datetime
from operation import rent_land,return_land
from write import invoices

def main():

    print("\t \t \t \t \t \t TechnoRental Property \t \t \t \t \t \t")
    print("\t \t \t \t \tKathmandu\t \t \t \t \t") 
    loop = True
    while loop==True:
        print("press 1 to rent")
        print("press 2 to return")
        print("press 3 to exit")

        input_=True 
        while input_==True:
            user_input =input("Enter the option the option you want to continue") 
            input_=False
        if user_input == "1":
           rent_land()
        elif user_input == "2":
            return_land()
        elif user_input == "3":
            print("Thank you for using our service")
            loop=False
        else:
            print("Enter the correct option")
main()