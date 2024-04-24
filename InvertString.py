def inverte_string(s):
    str_invertida = ''
    for caracter in s:
        str_invertida = caracter + str_invertida
    return str_invertida

s = input("Digite uma string: ")
resultado = inverte_string(s)
print("A string invertida é:", resultado)
