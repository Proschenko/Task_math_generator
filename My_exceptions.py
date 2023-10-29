class My_exceptions(Exception):
    #work
    class Factorial_error(Exception):
        def __init__(self, message="Ошибка факториала,\nотрицательные числа в факториале.\n"):
            super().__init__(message)
    #work
    class Min_max_error(Exception):
        def __init__(self, message="Минимум не должен быть больше максимума,\nпроверьте параметры генерации.\n"):
            super().__init__(message)
    #work
    class algebra_logic_error(Exception):
        def __init__(self, message="Количество неизвестных,\nне может быть меньше количества перменных.\n"):
            super().__init__(message)

    class algebra_logic_only_denial_error(Exception):
        def __init__(self, message="Невозможно составить логическое выражение,\n только из отрицания\n"):
            super().__init__(message)


    class Is_not_graph_error(Exception):
        def __init__(self, message="Во входных данных лежит не граф.\n"):
            super().__init__(message)


    class Is_not_AL_expression_error(Exception):
        def __init__(self, message="Во входных данных лежит не логическое выражение.\n"):
            super().__init__(message)

    class combinatoric_n_k_error(Exception):
        def __init__(self, message="k не может быть меньше n, а также это положительные целые числа или 0\n"):
            super().__init__(message)





