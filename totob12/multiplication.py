import numpy as np

class Multiplication:
    """
    Instantiate a multiplication operation.
    Numbers will be multiplied by the given multiplier.
    
    :param multiplier: The multiplier.
    :type multiplier: int
    """
    
    # def __init__(self, multiplier):
    #     self.multiplier = multiplier
    
    def multiply(number1, number2):
        """
        Multiply a given number by the multiplier.
        
        :param number: The number to multiply.
        :type number: int   
    
        :return: The result of the multiplication.
        :rtype: int
        """        
        # Using NumPy .dot() to multiply the numbers
        return np.dot(number1, number2)
