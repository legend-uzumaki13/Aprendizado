def mostrarSaudacao():
    print("Seja Bem Vindo!!!")
    nome = input("digite seu nome: ")
    saudacao(nome)

def saudacao(nome):
    print(f"olá, {nome}")

for i in range(3):
    mostrarSaudacao()