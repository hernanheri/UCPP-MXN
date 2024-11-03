import random
import string

def generar_texto(longitud):
    resultado = []
    for _ in range(longitud):
        tipo = random.choice(['numero', 'mayuscula', 'minuscula'])
        if tipo == 'numero':
            resultado.append(str(random.randint(0, 9)))
        elif tipo == 'mayuscula':
            resultado.append(random.choice(string.ascii_uppercase))
        elif tipo == 'minuscula':
            resultado.append(random.choice(string.ascii_lowercase))
    return ''.join(resultado)

def generar_varios_textos(cantidad, longitud):
    textos = []
    for _ in range(cantidad):
        textos.append(generar_texto(longitud))
    return textos

# Configura la cantidad de textos y la longitud de cada uno
cantidad_textos = 1000000
longitud_texto = 10

# Genera los textos aleatorios
textos_aleatorios = generar_varios_textos(cantidad_textos, longitud_texto)

# Guardar los textos en un archivo de texto
with open("textos_aleatorios.txt", "w") as archivo:
    for texto in textos_aleatorios:
        archivo.write(texto + "\n")

print("Los textos aleatorios se han guardado en 'textos_aleatorios.txt'")
