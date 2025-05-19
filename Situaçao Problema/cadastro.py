pais_inscritos = []
pais_presentes = []
pais_ausentes = []


while True:
    print("")
    print("menu de opções")
    print("1 - cadastrar nome dos pais")
    print("2 - exibir o total de pais")
    print("3 - exbir a lista de nomes em ordem alfabéticas")
    print("4 - realizar a confirmaçao de presença dos pais")
    print("5 - exibir um relatorio da chamadas")
    print("6 - sair")
    op = int(input("Digite sua escolha"))
    
    print("")
    
    if op == 1:
    
        inscriçao = input("digite o nome que deseja cadastrar :")
        
        if inscriçao in pais_inscritos:
            
            print("nome dos pais cadastrado")
            
        else:
            pais_inscritos.append(inscritos)
            
            print("nome dos pais cadastrado")
        