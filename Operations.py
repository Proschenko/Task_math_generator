import math
from My_exceptions import My_exceptions


class Operations:
    @staticmethod
    def sum(expression_1, expression_2):
        try:
            return expression_1 + expression_2
        except OverflowError:
            raise OverflowError

        except ValueError:
            raise ValueError

    @staticmethod
    def subtraction(expression_1, expression_2):
        try:
            return expression_1 - expression_2

        except OverflowError:
            raise OverflowError

        except ValueError:
            raise ValueError

    @staticmethod
    def multiplication(expression_1, expression_2):
        try:
            return expression_1 * expression_2

        except OverflowError:
            raise OverflowError

        except ValueError:
            raise ValueError

    @staticmethod
    def division(expression_1, expression_2):
        try:
            return expression_1 / expression_2

        except ZeroDivisionError:
            raise ZeroDivisionError

        except ValueError:
            raise ValueError

    @staticmethod
    def exponentiation(expression_1, expression_2):
        try:
            return expression_1 ** expression_2

        except OverflowError:
            raise OverflowError

        except ValueError:
            raise ValueError

    @staticmethod
    def factorial(expression):
        try:
            return math.factorial(expression)

        except OverflowError:
            raise OverflowError

        except:
            raise My_exceptions.Factorial_error()
