def calc_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter


# user input
length = float(input("Enter length: "))
width = float(input("Enter width: "))

# function call
area, perimeter = calc_rectangle(length, width)

print("Area:", area, ", Perimeter:", perimeter)
