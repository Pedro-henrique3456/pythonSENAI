#etapa 1 
objetos = ["lapis","estojo","borracha","garrafa","colher"]

print("")

#ETAPA2
objetos.append ("caneta")
print("objeto adicionado foi ", objetos [1] )

print("")

#etapa 3
v = objetos[1]
print(v)

print("")

#etapa 4
v1 = objetos.pop(2)
print(v1)

print("")

#etapa 5
v2 = len (objetos)
print(v2)

print("")

#etapa 6 
for item in objetos:
    print(item)
    
print("")
print("")

#etapa 7
if "cadeira" in objetos:
    objetos.remove ("cadeira")
    print('cadeira removida')
else:
    objetos.append("cadeira")
    print("cadeira adicionada")
    
print("")
print("")

#etapa 8
print(objetos)
objetos . sort()

#etapa 9
primeira = objetos[0]
ultimo = objetos [-1]
print("primeira item é :" , primeira)
print("o ultimo item é :", ultimo)

print("")
#etapa 10 

objetos.clear()
print("lista vazia")




