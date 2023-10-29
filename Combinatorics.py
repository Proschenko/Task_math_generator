import random
from Operations import Operations
from My_exceptions import My_exceptions


class Combinatorics:
    @staticmethod
    def C(k, n):
        if k > n or k < 0 or n < 0:
            raise My_exceptions.combinatoric_n_k_error()
        return Operations.factorial(n) / (Operations.factorial(n - k) * Operations.factorial(k))

    @staticmethod
    def P(k, n):
        if k > n or k < 0 or n < 0:
            raise My_exceptions.combinatoric_n_k_error()
        return Operations.factorial(n) / (Operations.factorial(n - k))

    @staticmethod
    def number_generation(min_number, max_number):
        if min_number > max_number:
            raise My_exceptions.Min_max_error()
        else:
            return random.randint(min_number, max_number)

    @staticmethod
    def float_number_generation(min_number, max_number, round_inner):
        if min_number > max_number:
            raise My_exceptions.Min_max_error()
        else:
            return round(random.random() * (max_number - min_number) + min_number, round_inner)
