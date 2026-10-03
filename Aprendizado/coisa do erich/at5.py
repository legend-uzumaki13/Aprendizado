def verificarNumero(a, b):
    if a == b:
        print("Ambos são iguais")
    elif a > b:
        print(f"{a} é maior que {b}")
    else:
        print(f"{b} é maior que {a}")

a = int(input("Digite um número: "))
b = int(input("Digite mais um número: "))

verificarNumero(a, b)