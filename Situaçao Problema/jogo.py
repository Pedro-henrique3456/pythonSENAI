import random 
pc = random.randint(0,100)
print('Olá, sou seu computador... Escolhi um numero de 0 a 100')
print('Tente adivinhar')
correto = False
while True: 
    voce = int(input('Digite seu numero: '))
    if voce == pc:
        print('Seu resultado está correto e seu numero é  ',pc)
        escolha = int(input('voce deseja continuar?'))
        break
    elif voce > pc:
        print('O numero é menor que',voce)
    elif voce < pc:
        print('O seu numero é maior que ',voce)