num1 = float(input())
num2 = float(input())
sign = input()
if sign == 'mod':
    if num2 == 0:
        print('Деление на 0!')
    else:
        print(num1 % num2)
elif sign == 'pow':
    print(num1 ** num2)
elif sign == 'div':
    if num2 == 0:
        print('Деление на 0!')
    else:
        print(num1 // num2)
elif sign == '+':
    print(num1 + num2)
elif sign == '-':
    print(num1 - num2)
elif sign == '*':
    print(num1 * num2)
elif sign == '/':
    if num2 == 0:
        print('Деление на 0!')
    else:
        print(num1 / num2)