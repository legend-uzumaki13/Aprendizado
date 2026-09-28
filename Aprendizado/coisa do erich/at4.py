def verificarNumero(n):
    if n == 0:
        print("esse número é zero")
    elif n > 0:
        print("este número é positivo")
    else:
        print("Este número é negativo")

n = int(input("Digite um número: "))
verificarNumero(n)