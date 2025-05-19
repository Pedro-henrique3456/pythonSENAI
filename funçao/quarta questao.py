def circulo(raio):
    return 3.14 * raio **2
   
def quadrado(num1):
    return num1 * num1
   
def retangulo(num1,num2):
    return num1 * num2
   
def menu_area():
    print("[1] circulo")
    print("[2] quadrado")
    print("[3] retângulo")
   
    opcao = int(input("escolha uma opcao: "))
   
    if opcao == 1:
        raio = float(input("digite o raio do circulo: "))
        print("área do circulo = ",circulo(raio))
       
    elif opcao == 2 :
        lado = float(input("digite o lado do quadrado: "))
        print("área do quadrado = ", quadrado(lado))
       
    elif opcao == 3 :
        base = float(input("digite a base do retangulo: "))
        altura = float(input("digite a altura do retangulo"))
        print("área do retângulo = ", retangulo(base, altura))
       
menu_area()
