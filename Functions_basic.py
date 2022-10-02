def calculator(num1, num2, operator):
    
    if operator == 'plus':
        result = num1 + num2   
        print(result)

    elif operator == 'minus':
        result = num1 - num2
        print(result)

    elif operator == 'multiplication':
        result = num1 * num2
        print(result)

    elif operator == 'divide':
        result = num1 / num2
        print(result)

    else: 
        print(f'{operator.title()} is not recognized as a operator, try again...')

    

calculator(10, 10, 'plus ')

