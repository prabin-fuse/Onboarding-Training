def operation_type():
    '''
    Takes input for the type of calcuation

    Returns:
    num(int): the opertion number
    '''
    print("Type the number associated withe the operation:\n")
    print("1) Addition\n")
    print("2) Subtraction\n")
    print("3) Multiplication\n")
    print("4) Division\n")
    num = input()
    return num


def take_inputs():
    '''
    Takes the input from user and returns two numbers

    Parameters:

    Returns:
    num1(int or float): The first number for calculation purpose
    num2(int or float): Second number for required calculation
    '''
    num1 = input()
    num2 = input()
    return num1, num2


########### Main:
operation = operation_type()
num1, num2 = take_inputs()
#print(operation, num1, num2)


