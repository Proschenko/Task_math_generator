import random
import re
from My_exceptions import My_exceptions


class AlgebraOfLogic:
    # Project active region start=======================================================================================
    __operations = "¬∧∨→≡⊕()"
    __prior = {
        '¬': 10000000,
        '∨': 20000000,
        '≡': 20000000,
        '⊕': 20000000,
        '→': 20000000,
        '∧': 10000000,
        '(': -100,
        ')': -99
    }

    @staticmethod
    def __generate_logistic_operation(lr_operand, final_iteration, number_of_unknowns, flag_array):
        not_operation = [""]
        operations_inner = []
        if flag_array[0]:
            not_operation.append("¬")
        if flag_array[1]:
            operations_inner.append("∧")
        if flag_array[2]:
            operations_inner.append("∨")
        if flag_array[3]:
            operations_inner.append("⊕")
        if flag_array[4]:
            operations_inner.append("→")
        if flag_array[5]:
            operations_inner.append("≡")

        is_choice = True
        for i in range(len(flag_array)):
            if flag_array[i]:
                is_choice = False

        if is_choice:
            not_operation = ["¬", ""]
            operations_inner = ["∧", "∨", "→", "⊕", "≡"]

        variables = [char for char in "abcdefg"][:number_of_unknowns]
        operator = random.choice(operations_inner)
        left_operand = random.choice(not_operation) + random.choice(variables)
        right_operand = random.choice(not_operation) + random.choice(variables)
        if lr_operand != "":
            if random.random() <= 0.5:
                left_operand = lr_operand
            else:
                right_operand = lr_operand
        if final_iteration:
            return f"({left_operand} {operator} {right_operand})"
        else:
            return f"{left_operand} {operator} {right_operand}"

    @staticmethod
    def generate_middle_logistic_operation(number_of_unknowns, counter_of_variables,
                                           flag_array):
        op_inner = ""
        final_iteration = True
        for step in range(counter_of_variables - 1):
            op = AlgebraOfLogic.__generate_logistic_operation(op_inner, final_iteration, number_of_unknowns, flag_array)
            op_inner = op
            if counter_of_variables - 2 - step == 1:
                final_iteration = False
        return op_inner

    @staticmethod
    def __checking_correctness_logistic_expression(logistic_expression_inner: str, number_of_unknowns_inner):
        logistic_expression_inner = logistic_expression_inner.replace(" ", "").replace("¬", "").replace("∧", "") \
            .replace("∨", "").replace("→", "").replace("(", "").replace(")", "").replace("⊕", "").replace("≡", "")
        if len(set(logistic_expression_inner)) == number_of_unknowns_inner:
            return True
        else:
            return False

    @staticmethod
    def __checkin_correctness_only_expression(logistic_expression_inner: str):
        try:
            logistic_expression_inner = logistic_expression_inner.replace(" ", "").replace("¬", "").replace("∧", "") \
                .replace("∨", "").replace("→", "").replace("(", "").replace(")", "").replace("⊕", "").replace("≡", "") \
                .replace("a", "").replace("b", "").replace("c", "").replace("d", "")
        except:
            return False
        if len(logistic_expression_inner) == 0:
            return True
        else:
            return False

    @staticmethod
    def generate_right_expression(number_of_unknowns, counter_of_variables, flag_array):
        if number_of_unknowns > counter_of_variables:
            raise My_exceptions.algebra_logic_error()
        elif flag_array[0] and sum(flag_array[1:]) == 0:
            raise My_exceptions.algebra_logic_only_denial_error()
        while True:
            expression = AlgebraOfLogic.generate_middle_logistic_operation(number_of_unknowns, counter_of_variables,
                                                                           flag_array)
            if AlgebraOfLogic.__checking_correctness_logistic_expression(expression, number_of_unknowns):
                return expression

    # solutions helper functions =====================================
    @staticmethod
    def __doing(operand1, operand2, symbol=None):  # good
        match symbol:
            case '∧':
                return operand1 and operand2
            case '∨':
                return operand1 or operand2
            case '→':
                return not operand1 or operand2
            case '⊕':
                return not (operand1 == operand2)
            case '≡':
                return operand1 == operand2
            case _:
                raise ValueError

    def __find_symbols(self, string, arr):  # good
        for i in range(len(string)):
            if string[i] in self.__operations:
                arr.append(string[i])

    @staticmethod
    def __denial_replace(string):  # good
        string = string.replace("¬0", '1')
        string = string.replace("¬1", '0')
        return string

    def __solution_bool(self, input_expression):  # good
        # input 1^1^0^1
        tmp = self.__denial_replace(input_expression)
        nums = re.split('[()¬∧∨→⊕≡]', tmp)  # значение переменных a b c d
        nums = list(filter(None, nums))
        nums = list(map(int, nums))

        operation = []  # знаки действий и скобки
        priority = []  # приоритеты выполнения действий
        self.__find_symbols(tmp, operation)
        for i in range(len(operation)):
            priority.append(self.__prior.get(operation[i]))
        tmp_priority_adder = 1
        for i in range(len(operation)):
            priority[i] //= tmp_priority_adder
            if operation[i] == '(':
                tmp_priority_adder *= 10
            if operation[i] == ')':
                tmp_priority_adder //= 10

        operation = list(filter(lambda e: e != '(', operation))
        operation = list(filter(lambda e: e != ')', operation))
        priority = list(filter(lambda e: e > 0, priority))

        while len(nums) > 1:
            global_minim_priority_index = None
            global_minim_priority_value = 1000000000

            for i in range(len(priority)):
                if 0 < priority[i] < global_minim_priority_value:
                    global_minim_priority_index = i
                    global_minim_priority_value = priority[i]

            # Процедура действия
            nums[global_minim_priority_index + 1] = self.__doing(nums[global_minim_priority_index],
                                                                 nums[global_minim_priority_index + 1],
                                                                 operation[global_minim_priority_index])
            nums.pop(global_minim_priority_index)
            operation.pop(global_minim_priority_index)
            priority.pop(global_minim_priority_index)
        return bool(nums[0])

    # вход: a ^ b, bool Flag, выход: кол-во 0 или 1
    def convert_to_bool_expression(self, expression, choice_inner):  # good
        # Выброс ошибки
        if not (self.__checkin_correctness_only_expression(expression)):
            raise My_exceptions.Is_not_AL_expression_error

        # Предобработка строки удаляем лишние пробелы
        space, void = " ", ""
        expression = expression.replace(space, void)

        count = 0
        input1 = list(expression)
        letter_index = []
        letters = []
        # Запоминаем неизвестные и их позиции в строке
        for i in range(len(expression)):
            local_flag1 = True
            if expression[i] not in self.__operations:
                for k in range(len(letters)):
                    if expression[i] == letters[k]:
                        letter_index[k].append(i)
                        local_flag1 = False
                if local_flag1:
                    tmp = [i]
                    letters.append(expression[i])
                    letter_index.append(tmp)

        sensors = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
                   '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
        # НЕЛЬЗЯ БОЛЕЕ 4 НЕИЗВЕСТНЫХ
        new_args = []
        for i in range(2 ** len(letters)):
            new_args.append(sensors[i][len(sensors[0]) - (len(letters)):])

        for i in range(len(new_args)):
            process_sensor = new_args[i]

            for j in range(len(process_sensor)):
                for k in range(len(letter_index[j])):
                    input1[letter_index[j][k]] = process_sensor[j]

            expression = ''.join(input1)
            if self.__solution_bool(expression):
                count += 1

        if choice_inner:
            return count
        else:
            return 2 ** len(letters) - count

    def helper_count_value_in_table(self, expression, choice_inner):
        return self.convert_to_bool_expression(expression, choice_inner)

    # Project active region end=========================================================================================
    '''
    # task 1 functions ==========================

    # endregion
    def task_logic_1(self, count_tasks_inner, number_of_unknowns, counter_of_variables, flag_array):
        space, void = " ", ""
        i = 0
        result_mas = []
        while i < count_tasks_inner:
            choice = random.choice([True, False])
            logistic_expression = self.__generate_middle_logistic_operation(number_of_unknowns, counter_of_variables,
                                                                            flag_array)
            if self.__checking_correctness_logistic_expression(logistic_expression, number_of_unknowns):
                if choice:
                    bool_tmp = "'истина'"
                else:
                    bool_tmp = "'ложь'"

                task_1_output = str.format("::Вопрос 1_{0}::Дана формула логики высказываний {1} Сколько значений {2} "
                                           "содержит ее таблица истинности? {{={3}}}", i, logistic_expression, bool_tmp,
                                           self.convert_to_bool_expression(logistic_expression.replace(space, void),
                                                                           choice))
                i += 1
                result_mas.append(task_1_output)
        return result_mas

    # region приватные всякие функции интересные смотрите разглядывайте для 2 задания
    # task 2 functions ==========================
    def __convert_expression_to_bool_array_task2(self, expression):
        expression_matrix_value_bool = []
        input1 = list(expression)
        letter_index = []
        letters = []
        for i in range(len(expression)):
            local_flag1 = True
            if expression[i] not in self.__operations:
                for k in range(len(letters)):
                    if expression[i] == letters[k]:
                        letter_index[k].append(i)
                        local_flag1 = False
                if local_flag1:
                    tmp = [i]
                    letters.append(expression[i])
                    letter_index.append(tmp)
        # Сортируем по алфавиту
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                if letters[i] > letters[j]:
                    letters[i], letters[j] = letters[j], letters[i]
                    letter_index[i], letter_index[j] = letter_index[j], letter_index[i]

        sensors = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
                   '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']

        new_args = []
        for i in range(2 ** len(letters)):
            new_args.append(sensors[i][4 - (len(letters)):])

        for i in range(len(new_args)):
            process_sensor = new_args[i]

            for j in range(len(process_sensor)):
                for k in range(len(letter_index[j])):
                    input1[letter_index[j][k]] = process_sensor[j]

            expression = ''.join(input1)
            if self.__solution_bool(expression):
                expression_matrix_value_bool.append(True)
            else:
                expression_matrix_value_bool.append(False)
        return expression_matrix_value_bool

    def __result_task_2(self, expressions_array_inner):
        tmp = []
        space, void = " ", ""
        for i in range(len(expressions_array_inner)):
            tmp.append(self.__convert_expression_to_bool_array_task2(expressions_array_inner[i].replace(space, void)))

        for j in range(len(tmp[0])):
            if tmp[1][j] == tmp[2][j] == True and tmp[0][j] == False:
                return False
        return True

    # endregion

    def task_logic_2(self, counter_task, number_of_unknowns, counter_of_variables, flag_array):

        result_mas = []
        for i in range(counter_task):
            expressions_array = []

            while len(expressions_array) < 3:
                logistic_expression = self.__generate_middle_logistic_operation(number_of_unknowns,
                                                                                counter_of_variables, flag_array)
                if self.__checking_correctness_logistic_expression(logistic_expression, number_of_unknowns):
                    expressions_array.append(logistic_expression)

            task_2_output = str.format(
                "::Вопрос 2_{0}::Следует ли формула {1} из формул {2}, {3}? Написать 1, если следует"
                " и 0 в противном случае.{{={4}}}", i, expressions_array[0], expressions_array[1],
                expressions_array[2], int(self.__result_task_2(expressions_array)))
            result_mas.append(task_2_output)
        return result_mas

    # region приватные всякие функции интересные смотрите разглядывайте комментируйте для 3 задания
    # task 3 functions ==========================
    def __calculation_expression_task_3(self, expression, process_sensor):  # good
        input1 = list(expression)
        letter_index = []
        letters = []
        # Запоминаем неизвестные и их позиции в строке
        for i in range(len(expression)):
            local_flag1 = True
            if expression[i] not in self.__operations:
                for k in range(len(letters)):
                    if expression[i] == letters[k]:
                        letter_index[k].append(i)
                        local_flag1 = False
                if local_flag1:
                    tmp = [i]
                    letters.append(expression[i])
                    letter_index.append(tmp)

        # Сортируем по алфавиту
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                if letters[i] > letters[j]:
                    letters[i], letters[j] = letters[j], letters[i]
                    letter_index[i], letter_index[j] = letter_index[j], letter_index[i]

        for j in range(len(process_sensor)):
            for k in range(len(letter_index[j])):
                input1[letter_index[j][k]] = process_sensor[j]

        expression = ''.join(input1)
        if self.__solution_bool(expression):
            return 1
        else:
            return 0

    def __solution_task_3(self, expression_array_inner, process_sensor_inner):
        space, void = " ", ""
        result = 0
        for i in range(len(expression_array_inner)):
            result += self.__calculation_expression_task_3(expression_array_inner[i].replace(space, void),
                                                           process_sensor_inner)
        return result

    # endregion

    def task_logic_3(self, counter_task, number_of_unknowns, counter_of_variables, flag_array):
        result_mas = []
        for i in range(counter_task):
            expressions_array = []
            sensor = str(random.choice(['0', '1'])) + str(random.choice(['0', '1'])) + str(random.choice(['0', '1']))

            while len(expressions_array) < 4:
                logistic_expression = self.__generate_middle_logistic_operation(number_of_unknowns,
                                                                                counter_of_variables, flag_array)
                if self.__checking_correctness_logistic_expression(logistic_expression, number_of_unknowns):
                    expressions_array.append(logistic_expression)

            task_3_output = str.format("::Вопрос 3_{0}::Сколько формул из списка {1}, {2}, {3}, {4} истинны на наборе "
                                       "a = {5}, b = {6}, c = {7}? {{={8}}}", i, expressions_array[0],
                                       expressions_array[1], expressions_array[2], expressions_array[3], sensor[0],
                                       sensor[1], sensor[2], self.__solution_task_3(expressions_array, sensor))
            result_mas.append(task_3_output)
        return result_mas
    '''
