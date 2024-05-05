from read import buy_land
from datetime import datetime

def invoices(name,phone,kitta, aana,month , total_price):
    land_data=buy_land()
    user_land=[]
    name_=name
    phone_=phone
    kitta_=kitta
    aana_=aana
    month_=month
    total_price_=total_price
    with open(name+str(phone)+".txt", "w") as file:
        file.write("\n")
        file.write("\tTechnoRental Property")
        file.write("\n")
        file.write(" \t \t \t \t Kathmandu")
        file.write("\t \t \t Contact no: 97458436 || Email: dfhv@gmail.com")
        file.write("\n")
        file.write("Name of the customer: " + name + "\n")
        file.write("Phone of the customer: " + str(phone) + "\n")

        file.write("-" * 40)
        file.write("\t \t \t Kitta no \t Anna \t Month \t Price \t Total")
        file.write("-" * 40)
        user_land.append((name_,phone_, kitta_, aana_,month_,total_price_))
        for i in user_land:
            file.write("\n")
            file.write("\n")
            file.write("\t \t \t \t \t \t \t \t \t \t \t \t" + str(i[0]) + "\t \t \t" + str(i[1]) + "\t \t \t" + str(i[2]) + "\t \t \t" + str(i[3]) + "\t \t \t" + str(i[3]))
            file.write("\n")
            file.write("The grand total is " + str(total_price) + "\n")
        file.write("\nThank you for using")

'''
#Creating a function which changes the availibility from available to not available 
def change(land_data):
    with open("test.txt","w") as file:
        for kitta in range (len(land_data)):
            for value in land_data.values:
                file.write(str(land_data[kitta][0]) + "," + str(land_data[kitta][1]) + "," + str(land_data[kitta][2]) + "," + str(land_data[kitta][3]) + "," + str(land_data[kitta][4]))
                file.write("")
'''


def change(land_data):
    try:
        with open("open.txt", "w") as file:
            for values in land_data.values():
                for value in values[:-1]:  # Exclude the last element
                    file.write(value + ",")  # Write value followed by a comma
                file.write(values[-1])  # Write the last value without a comma
                file.write("\n")
    except FileNotFoundError:
        print("File not found")