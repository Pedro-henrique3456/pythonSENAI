

t1 = int(input("digite lado do triangulo"))
t2 = int(input("digite lado do triangulo"))
t3 = int(input("digite lado do triangulo"))

if t1 == t2 and t3 == t2:
    print("equilatero")
   
   
elif t1 != t2 and t3 == t2 or t1 == t2 and t3 != t2 or t1 == t2 and t1 != t3:
    print("isosceles")
   
   
elif t1 != t2 and t3 != t2:
    print("escaleno")
