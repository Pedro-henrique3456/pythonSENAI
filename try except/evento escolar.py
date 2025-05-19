import inputs




lista = []

while True:
    print("")
    print("menu de opções")
    print("1 - cadastrar um nome")
    print("2 - exibir o total de inscritos")
    print("3 - exibir a lista de nomes em ordem alfabética")
    print("4 - permitir a consulta de um nome")
    print("5 - sair")
    opcao = inputs.input_int(("Digite sua escolha"))

    print("")

    if opcao == 1:

        nome = inputs.input_str("digite o nome que deseja cadastrar:")

        if nome in lista:

            print("nome cadastrado")

        else:

            lista.append(nome)

            print("nome cadastrado ")

    elif opcao == 2:

        print("o total de inscritos foram", len(lista))

    elif opcao == 3:

        for nome in lista:

            print(nome)

    elif opcao == 4:

        nome = inputs.inputs_str("digite seu nome que deseja consultar")

        if nome in lista:

            vari = inputs.inputs_int("nome encontrado com sucesso , você deseja remover da lista? s/n ")

            if vari == "s":

                lista.remove(nome)

                print("nome retirado com sucesso")

            elif nome1 == "n":

                print("o nome ainda permanece na lista")

        else:

            nome1 = inputs.inputs_str("nome não encontrado, deseja adiciona-lo? s/n")

            if nome1 == "s":

                lista.append(nome)

                print("o nome foi adicionado à lista")

            elif  nome1 == "n":

                print("ok")

            else:

                print("opção inesistente")

    elif opcao == 5:

        print("você saiu")

        break

    else:

        print("opção inesistente")
 
