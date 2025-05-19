def input_str(mensagem="digite qualquer coisa"):
    while True:
        nome = str(input(mensagem))
        
        if not nome.isalpha():
            print('digite apenas letras')
            
        else:
            return nome
        
def input_int(mensagem="Digite um numero"):
    while True:
        try:
            valor =int(input(mensagem))
            return valor
        except ValueError:
                print("invalido")
      
        

        
def input_float(mensagem="digite o numero"):
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        
        except ValueError:
                print("erro")
        
        
        