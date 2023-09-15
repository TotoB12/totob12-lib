import numpy as np

class Math:
    """
    Instantiate a multiplication operation.
    Numbers will be multiplied by the given multiplier.
    
    :param multiplier: The multiplier.
    :type multiplier: int
    """
    
    def add(*numbers):
        """
        Add any amount of given numbers.

        :param numbers: The numbers to add.
        :type numbers: int, float, list, tuple

        :return: The result of the addition.
        :rtype: int, float, list, tuple
        """
        total = 0
        for number in numbers:
            total += number
        return total
    
    def subtract(number1, number2):
        """
        Subtract a given number from another.

        :param numbers1: The numbers to subtract.
        :type numbers: int, float
        :param number2: The number to subtract.
        :type number2: int, float

        :return: The result of the subtraction.
        :rtype: int, float, list, tuple
        """
        return number1 - number2
    
    def multiply(*numbers):
        """
        Multiply any amount of given numbers by themselves.

        :param numbers: The numbers to multiply.
        :type numbers: int, float, list, tuple
        :return: The result of the multiplication.
        :rtype: int, float, list, tuple
        """
        total = 1
        for number in numbers:
            total *= number
        return total
    
    def divide(number1, number2):
        """
        Divide a given number by the multiplier.
        
        :param number1: The number to divide.
        :type number1: int
        :param number2: The divider.
        :type number2: int
    
        :return: The result of the division.
        :rtype: int
        """
        return np.divide(number1, number2)
