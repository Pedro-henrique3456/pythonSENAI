#------------ Dicionarario -------------

#criar
aluno = {
    "nome": "pedro",
    "idade": 17,
    "altura": 1.75,
    "matriculado": True

}
carro ={
     "nome": "civic",
     "marca": "honda",
     "motor": 1.5, 
     "cv" : 173,  
}    
carro2 ={
    "nome": "gtr",
    "marca": "nissan",
    "motor": "v6 biturbo",
    "cv" : 600
    
}   

carro3 ={
    "nome" : "supra",
    "marca" : "toyota",
    "motor" :"motor de seis cilindros",
    "cv" : 387,
    
}    


#print(aluno)

#adicionar campo
aluno["peso"] = 68

#print(aluno)

#altera campo
aluno["idade"]= 18

#print(aluno)

#deletar o campo
del aluno["altura"]
#print(aluno)

#verificar
if "altura" in aluno:
    print("altura existente")
else :
    print("altura inexcistente")
    
#exibir
for chave,valor in aluno.items():
    print(f"{chave}: {valor}")
    
#exibir uma lista de dicionario
lista_carros = [carro,carro2,carro3]

    
    # Escolha dos campos
for carro in lista_carros:
    print(f"{carro['marca']}")
    
    
    #exibindo todos
for carro in lista_carros:
    for chave,valor in carro.items():
        print(f"{chave} - {valor}")
    print()
    
    
    
    





