from stack import Stack
# Задание 1.
# Перевести выражение из инфиксной формы в постфиксную форму
# записи.
# Говорят, что выражение записано в инфиксной форме, если знак
# операции (сложения, умножения, вычитания либо деления) стоит между
# своими аргументами, например, 5 + 7. Каждая операция имеет приоритет
# выполнения (сначала выполняются умножение и деление, затем сложение и
# вычитание).
# Для изменения приоритета выполнения операций используются
# круглые скобки. Вычислять значение выражения, записанного в инфиксной
# форме, неудобно. Проще сначала перевести его в постфиксную.
# Для перевода выражения из инфиксной формы в постфиксную с учетом
# приоритетов операций и скобок существует простой алгоритм.
# Алгоритм работает со стеком, в котором хранятся знаки операций.
# Сначала стек пуст. На вход алгоритму подается последовательность лексем
# (числа, скобки или знаки операций), представляющая некоторое
# арифметическое выражение, записанное в инфиксной форме. Результатом
# работы алгоритма является эквивалентное выражение в постфиксной форме.
# Вводятся приоритеты операций: открывающая скобка имеет приоритет
# 0, знаки + и – — приоритет 1 и знаки * и / — приоритет 2.
# 2
# Алгоритм:
# 1. Если не достигнут конец входной последовательности, прочитать
# очередную лексему.
# 1.1. Если прочитан операнд (число), записать его в выходную
# последовательность.
# 1.2. Если прочитана открывающая скобка, положить ее в стек.
# 1.3. Если прочитана закрывающая скобка, вытолкнуть из стека в
# выходную последовательность все до открывающей скобки. Сами скобки
# уничтожаются.
# 1.4. Если прочитан знак операции, вытолкнуть из стека в выходную
# последовательность все операции с большим либо равным приоритетом, а
# прочитанную операцию положить в стек.
# 2. Если достигнут конец входной последовательности, вытолкнуть все
# из стека в выходную последовательность и завершить работу.
# Реализуйте метод to_postfix класса ExpressionConverter в файле
# expression.py и протестируйте класс Expression.

#Дополнительное задание 1.
#Стандартный алгоритм перевода из инфиксной формы в постфиксную
#форму записи не учитывает, что в выражении могут участвовать
#отрицательные числа. Напишите метод, который приводит инфиксную форму
#к виду пригодному для перевода в постфиксную форму. Отрицательные числа
#в арифметическом выражение заключаются в круглые скобки, кроме случая
#когда выражение начинается с отрицательного значения.

#Дополнительное задание 2.
#Напишите метод, который проверяет, правильно ли расставлены скобки
#внутри инфиксной записи арифметического выражения.
class BracketError(Exception):
    def __init__(self, text: str):
        self.text = text
class ExpressionConverter:
    operation_priority = {
        '(': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }

    @staticmethod
    def __normalize_infix_expression(expression: str) -> str:
        """
        Метод который учитывает отрицательные значения и приводит инфиксную
        запись выражения к виду пригодному для перевода в постфиксную запись
        :param expression: str: строковое выражение.
        :return:
            str: строка.
        """
        if expression[0] == "-":
            expression = "0" + expression
        if "(-" in expression:
            expression = expression.replace("(-", "(0-")
        return expression

    @staticmethod
    def __check_drackets(expression: str)-> bool:
        """
        Проверка на правильность расстановки скобок '()'
        :param expression str: строка
        :return:
            True: Корректно
            False: Не корректно
        """
        brackets = {
            "(": ")",
            }
        stack = Stack
        for symbol in expression:
            if symbol in brackets.keys():
                stack.push(symbol)
            elif not stack.is_empty() and symbol == brackets [stack.peek()]:
                stack.pop()
            elif symbol.isdigit() or symbol in "+-*/ ":
                continue
            else:
                return False
    @staticmethod
    def __modification_expression(expression: str) -> str:
        """

        Пробеловы между операндами и знаками.
        :param expression: str: строка.
        :return:
            str: строка с расставленными пробелами.
        """
        res_str = ""
        for symbol in expression:
            if symbol.isdigit():
                res_str += symbol
            elif symbol in "+-*/()":
                res_str += " " + symbol + " "
        return res_str
    @staticmethod
    def to_postfix(expression: str) -> list:
        result_str = ""
        stack = Stack()
        check_brackets = ExpressionConverter.__check_drackets(expression)
        if check_brackets:
            expression = ExpressionConverter.__normalize_infix_expression(expression)
            expression = ExpressionConverter.__modification_expression(expression)
            operation_value = ExpressionConverter.operation_priority
        else:
            raise BracketError(f"Не корректно расставлены скобки: {expression}.")
        for symbol in expression:
#1.1
            if symbol.isdigit():
                result_str += symbol
#1.2
            elif symbol == "(":
                stack.push(symbol)
#1.3
            elif symbol == ")":
                while stack.peek() != "(":
                    result_str += " " + stack.peek()
                    stack.pop()
                stack.pop()
            elif symbol == " ":
                result_str += symbol
#1.4
            elif symbol in "+-*/":
                if len(stack) == 0:
                    stack.push(symbol)
                elif not stack.is_empty() and operation_value[symbol] <= operation_value[stack.peek()]:
                    while not stack.is_empty() and operation_value[stack.peek()] >= operation_value[symbol]:
                        result_str += " " + stack.peek()
                        stack.pop()
                    stack.push(symbol)
                else:
                    stack.push(symbol)

#2
        while len(stack) != 0:
            result_str += " " +  stack.pop()
        return result_str.split()


class Expression:

    def __init__(self, expression: str):
        self.__infix_expression = expression
        self.__postfix_expression = ExpressionConverter.to_postfix(expression)

    @property
    def infix_expression(self):
        return self.__infix_expression

    @property
    def postfix_expression(self):
        return self.__postfix_expression

    def get_expression_value(self):
        '''
        Возвращает значение выражения, записанного в постфиксной форме в поле __postfix_expression
        :return:
        '''
        pass



def execute_application():
    expression_str = "6+(-3)*(-2)+(-9)*(-8+3*(-2))"
    try:
        postfix_list = ExpressionConverter.to_postfix(expression_str)
        print(postfix_list)
    except (BracketError) as e:
        print(e)


if __name__ == '__main__':
    execute_application()