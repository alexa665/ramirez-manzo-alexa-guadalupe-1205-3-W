print(" ")
print("alexa guadalupe ramirez manzo 1205 3-W")
print(" ")
diccionario = {} #diccionario
def llenar_diccionario(entrada): #como llenar el diccionario
    pares = entrada.split(',')
    for par in pares:
        try:
            español, ingles = par.split(':')
            diccionario[español.strip()] = ingles.strip()
        except ValueError:
            print(f"Error al procesar el par: '{par}'. Asegúrate de usar el formato correcto.") #sirve para imprimir el error
entrada = input("Introduce las palabras en español e inglés (ejemplo: hola:hello, adiós:goodbye): ")# Solicita palabras al usuario
llenar_diccionario(entrada)
frase = input("Introduce una frase en español para traducir: ")#frace en español
palabras = frase.split()
frase_traducida = [] #traduce la frace
for palabra in palabras:
    traduccion = diccionario.get(palabra, palabra)  #mantiene la palabra si no se encuentra
    frase_traducida.append(traduccion)
print("Frase traducida:", ' '.join(frase_traducida))# Mostrar la frase traducida


