#passo a passo

#calcule o preço do produto


#1 solicite um nome de qualquer produto e solicite seu preço

#2descobrir o nome do produto
#solicitar o preço do produto
#descobrir o desconto de 5%

#3
#passo1: multiplique o preço do produto por 5
#passo2: divida os resultados por 100
#passo3: exiba o novo preço do produto e quanto ele diminuiu


produto = input(" nome do produto ")
preço = float(input('qual o preço do produto'))
cupom1 = preço * 5
cupom2 = cupom1 / 100
print('o preço com cupom sera de ', cupom2)
print('preço do produto com desconto é', preço - cupom2)
