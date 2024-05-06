import invoice
import read

def write(mydictionary):
    try:
        with open("land.txt", "w") as file:
            for values in mydictionary.values():
                for value in values[:-1]:  # Exclude the last element
                    file.write(value + ",")  # Write value followed by a comma
                file.write(values[-1])  # Write the last value without a comma
                file.write("\n")
    except FileNotFoundError:
        print("File not found")

def get_anna(kitta, mydictionary):
    error = True
    while error:
        try:
            anna_input = int(input("Enter the anna you want: "))
            if int(mydictionary[kitta][2]) != anna_input:
                print("Please enter anna according to your land kitta")
            else:
                error = False
        except:
            print("Please enter a valid anna")
    return anna_input

def get_kitta(mydictionary):
    error = True
    while error:
        try:
            kitta = int(input("Enter a kitta number: "))
            if kitta <= 100 or kitta > len(mydictionary) + 100:
                print("Enter a correct option")
            else:
                error = False
        except ValueError:
            print("Invalid kitta")
    return kitta

def rent():
    land = []
    rented = True
    name = get_name()
    phone = get_phone()
    print("Below are the options: ")
    print("\n")
    print("Kitta no \t District\t\tDirection \tAnna \t\tPrice\t\tAvailability")
    print("-" * 100)
    mydictionary = read.read()
    loop = True
    error = True

    while loop:
        kitta = get_kitta(mydictionary)
        availability = mydictionary[kitta][4]
        if availability.lower() == 'not available':
            print("The kitta is not available. Please choose another kitta")
            error = True
        else:
            anna_land = get_anna(kitta, mydictionary)
            print("Availability Status: " + availability)
            print(kitta, "kitta number has", anna_land, "anna of land")
            month = get_month(rented)
            per_month_price = int(mydictionary[kitta][3])
            mydictionary[kitta][4] = "Not available"
            write(mydictionary)

            # Invoice
            bill_kitta = kitta
            bill_anna = anna_land
            month_ = month
            per_month_price_land = per_month_price
            total_price = month_ * per_month_price_land
            land.append([bill_kitta, bill_anna, month_, per_month_price_land, total_price])

            more_error = True
            while more_error:
                more = input("Do you want to rent more (y/n): ")
                if more.lower() == 'y' or more.lower() == 'n':
                    more_error = False
                else:
                    print("Please enter y for yes and n for no")
            if more.lower() != 'y':
                loop = False

    grand_total = 0.0
    for i in land:
        grand_total += int(i[4])
    invoice.invoice(rented, land, grand_total, name, phone)
    return land, grand_total

def return1():
    land = []
    rented = False
    loop = True
    name = get_name()
    phone = get_phone()
    print("Below are the options: ")
    print("\n")
    print("Kitta no \t District\t\tDirection \tAnna \t\tPrice\t\tAvailability")
    print("-" * 100)
    mydictionary = read.read()

    while loop:
        kitta1 = get_kitta(mydictionary)
        for kitta in mydictionary:
            if kitta == kitta1:
                availability1 = mydictionary[kitta1][4]
                print("Availability Status: ", availability1)
                availability1 = mydictionary[kitta1][4]
                price = int(mydictionary[kitta][3])
                anna_land = int(mydictionary[kitta][2])
                fine = 0.0
                delay_month = 0
                total_monthly_price = 0
                total_price_after_fine = 0

                if availability1.lower() == "not available":
                    month = get_month(rented)
                    return_month = get_return_month()
                    total_monthly_price = float(month * price)

                    if month <= return_month:
                        delay_month = return_month - month
                        fine = float(delay_month * (((10 / 100) * price)))
                        total_monthly_price = float(return_month * price)
                        total_price_after_fine = total_monthly_price + fine
                    else:
                        total_price_after_fine = total_monthly_price

                mydictionary[kitta1][4] = "Available"
                write(mydictionary)

                print("Do you want to continue?")
                more = input("y/n: ")
                bill_k = kitta
                bill_fine = fine
                bill_month = month
                bill_returnMonth = return_month
                bill_total_price = total_monthly_price
                bill_price = price
                bill_anna = anna_land
                bill_total = total_price_after_fine

                land.append([bill_k, bill_anna, bill_month, bill_returnMonth, bill_price, bill_total_price, bill_fine, bill_total])

                if more.lower() == "n":
                    loop = False

    grand_total = 0
    for i in land:
        grand_total += int(i[7])
    print("The grand total is Rs.", grand_total)
    invoice.invoice(rented, land, grand_total, name, phone)
    return land, grand_total

def get_month(rented):
    month_error = True
    while month_error:
        try:
            if rented == True:
                month = int(input("Enter the months for which you want to rent the land: "))
            if rented == False:
                month = int(input("Enter the months you rented the land for: "))
            if month < 13 and month > 0:
                month_error = False
            else:
                print("Please enter a month between 1-12")
        except:
            print("The month given is not valid")
    return month

def get_return_month():
    return_month_error = True
    while return_month_error:
        try:
            return_month = int(input("Enter the month you returned the land: "))
            if return_month < 13 and return_month > 0:
                return_month_error = False
            else:
                print("Please enter the month between the range of 0-12")
        except:
            print("The month you returned is invalid")
    return return_month

def get_name():
    error = True
    while error:
        name = input("Enter your name: ")
        if name.isalpha():
            error = False
        else:
            print("The name provided is invalid.")
    return name

def get_phone():
    error = True
    while
