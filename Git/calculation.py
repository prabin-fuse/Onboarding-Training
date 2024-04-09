def addition(num1, num2):
    '''
    Addition of two numbers.

    Parameters:
    num1(int or float): The first number to be added.
    num2(int or float): The second number to be added.

    Returns:
    int or float: The sum of two input numbers
    '''
    return num1 + num2


def subtraction(num1, num2):
    '''
    Subtraction of two given numbers.

    Parameters:
    num1(int or float): Minuend of the subtraction operation
    num2(int or float): Subtrahend of the subtraction operation

    Returns:
    int or float: The difference of two numbers.
    Case1: The return number is positive if Minuend >= Subtrahend
    Case2: The retrn number is negative if Minuend < Subtrahend
    '''
    return num1 - num2

def multiplicaion(num1, num2):
    '''
    Multiplication of two given numbers.

    Parameters:
    num1(int or float): Multiplicand for the multiplication operation
    num2(int or float) : Multiplier for the multiplication

    Returns:
    int or float: The product of two numbers
    '''
    return num1 * num2

def division(num1, num2):
    '''
    Division of two given number

    Parameters:
    num1(int or float): The number to be divided i,e. dividend
    num2(int or float): divisor which divides the dividend

    Returns:
    float: The result of division operation
    '''

    if num2 == 0:
        raise ValueError("cannot be divided by zero!")
    
    return num1/num2