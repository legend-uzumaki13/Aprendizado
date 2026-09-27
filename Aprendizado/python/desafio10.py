import time

Alunonome = []
Alunonota = []
funcionando = True
media = 0

def vernome(nome, i):
    correto = False
    if nome in Alunonome:
        print("O nome do aluno já foi cadastrado, digite outro nome")
        nome = (input("Digite o nome correto: "))
        vernome(nome, i)
    else:
        while correto != True:
            try:
                nome = str(nome)
                print(nome)
                if isinstance(nome, str) and len(nome) >= 3 and nome.isalpha():
                        correto = True
                        Alunonome.append(nome)
                        return Alunonome[i]
                        
                else:

                    print("O nome do aluno deve conter 3 ou mais letras, e não deve conter números")
                    nome = (input("Digite o nome correto: "))
                    
            except ValueError:
                continue
                        

def vernum(i):
    while Alunonota[i] < 0 or Alunonota[i] > 100:
        print("Nota inválida, digite uma nota entre 0 e 100")
        Alunonota[i] = float(input("Digite: "))
        
        
def cadastro():
    resp = "Y"
    contador = 2
    i = 0
    while True:
        nome = (str.lower(input("Digite o nome do Aluno: ")))
        vernome(nome, i)
                
        Alunonota.append(float(input("Agora digite a nota desse aluno: ")))
        vernum(i)
        i += 1          
        resp = input("Deseja cadastrar mais um aluno? [Y/n]")
        if resp == "n":
            break
        else:
            
            continue
        
            
def listar():
    for i in range(len(Alunonome)):
        print(i + 1 , "-" , Alunonome[i])
        
def pesquisa():
    resp = "Y"
    
    if len(Alunonome) < 1:
        print("Nenhum aluno foi cadastrado")
        time.sleep(1.5)
        
    else:
        while resp != "n":    
            busca = str.lower(input("Digite o nome do Aluno: "))
            encontrado = False
            
            for i in range(len(Alunonome)):
                if busca == Alunonome[i]:
                    print("O aluno", busca , "tem a nota de:", Alunonota[i])
                    resp_alterar = str.lower(input("Deseja alterar a nota desse aluno? [y/N]: "))
                    if resp_alterar == "y":
                        Alunonota[i] = float(input("Digite a nova nota: "))
                        vernum(i)
                        print("Nota alterada com sucesso!")
                    encontrado = True
                    break
                    
                
            else:
                print("O aluno", busca, "não está cadastrado no sistema")
                
            resp = input("deseja pesquisar outro aluno? [Y/n]")
            if resp == "n":
                break
            else:
                continue
        

def media():
    media = 0
    if len(Alunonome) < 1:
        print("Você ainda não cadastrou nenhum aluno...")
        time.sleep(1.5)
    
    else:
        for i in range(len(Alunonota)):
            media = Alunonota[i] + media
            
        print("a média da turma é de", media / len(Alunonota))
        time.sleep(1.5)


while funcionando == True:
        try:
            print("=============SISTEMA DE ALUNOS==============")
            print("1 - Cadastrar Aluno")
            print("2 - Listar Alunos")
            print("3 - Pesquisar Aluno")
            print("4 - Calcular média da turma")
            print("0 - Sair")
            print("============================================")
    
            escolha = int(input("Selecione uma opção: "))
            match escolha:
                case 0:
                    print("Saindo...")
                    break
        
                case 1:
                    cadastro()
        
                case 2:
                    listar()

                case 3:
                    pesquisa()
                
                case 4:
                    media()
                                       
        except ValueError:
            print("Resposta inválida, tente novamente.")
            time.sleep(1)
            continue