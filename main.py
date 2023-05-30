from data_structure.stack import Stack
#Задание 2.
#Реализовать алгоритм вычисления выражения по постфиксной (обратной польской) записи.
#Обратная польская нотация или постфиксная нотация — форма записи
#математических и логических выражений, в которой операнды расположены
#перед знаками операций. Выражение читается слева направо.
#Когда в выражении встречается знак операции, выполняется
#соответствующая операция над двумя ближайшими операндами,
#находящимися слева от знака операции. Результат операции заменяет в
#выражении последовательность её операндов и знак, после чего выражение
#вычисляется дальше по тому же правилу. Таким образом, результатом
#вычисления всего выражения становится результат последней вычисленной операции.
#Например, выражение (1 + 2) * 4 + 3 в постфиксной нотации будет
#выглядеть так: 1 2 + 4 * 3 +, а результат: 15.
#Реализуйте метод get_expression_value() класса Expression, который
#принимает список, каждый элемент которого содержит неотрицательное
#число или знак операции (+, -, *, /).
#Функция должна вернуть результат вычисления по обратной польской записи.
#2
#Для вычисления значения выражения, записанного в постфиксной
#форме, можно использовать описанный далее алгоритм. На вход подается
#последовательность лексем (числа или знаки операций), представляющая
#некоторое арифметическое выражение, записанное в постфиксной форме.
#Результатом работы алгоритма является значение этого выражения.
#1. Если не достигнут конец входной последовательности, прочитать
#очередную лексему.
#2. Если прочитан операнд (число), положить его в стек.
#3. Если прочитан знак операции, вытолкнуть из стека два операнда и
#положить в стек результат применения прочитанной операции к этим
#операндам, взятым в обратном порядке.
#4. Если достигнут конец входной последовательности, завершить
#работу. В стеке останется единственное число — значение выражения.

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

        expression = ExpressionConverter.__normalize_infix_expression(expression)

        expression = ExpressionConverter.__modification_expression(expression)
        operation_value = ExpressionConverter.operation_priority
        for symbol in expression:
            # 1.1.
            if symbol.isdigit():
                result_str += symbol

            # 1.2.
            elif symbol == "(":
                stack.push(symbol)
            # 1.3.
            elif symbol == ")":
                while stack.peek() != "(":
                    result_str += " " + stack.peek()
                    stack.pop()
                stack.pop()
            elif symbol == " ":
                result_str += symbol
            # 1.4.
            elif symbol in "+-*/":
                if len(stack) == 0:
                    stack.push(symbol)
                elif operation_value[symbol] <= operation_value[stack.peek()]:
                    while not stack.is_empty() and operation_value[stack.peek()] >= operation_value[symbol]:
                        result_str += " " + stack.peek()
                        stack.pop()
                    stack.push(symbol)
                else:
                    stack.push(symbol)

        # 2.
        while len(stack) != 0:
            result_str += " " + stack.pop()
        return result_str.split()


class Expression:

    def __init__(self, expression: str):
        self.__infix_expression = expression
        self.__postfix_expression = ExpressionConverter.to_postfix(expression)

    @staticmethod
    def __is_valid_expression(expression: str) -> bool:
        """
        Проверяет выражение на корректность ввода.
        :param expression: str: строка.
        :return:
            True: корректно.
            False: не корректно.
        """
        brackets = {
            "(": ")",
        }
        stack = Stack()
        for i, symbol in enumerate(expression):
            if not symbol.isdigit() and symbol not in "+-*/() ":
                raise ExpressionValueError(f"Не корректный символ {symbol}, в {expression}")
            if symbol in "+-*/" and expression[i + 1] in "+-*/" and i != len(expression) - 1:
                return False
            if symbol in brackets.keys():
                stack.push(symbol)
            elif not stack.is_empty() and symbol == brackets[stack.peek()]:
                stack.pop()
            elif symbol.isdigit() or symbol in "+-*/ ":
                continue
            else:
                return False

        if stack.is_empty():
            return True
        raise BracketError(f"Не корректно расставлены скобки  {expression}")

    def __setattr__(self, key, value):
        if key == "_Expression__infix_expression" and not self.__is_valid_expression(value):
            raise ExpressionValueError(f"Выражение: {value} не корректно.")
        else:
            object.__setattr__(self, key, value)

    @property
    def infix_expression(self):
        return self.__infix_expression

    @property
    def postfix_expression(self):
        return self.__postfix_expression

    def get_expression_value(self):
        """
        Возвращает значение выражения, записанного в постфиксной форме
        :return:
            float: результат выражения.
        """
        stack = Stack()
        for symbol in self.postfix_expression:
            if symbol.isdigit():
                stack.push(symbol)

            elif symbol in "+-*/":
                a = int(stack.pop())
                b = int(stack.pop())
                if symbol == "+":
                    stack.push(b + a)
                elif symbol == "-":
                    stack.push(b - a)
                elif symbol == "*":
                    stack.push(b * a)
                else:
                    stack.push(b / a)

        return stack.pop()


def execute_application():
    expression_str = "6+(-3)*(-2)+(-9)*(-8+3*(-2))"
    try:
        postfix_list = ExpressionConverter.to_postfix(expression_str)
        print(postfix_list)
    except (BracketError) as e:
        print(e)


if __name__ == '__main__':
    execute_application()