n = []
for i in range(10):
    try:
        n.append(int(input("Enter a number: ")))
    except ValueError:
        print("Entrada inválida, por favor tente novamente.")
sum = 0
for i in n:
    sum += i
    
print("A soma dos seguintes números: ", n, " equivale a: ", sum)