import inputs



def menu_calculadora():
    print('')
    print('escolha uma opçao')
    print('1 - soma')
    print('2 - subtraçao')
    print('3 - diviçao')
    print('4 - multiplicaçao')
    
     
        
def soma(num1,num2):
    return num1 + num2
def subtraçao(num1,num2):
    return num1 - num2
def diviçao(num1,num2):
    return num1  / num2
def multiplicaçao(num1,num2):
    return num1 * num2

def operaçao_em_geral():
    print('a soma é igual a',1)
    print('a subtraçao é igual ', 2)
    print('a diviçao é igual a ', 3)
    print('a multiplicaçao é igual a',4)

    
menu_calculadora()


operaçao = inputs.input_int('Digite uma opção')
        
         
num1 = inputs.input_int(('digite um numero'))
       
num2 = inputs.input_int(('digite outro numero '))
          
    
if operaçao == 1:
    print(soma(num1,num2))
elif  operaçao == 2:
    print(subtraçao (num1,num2))
elif  operaçao == 3:
    print(diviçao (num1,num2))
elif  operaçao == 4:
    print(multiplicaçao (num1,num2))
    
    



            

     
