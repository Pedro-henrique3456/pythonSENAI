gran  = 0
quant = 0

while True:
    print("selecione o menu desejado")
    print("")
    print("[1] Adicionar o valor da despesa")
    print("[2] mostrar quantidade e valor total das despesas")
    print("[0] sair")
    num = input("solicite um numero de [0-2]")


    if num == "1":
        gasto = int(input("valor gasto"))
        print(gasto, "reais")
        gran = gran + gasto
        quant += 1
    elif num == "2":
        print(gran ,'reais')
        print('quantidade de despesas=',quant)
    elif num == "0":
        print("sair")
        break 