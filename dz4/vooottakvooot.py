def checker(function):
    def checker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as e:
            print(f'We have problems {e}')
        else:
            print(f'No problems. Result - {result}')
    return checker
def calculate(expression):
 return eval(expression)

calculate = checker(calculate)
x = int(input('Перше число: '))
x2 = int(input('Другое число: '))
x3 = (input('Дія: '))
if x3 == '+':
    calculate('x+x2')
elif x3 == '-':
    calculate('x-x2')
elif x3 == '*':
    calculate('x*x2')
elif x3 == '/':
    calculate('x/x2')