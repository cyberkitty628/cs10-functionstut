def area(width, height):
    result = width * height
    return result

result = area(5, 6)
print(result)

twin_bed = area(38, 75)
print("A twin bed measures at " + str(twin_bed) + " square inches.")

queen_bed = area(60, 80)
print("A queen bed measures at " + str(queen_bed) + " square inches.")

def substract(num1, num2):
    result = num1 - num2
    return result

result = substract(5, 2)
print(result)

def add(num1, num2):
    result = num1 + num2
    return result

cost_of_bed_set = add(80, 40)
print("Your total for a comforter and pillow set comes to " + "$" + str(cost_of_bed_set) + ".")

cost_of_sheets = add(120, 40)
print("If you want to add a set of sheets, your totall will be updated to " + "$" + str(cost_of_sheets) + ".")