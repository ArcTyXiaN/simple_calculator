while True:
    a = int(input('Enter num1: '))
    b = int(input('Enter num2: '))
    operator = input('Enter operator (+, -, *, /, //): ')
    
    print(f'You entered {a} as num1, {b} as num2, and {operator} as operator')

    if operator == '+':
        print("Result:", a + b)
    elif operator == '-':
        print("Result:", a - b)
    elif operator == '*':
        print("Result:", a * b)
    elif operator == '/':
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero.")
    elif operator == '//':
        if b != 0:
            print("Result:", a // b)
        else:
            print("Cannot perform floor division by zero.")
    else:
        print("Invalid operator")

    iteral = input('Do you want to perform another operation? (yes/no): ').lower()
    true_options = ['yes', 'yep', 'yeah', 'yo']

    if iteral in true_options:
        print('Running again...\n')
    else:
        print('You are done.')
        break
