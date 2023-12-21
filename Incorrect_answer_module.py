import random


class IncorrectAnswer:
    @staticmethod
    def incorrect_answer_number(true_answer, wrong_numbers_operation_list, *operations):
        """
        Функция для генерации неправильных ответов для числа
        :param true_answer: правильный ответ
        :param wrong_numbers_operation_list: Массив чисел, который взаимодействует с правильным ответом, рекомендуется 2, 3, 4
        :param operations: массив операций, которые будут применены к правильному ответу
        :return:
        """
        incorrect_answer = []
        true_answer = int(true_answer)
        for operation in operations:
            match operation:
                case "*":
                    incorrect_answer.append(true_answer * random.choice(wrong_numbers_operation_list))
                case "/":
                    if true_answer != 0:  # Убедимся, что мы не делим на ноль
                        incorrect_answer.append(true_answer / random.choice(wrong_numbers_operation_list))
                case "+":
                    incorrect_answer.append(true_answer + random.choice(wrong_numbers_operation_list))
                case "-":
                    incorrect_answer.append(true_answer - random.choice(wrong_numbers_operation_list))
                case "%":
                    if true_answer != 0:  # Убедимся, что мы не делим на ноль
                        incorrect_answer.append(true_answer % random.choice(wrong_numbers_operation_list))
                case "//":
                    if true_answer != 0:  # Убедимся, что мы не делим на ноль
                        incorrect_answer.append(true_answer // random.choice(wrong_numbers_operation_list))
                case "**":
                    incorrect_answer.append(true_answer ** random.choice(wrong_numbers_operation_list))

        if true_answer in incorrect_answer:
            incorrect_answer.remove(true_answer)

        return incorrect_answer
