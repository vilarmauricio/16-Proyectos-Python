from secrets import choice

def iniciar(nombre):
    print(f'Hola {nombre}, te desfio a jugar al ahorcado\n debes adivinar las letras de la palabra incognita\n solo puedes equivocarte {vidas} veces\n')

def elegir_palabra(incognita):
    return choice(incognita)

def crear_guiones(palabra):
    return ' _ ' * len(palabra)

def modificar_guiones(letra, palabra, guiones):
    for indice, valor in enumerate(palabra):
        if valor == letra:
            guiones[indice] = letra
    return guiones
    



    


lista_palabras = ['PAJARO', 'PERRO', 'CONEJO', 'ELEFANTE', 'JIRAFA', 'AVESTRUZ']
palabra_incognita = elegir_palabra(lista_palabras)
vidas = 5
guiones = crear_guiones(palabra_incognita)
nombre = input('Bienvenido! Dime tu nombre: ')
iniciar(nombre)
print('" ', guiones, ' "')
guiones = guiones.split()

while (vidas > 0):
    letra = input('Ingresa una letra: ').upper()
    if letra in palabra_incognita:
        guiones = modificar_guiones(letra, palabra_incognita, guiones)
        
    else:   
        vidas -= 1
        print(f'Letra incorrecta, te quedan {vidas} VIDAS')
    print('"', ' '.join(guiones), '"')
    if '_' not in guiones:
        print(f'MUY BIEN {nombre}, HAS GANADO!!')
        break
if vidas == 0:
    print(f'Lo siento {nombre}, has perdido. La palabra era "{palabra_incognita}".')
