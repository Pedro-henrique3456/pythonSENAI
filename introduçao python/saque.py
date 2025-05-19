# Definir o saldo inicial 
saldo = 10000.0 
 
# Função para verificar o saldo 
def verificar_saldo(): 
    print(f"Seu saldo atual é: R${saldo:.2f}") 
 
# Função para sacar dinheiro 
def sacar_dinheiro(valor): 
    global saldo 
    if valor > 0 and valor <= saldo: 
        saldo -= valor 
        print(f"Saque de R${valor:.2f} realizado com sucesso.") 
    else: 
        print("Saque não realizado. Verifique o valor ou seu saldo.") 
 
# Função para depositar dinheiro 
def depositar_dinheiro(valor): 
    global saldo 
    if valor > 0: 
        saldo += valor 
        print(f"Depósito de R${valor:.2f} realizado com sucesso.") 
    else: 
        print("Depósito não realizado. Verifique o valor.") 
 
# Menu do caixa eletrônico 
while True: 
    print("\nCaixa Eletrônico") 
    print("1. Verificar o seu saldo") 
    print("2. Sacar seu dinheiro") 
    print("3. Depositar seu dinheiro") 
    print("4. Sair") 
    opcao = input("Digite a sua opçao q deseja : ") 
 
    if opcao == "1": 
        verificar_saldo() 
    elif opcao == "2": 
        valor = float(input("Digite o valor para sacar: ")) 
        sacar_dinheiro(valor) 
    elif opcao == "3": 
        valor = float(input("Digite o valor para depositar: ")) 
        depositar_dinheiro(valor) 
    elif opcao == "4": 
        print("Obrigado por usar o caixa eletrônico.") 
        break 
    else: 
        print("Opção inválida. Por favor, tente novamente.") 