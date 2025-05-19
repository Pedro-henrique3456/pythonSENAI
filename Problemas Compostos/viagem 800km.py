# passo a passo

# 1 - exibir quantos litros de combustível e quantos reais é preciso pra fazer uma viagem de 800 km

# 2 - o carro tem 10 litros no tanque, ja percorreu 90 km, o combustível custa R$6,90, o carro tem autonomia de 7 km por litro

# 3
#1 descobrir quantos litros de combustivel é preciso pra viagem
#2 descobrir quantos reais é preciso pra fazer a viagem

n1 = int(input('Quantos km ainda falta percorrer:'))
n2 = int(input('Digite quantos km por litro é gasto:'))
c1 = n1 / n2
print('Vai precisar de =',c1, 'litros')
n3 = float(input('Digite o preço da gasolina:'))
c2 = c1 * n3
print('O preço total foi:',c2,'reais')
