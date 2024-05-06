from read import buy_land
from datetime import datetime

def invoices(name,phone,grand_total,user_land):

    with open(name+str(phone)+".txt", "w") as file:
        file.write("\n")
        file.write("\tTechnoRental Property")
        file.write("\n")
        file.write(" \t \t \t \t Kathmandu")
        file.write("\t \t \t Contact no: 97458436 || Email: dfhv@gmail.com")
        file.write("\n")
        file.write("Name of the customer: " + name + "\n")
        file.write("Phone of the customer: " + str(phone) + "\n")

        file.write("-" * 80)
        file.write("\t \t \t Kitta no \t Anna \t Month \t Price \t Total")
        file.write("-" * 80)

        for i in user_land:
            file.write("\n")
            file.write("\n")
            file.write("\t \t \t \t \t \t \t \t \t \t \t \t" + str(i[0]) + "\t \t \t" + str(i[1]) + "\t \t \t" + str(i[2]) + "\t \t \t" + str(i[3]) + "\t \t \t" + str(i[4]))
            file.write("\n")
        file.write("The grand total is " + str(grand_total) + "\n")
        file.write("\nThank you for using")

def return_invoices(name,phone,grand_total,total_price_fine,user_land):

    with open(name+str(phone)+".txt", "w") as file:
        file.write("\n")
        file.write("\tTechnoRental Property")
        file.write("\n")
        file.write(" \t \t \t \t Kathmandu")
        file.write("\t \t \t Contact no: 97458436 || Email: dfhv@gmail.com")
        file.write("\n")
        file.write("Name of the customer: " + name + "\n")
        file.write("Phone of the customer: " + str(phone) + "\n")

        file.write("-" * 90)
        file.write("\n")
        file.write("Kitta no \t \t district \t \t direction \t \tmonths rented \t\t anna  \t\t Total \t\t fine \t\t total fined price")
        file.write("\n")
        file.write("-" * 90)

        for i in user_land:
            file.write("\n")
            file.write(str(i[0]) + "\t \t \t" + str(i[1]) + "\t \t \t" + str(i[2]) + "\t \t \t" + str(i[3]) + "\t \t \t" + str(i[4]) + "\t \t \t" + str(i[5]) + "\t \t \t" + str(i[7]) + str(i[6]))
            file.write("\n")
        file.write("The grand total is " + str(total_price_fine) + "\n")
        file.write("\nThank you for using")



def change(land_data):
    try:
        with open("land.txt", "w") as file:
            for values in land_data.values():
                for value in values[:-1]:  # Exclude the last element
                    file.write(value + ",")  # Write value followed by a comma
                file.write(values[-1])  # Write the last value without a comma
                file.write("\n")
    except FileNotFoundError:
        print("File not found")