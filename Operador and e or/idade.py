an = int(input('Digite o ano do seu nascimento'))
aa = int(input('Digite o ano atual'))
if an >= 1908 and an <= 2025 and an > 0 and an <= 2025:
    idade = aa - an
    print('A idade é =', idade)
    if idade <= 10:
        print('Você é criança')
    elif idade == 11 or idade <= 17:
        print('Você é adolescente')
    elif idade == 18 or idade <=59:
        print('Você é adulto')
    elif idade >= 60 and idade <=117:
        print('parabens vc é o mais velho da terra')
else:
    print('Você não esta vivo')
    idade = aa - an
    print('A idade é =', idade,'anos')






