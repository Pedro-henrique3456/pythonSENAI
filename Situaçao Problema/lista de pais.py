pais_inscritos = []
pais_presentes = []
pais_ausentes = []

while True:
    print("")
    print("Menu de opções")
    print("1 - Cadastrar nome dos pais")
    print("2 - Exibir o total de pais")
    print("3 - Exibir a lista de nomes em ordem alfabética")
    print("4 - Realizar a confirmação de presença dos pais")
    print("5 - Exibir um relatório das chamadas")
    print("6 - Sair")
    
    op = int(input("Digite sua escolha: "))
    
    print("")
    
    if op == 1:
        nome = input("Digite o nome que deseja cadastrar: ")
        
        if nome in pais_inscritos:
            print("Nome já cadastrado.")
        else:
            pais_inscritos.append(nome)
            print("Nome cadastrado com sucesso.")
            
    elif op == 2:
        print("O total de inscritos foi de", len(pais_inscritos), "pessoas.")
        
    elif op == 3:
        pais_inscritos.sort()
        for nome in pais_inscritos:
            print(nome)
           
    elif op == 4:
        pais_presentes = []
        pais_ausentes = []
        
        for nome in pais_inscritos:
            pergunta = input(nome + " está presente? (s/n): ")
            if pergunta == "s":
                pais_presentes.append(nome)
            elif pergunta == "n":
                pais_ausentes.append(nome)
                
    elif op == 5:
        print("Relatório de presença:")
        for nome in pais_presentes:
            print("Presente:", nome)
        for nome in pais_ausentes:
            print("Ausente:", nome)
            
    elif op == 6:
        print("Fechando o programa.")
        break