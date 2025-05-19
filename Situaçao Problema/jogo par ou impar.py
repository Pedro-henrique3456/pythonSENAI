import random

print('Ola, jogador seja bem vindo vamo começar?"\033[mTeste\033[m (padrão do terminal)"')

pc = random.randint(1,10)

while True:
    print("PAR OU IMPAR")
    print("")
    print("[1]-impar")
    print("[2]-par")
    print("[3]- sair")
    ia = int(input("numero de [0-2]"))
    
    if ia  == 1:
        num =print('vocé é impar')
        print('seu adiversario escolheu par')
        num1 = int(input('escolha um numero de 1 a 10 ='))
        sominha = num1 + pc
        if sominha % 2 == 0:
             print('vocé perdeu',)
             print('seu adiversario escolheu', pc)
             print('resultado = ', sominha)
        else: 
            print( 'DEU IMPAR')
            print('GANHOU JOGADOR' ,sominha)
            
            print('oponente escolheu', pc )
            print('resu',sominha)
            
    elif ia == 2:   
        num = print('vocé é par')
        print('seu adiversario escolheu impar')
        num1 = int(input('esconha um numero de 1 a 10 ='))
        sominha = num1 + pc
        if sominha % 2 == 0:
            print('deu par')
            print('GANHOU!')
            print('o adiversario escolheu', pc)
            print('resu deu ', sominha)
        else:
            print("Seu jogo deu Impar")
            print("VOCÊ PERDEU!!!", soma)
                     
        



    
    
    
    
    
    
    

        
        