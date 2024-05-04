from datetime import datetime
from operation import rent_land


print("\t \t \t \t \t \t TechnoRental Property \t \t \t \t \t \t")
print("\t \t \t \t \tKathmandu\t \t \t \t \t") 
def main():

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
            problem=True
            while problem:
                name=input("enter your name")
                if name.isalpha():
                    problem=False
                Phone=str(input("enter your phone number"))
                if len(Phone)==10 and Phone.isdigit:
                    problem=False
            kitta=int(input("enter the kitta no."))
            
            with open("land.txt", "r") as file:
                mydictionary = {}
                kitta = 101
                for line in file:
                    line = line.replace("\n", "")
                    print(kitta, "\t", line)
                    mydictionary[kitta] = line.split(',')
                    kitta += 1
            
            print("Below are the options:")
            print("\n")
            print("-------------Kitta no \t District \t Direction \t Anna \t Price \t Availability-------------")
            return_Land=int(input("Enter the kitta no. you want to return"))
            with open("land.txt", "r") as file:
                mydictionary = {}
                kitta = 101
                for line in file:
                    line = line.replace("\n", "")
                    print(kitta, "\t", line)
                    mydictionary[kitta] = line.split(',')
                    kitta += 1 
            print("Thank you for returning")
            



            
        elif user_input == "3":
            print("Thank you for using our service")
            loop=False
        else:
            print("Enter the correct option")
main()