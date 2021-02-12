
def fizzbuzz(num: int) -> str:
    """
    Function to play the game FIzz Buzz.
    
    :param num: The number to check.
    :return: `fizz` if the number if divisble by 3.
        `buz` if the number is divisible by 5.
        `fizzbuzz` if the number is divisible by both 3 and 5.
        The number as a string otherwise

    """
    if num % 15 == 0:
        return 'fizzbuzz'
    elif num % 5 == 0:
        return 'buzz'
    elif num % 3 == 0:
        return 'fizz'
    else:
        return str(num)

def factorialNum(number: int) -> int:
    """
    Function which returns the factorial if a given integer.

    :param number: The Integer to calculate the factorial of.
    :return: Integer evaluation of `number`!

    docstring
    """

    tmp = 0
    
    for i in range(number+1):
        if i == 0:
            tmp = 1
        else:
            tmp *= i
        if i < 37:
            print("{} {}".format(i, tmp))
    
    return tmp

factorialNum(100)

