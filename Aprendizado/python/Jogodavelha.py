contador = int(1)
x = True
jogo = []
contador = 0

linha1 = [1, 2, 3]
linha2 = [4, 5, 6]
linha3 = [7, 8, 9]

jogo.append(linha1)
jogo.append(linha2)
jogo.append(linha3)

def l1(resp, x, vez):
    l = 0
    checador(resp, jogo, l)
    if che
    if vez == 1:
        jogo[l] [resp - 1] = "X"
    else:
        jogo[l] [resp - 1] = "O"
    return linha1
    
def l2(resp, x, vez):
    l = 1
    if vez == 1:
        jogo[l] [resp - 4] = "X"
    else:
        jogo[l] [resp - 4] = "O"
    return linha2

def l3(resp, x, vez):
    l = 2
    if vez == 1:
        jogo[l] [resp - 7] = "X"
    else:
        jogo[l] [resp - 7] = "O"
    return linha3
       
def checador(resp, jogo, l):
    for c in range(len(jogo)):
        if jogo[c] == "X" or "O":
            jogo[l] [resp] = ("jogada inválida, digite outra posição: ")
        
def inicio(linha1, linha2, linha3):
    global contador
    vez = contador % 2
    print(contador)
    if vez == 1:
        x = True
        o = False

    else:
        x = False
        o = True
    
    match x:
        case True:
            print("X, Selecione uma casa:")
            print(f"[{linha1[0]}] [{linha1[1]}] [{linha1[2]}]")
            print(f"[{linha2[0]}] [{linha2[1]}] [{linha2[2]}]")
            print(f"[{linha3[0]}] [{linha3[1]}] [{linha3[2]}]")
            
            resp = int(input())
        
        case False:
            print("O, Selecione uma casa:")
            print(f"[{linha1[0]}] [{linha1[1]}] [{linha1[2]}]")
            print(f"[{linha2[0]}] [{linha2[1]}] [{linha2[2]}]")
            print(f"[{linha3[0]}] [{linha3[1]}] [{linha3[2]}]")
            
            resp = int(input())
    contador += 1
    resposta(resp, vez)
    return resp, vez


def resposta(resp, vez):
    match resp:
        case 1:
            l1(resp, x, vez) 
        case 2:
            l1(resp, x, vez)
        case 3:
            l1(resp, x, vez)
        case 4:
            l2(resp, x, vez)
        case 5:
            l2(resp, x, vez)
        case 6:
            l2(resp, x, vez)
        case 7:
            l3(resp, x, vez)
        case 8:
            l3(resp, x, vez)
        case 9:
            l3(resp, x, vez)

while True:
    inicio(linha1, linha2, linha3)