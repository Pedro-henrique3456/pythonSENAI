#construa um programa que calcule quanto custa para encher o tanque de um carro que tem 50 de capacidade ele estando com 20
 
#1 o objetivo é criar um sistema que calcule quanto falta para completar um tanque de um carro de 50 litros
# o carro está com 20 litros

#2 é necessario calcular a diferença entre 50 e 20
#    para calcular o valor entre 20 e 50


#3
#passo1 subtrair 50 por 20
#passo2 multiplicar a o resultado por 5,80
#passo3 exibir o resultado


t1 = int(input(	" digite a capacidade do tanque"))
t2 = int(input(" digite quanto tem no tanque"))
resultado = t1 - t2
gasolina = float(input("digite o preço"))
print(" o resultado é", resultado * gasolina)