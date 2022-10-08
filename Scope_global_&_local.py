multiplier = 2
has_calculated = False

def multiply_calculator(number, has_calculated):
    result = number * multiplier
    has_calculated = True
    
    print(result)
    return has_calculated
print(multiply_calculator(4, has_calculated))