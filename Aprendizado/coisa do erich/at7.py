def som(a, b):
    somar = a + b
    return somar

def sub(a, b):
    subtracao = a - b
    return subtracao

def mult(a, b):
    multiplicacao = a * b
    return multiplicacao

def div(a, b):
    div = a / b
    return div

def inicio():
    a = int(input("Digite um número: "))
    b = int(input("Digite mais um número: "))

    print("====================")
    print("1 - soma")
    print("2 - subtração")
    print("3 - multiplicação")
    print("4 - divisão")
    print("====================")

    resp = int(input("digite o número correspondente a operação desejada: "))

    if resp == 1:
        print(som(a, b))

    elif resp == 2:
        print(sub(a, b))

    elif resp == 3:
        print(mult(a, b))

    elif resp == 4:
        print(div(a, b))
    else:
        print("resposta inválida, tente novamente")
        inicio()

inicio()