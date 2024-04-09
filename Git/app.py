from calculation import addition, subtraction, multiplicaion, division

def operation_type():
    '''
    Takes input for the type of calcuation

    Returns:
    num(int): the opertion number
    '''
    print("Type the number associated withe the operation:\n")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
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
    print("\nEnter the first number : ")
    num1 = int(input())
    print("Enter the second number : ")
    num2 = int(input())
    return num1, num2


def main():
    ########### Main:
    operation = int(operation_type())
    num1, num2 = take_inputs()
    #print(operation, num1, num2)

    if(operation == 1):
        result = addition(num1, num2)
    elif(operation == 2):
        result = subtraction(num1, num2)
    elif(operation == 3):
        result = multiplicaion(num1, num2)
    elif(operation == 4):
        result = division(num1, num2)
    else:
        print(operation)
        print("Invalid operation type")
        return
    
    print("\nThe output of the opeartion is : ", result)
    

main()