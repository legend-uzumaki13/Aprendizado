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

a = int(input("Digite um número: "))
b = int(input("Digite mais um número: "))

print(f"A soma equivale a: {som(a, b)}, a subtração equivale a: {sub(a, b)}, a Multiplicação equivale a: {mult(a, b)} e a Divisão equivale a: {div(a, b)}")
