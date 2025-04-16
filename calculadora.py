print("\n******************* Calculadora em Python ******************* \n")

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply (x,y):
    return x * y

def divide(x,y):
    return x/y

print("Selecione o número  da operação desejada: \n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão \n")

opcao = input("\nDigite sua opção (1/2/3/4): ")
print('\n')

num1 = int(input("\nDigite o primeiro numero: "))
num2 = int(input("\nDigite o segundo numero: "))

if opcao == '1':
    print('\n')
    print(num1, "+", num2, "=", add(num1, num2))
    print('\n')
    
elif opcao == '2':
    print('\n')
    print(num1, "-", num2, "=", subtract(num1, num2))
    print('\n')
    
elif opcao == '3':
    print('\n')
    print(num1, "*", num2, "=", multiply(num1, num2))
    print('\n')
    
elif opcao == '4':
    print('\n')
    print(num1, "/", num2, "=", divide(num1, num2))
    print('\n')
else:
    print("Opcão inválida!")
