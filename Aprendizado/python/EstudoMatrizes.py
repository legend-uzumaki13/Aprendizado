mat = []
Dprin = []
import time

def confirmador():
    try:
        resp = str(input("Deseja continuar? [Y/n] "))
    except ValueError:
        resp = "Y"
    if resp != "n":
        inicio()
     
            
def receber():
    for l in range(4):
        linha = []
        for c in range(4):
            try:
                linha.append(int(input(f"Digite um número para a linha {l + 1}, e coluna {c + 1}: ")))
            except ValueError:
                linha.append(0)
        mat.append(linha)
    return(mat)


def inicio():
    print("====================================")
    print("1 - Mostrar a Matriz")
    print("2 - Diagonal Principal")
    print("3 - Triangulo Superior")
    print("4 - Triangulo Inferior")
    print("5 - Sair")

    try:  
        resp = int(input("Escolha uma alternativa: "))
            
        match resp:
            case 1:
                Mostrar(mat)
            
            case 2:
                MDprin(mat)
            
            case 3:
                triangulos(mat, resp)
                
            case 4:
                triangulos(mat, resp)
                
            case 5:
                print("Saindo... ")

    except ValueError:
        print("Valor inválido digitado, tente novamente:")
        time.sleep(0.5)
        inicio()


def Mostrar(mat):
    for l in range(4):
        for c in range(4):
            print(f"{mat[l][c]:02d}" , end=" ")
        print("")
    confirmador()


def MDprin(mat):
    if Dprin:
        for i in range(len(Dprin)):
            print(Dprin[i], end=", ") 
    else:  
        for l in range(4):
            linha = []
            for c in range(4):
                if c == l:
                    Dprin.append(mat[c] [l])
        for i in range(len(Dprin)):
            print(Dprin[i], end=", ")
    confirmador()

def triangulos(mat, resp):
    TS = []
    TI = []
    for l in range(4):
        for c in range(4):
            if c > l:
                TS.append(mat[l] [c])
            elif l > c:
                TI.append(mat[l] [c])
            else:
                continue

    if resp == 3:
        for i in range(len(TS)):
            print(TS[i], end=", ")
    if resp == 4:
        for i in range(len(TI)):
            print(TI[i], end=", ")
    confirmador()
receber()
inicio()