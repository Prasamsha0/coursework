#creating a function that reads the details in the file and the data back in a dictionary
def buy_land():
    land_data = {}
    with open("land.txt", "r") as file:
        kitta=101
        for line in file:
            line = line.replace("\n", ", ")
            land_data[kitta] = line.split(",")
            kitta += 1
    return land_data

#creating a function to just display the data of the land
def land_info():
    with open("land.txt","r") as line:
        kitta=101
        for i in line: 
            print(kitta,"\t ", i.replace(","," \t"))
            kitta+=1
