import time
times = []

def fatorial(quantia):
    contador = 0
    i = 0
    while True:
        i += 1
        fatorialres = 1
        for x in range(i):
            while quantia > contador:
                fator = quantia - contador
                fatorialres *= fator 
                contador += 1
                print(fatorialres)
        return fatorialres

def combinacao():
    i = int(input("Digite a quantidade de itens para combinar: "))
    k = 0
    c = 0
    x = 0
    while i > 0:
        i -= 1
        times.append((str(input("Digite os itens para combinar: "))))
    while k < len(times):
        time1 = times[k]
        k += 1
        for x in range(len(times)):
            time2 = times[x]

            if time1 != time2:
                c += 1
                print(f"Combinação {c}: {time1} e {time2}")
            else:
                continue

combinacao()
