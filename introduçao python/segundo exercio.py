from datetime import datetime

def tempratura_kelvin (celsius):
    return celsius + 273

def temperatura_fahrenheit (celsius):
    return celsius * 1.8 + 32

temperatura = int(input('exiba'))

print('fahrenheit_grau',temperatura_fahrenheit (temperatura))
print('kelvin_grau',tempratura_kelvin (temperatura))
