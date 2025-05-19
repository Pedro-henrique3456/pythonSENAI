
def calcular_imc(peso, altura):
    return peso / altura**2

altura = float(input("Digite seu altura "))
peso = float(input("Digite sua peso "))

def classificaçao_imc(imc):
    if imc <= 18.5:
        print("Magreza")
   
    elif imc > 18.5 and imc <= 24.9:
        print("Normal")

    elif imc > 25 and imc <= 29.9:
        print("Sobrepeso")
   
    elif imc > 30 and imc <= 34.9:
        print("Obesidade grau I")

    elif imc > 35 and imc <= 39.9:
        print("Obesidade grau II")
   
    elif imc > 40 :
        print("Obesidade grau III")
   
imc = calcular_imc(peso, altura)
classificaçao_imc(imc)




    
    
