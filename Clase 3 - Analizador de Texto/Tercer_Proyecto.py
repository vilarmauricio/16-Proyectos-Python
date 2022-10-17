

'''ingresar un Text
insertrar 3 Letras
1 cuantas veces aparecen las letras en mayusculs y minusculas
2 cantidad de palabras
3 primer letra del texto y URLSafeTimedSerializer
4 texto en orden inverso
5 python se encuentra en el texto'''

# Creamos el parrafo
texto = 'La casa esta, en llamas. Python'
print('\nParrafo: ', texto, '\n')
# Creamos variables con letra en minuscula a buscar
a = 'a'
b = 'm'
c = 's'

# Contamos tanto minusculas como mayuculas
cantidad_A = texto.count(a) + texto.count(a.upper())
cantidad_B = texto.count(b) + texto.count(b.upper())
cantidad_C = texto.count(c) + texto.count(c.upper())

print(f'Letra buscada: {a}, cantidad de apariciones: {cantidad_A}')
print(f'Letra buscada: {b}, cantidad de apariciones: {cantidad_B}')
print(f'Letra buscada: {c}, cantidad de apariciones: {cantidad_C}')

# Contamos cantidad de palabras
cantidad_palabras = texto.split() 
#print(cantidad_palabras)
print('\nCantidad de palabras: ', len(cantidad_palabras))

primer_letra = texto[0]
ultima_letra = texto[-1]

print('\nPrimer Caracter del parrafo:', primer_letra)
print('Ultimo Caracter del parrafo:', ultima_letra)

# Texto orden inverso
cantidad_palabras.reverse()
print('\nTexto inverso:', cantidad_palabras)

# Encontrar palabra
palabra = 'Python'
print(f'\nLa palabra "Python" se encuentra en el parrafo?  {palabra in texto}\n')