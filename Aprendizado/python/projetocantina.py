item = ["Salgado", "Sanduiche", "Refrigerante", "Suco", "Água"]
preço = [6, 8, 5, 4, 3]
compra = []
def inicio():
    print("========CANTINA========")
    print("1 - Fazer pedido")
    print("2 - Consultar cardápio")
    print("3 - Sair")
    print("=======================")
    resp = int(input("Escolha uma das opções acima:"))
    match resp:
        case 1:
            pedido()
        case 2:
            cardapio()
        case 3:
            exit

def pedido():
    print("Digite o código correspondente ao seu pedido:")
    

def cardapio():
    for i in range(len(item)):
        print(f" {i} - {item[i]:<25} Preço: R$: {preço[i]}")
        
inicio()