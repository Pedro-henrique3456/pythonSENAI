from datetime import datetime

def mostrar_nome (nome):
    hora = datetime.now().hour
    
    if hora > 00 and hora <= 5:
        print('boa madrugada', nome)
    
    elif hora > 5 and hora <= 12:
        print('bom dia', nome)
    
    elif hora > 12 and hora <= 19:
        print('boa tarde', nome)
    
    elif hora > 19 and hora <= 23:
        print('boa noite', nome)
        
pessoa = input('digite seu nome ')

mostrar_nome (pessoa)
   



    
    
    
    
    