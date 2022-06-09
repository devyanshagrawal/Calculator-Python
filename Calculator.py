from ast import operator
import art

print(art.logo)

#Addition
def add(a, b):
    return a+b

#Subtraction
def sub(a, b):
    return a-b

#Multiplication
def mul(a, b):
    return a*b

#Division
def div(a, b):
    return a/b

def end():
    return 0

def exi():
    exit()   

operators = {
    '+' : add,
    '-' : sub,
    '*' : mul,
    '/' : div,
    'AC' : end,
    'exit' : exi
}

num1 = float(input("Enter the first number: "))
answer = num1

while(True):
    for key in operators:
        print(key)
    opr = input("Choose from above operator: ")
    if opr == 'AC' or opr == 'ac':
        num1 = float(input("Enter the first number: "))
        answer = num1
        for key in operators:
            print(key)
        opr = input("Choose from above operator: ")
    elif opr == 'exit':
        exi()

    num2 = float(input("Enter the number: "))

    print(f'{answer} {opr} {num2} = {operators[opr](answer, num2)}')

    answer = operators[opr](answer, num2)