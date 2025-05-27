lista1 = []

while True:
    print("")
    print("MENU")
    print("[1] - Cadastrar livros")
    print("[2] - Exibir lista")
    print("[3] - Quantidade de livros")
    print("[4] - Títulos cadastrados")
    print("[5] - Buscar por autor")
    print("[6] - Buscar por categoria")
    print("[7] - Editar dados")
    print("[0] - Sair")
    op = int(input("digite sua opeçao"))

    if op == 0:
        print("SAINDO..")
        time.sleep(2)
        print("FIM.")
        break
    elif op == 1:
        nome_autor = input("Digite o nome do autor do livro: ")
        titulo = input("Digite o título do livro: ")
        isbn = input("Digite o código (isbn): ")
        categoria = input("Qual a categoria do livro: ")
        ano_publicaçao = input("Digite o Ano de lançamento: ")
        livro = {
            "titulo": titulo,
            "Autor": nome_autor,
            "ISBN": isbn,
            "Categoria": categoria,
            "Ano": ano_publicaçao
        }
        print("")
        lista1.append(livro)
        continuar = input("Deseja continuar? (s/n): ")
        if continuar == "n":
            print("FIM!")
            break
        else:
            continue
    elif op == 2:
        for ordem1 in lista1:
            for chave, valor in ordem1.items():
                print(f' {chave}:  {valor}')
            print("")
       
   
    elif op == 3:
        quantidade = len(lista1)
        print(quantidade, "livros na lista")
        
     
           
    elif op == 4:
        print("Títulos cadastrados:")
        for escolha in lista1:
            print(f"{escolha['titulo']}")
      
   
    elif op == 5:
        autor = input("Digite o autor desejado: ")
        livros_encontrados = [livro for livro in lista1 if livro['Autor'] == autor]
        if livros_encontrados:
            print('Livros encontrados:')
            for livro in livros_encontrados:
                    print(f"- {livro['titulo']} (isbn: {livro['isbn']})")
         
   
    elif op == 6:
        categoria = input("Digite a categoria desejada: ")
        livros_encontrados = [livro for livro in lista1 if livro['Categoria'] == categoria]
        if livros_encontrados:
            print('Livros encontrados nesta categoria:')
            for livro in livros_encontrados:
                print(f"- {livro['titulo']} (Autor: {livro['Autor']}, isbn: {livro['isbn']})")
            

    elif op == 7:
        isbn_editar = input("Digite o isbn do livro que deseja editar: ")
        for livro in lista1:
            if livro['ISBN'] == isbn_editar:
                print("LIVRO ENCONTRADO!. Faça as alterações:")
                livro['titulo'] = input("Digite o novo título: ")
                livro['Autor'] = input("Digite o novo autor: ")
                livro['Categoria'] = input("Digite a nova categoria: ")
                livro['Ano'] = input("Digite o novo ano de lançamento: ")
                print("DADOS ENCONTRADOS!")
                break
        else:
            print("Livro não encontrado!")
            continuar = input("Deseja continuar? (s/n): ")
            if continuar == "n":
                print("FIM!")
                break
            else:
                continue

   

