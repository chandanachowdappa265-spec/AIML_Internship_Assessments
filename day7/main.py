import csv

with open("C:\\Users\\chandana\\Music\\Desktop\\practice\\day7\\Company_Data.csv", mode="r") as file:
    csv_file = csv.reader(file)
    for lines in csv_file:
        print(lines)

