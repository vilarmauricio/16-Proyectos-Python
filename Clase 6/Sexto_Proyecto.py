'''Proyecto: Administrador de recetas.

crear directorio de carpeta:
Recetas: Carnes: (Entrecort al Malbec.txt, Matambre a la Pizza.txt)
	 Ensaladas: (Ensalada Griega.txt, Ensalada Mediterranea.txt)
	 Pastas: (Canelones de ESpinaca.txt, Ravioles de Ricotta.txt)
	 Postres: (Compota de manzana.txt, Tarta de Frambueza.TXT)

-Saludo de Bienvenida
-Mostrar Directorio donde se encuetran las Recetas
-Cantidad de Recetas disponibles

Menu:
[1] Leer Receta -> Elegir categoria -> Mostrar Recetas -> Elegir Receta - Leer Receta
[2] Crear Receta -> Elegir Categoria -> Nombre Receta -> Contenido Receta
[3] Crear Categoria -> Nombre Categoria -> Crear Carpeta
[4] Eliminar Receta ->Idem Opcion 1 Pero Elimina
[5] Eliminar Categoria -> Elimina Categoria
[6] Finalizar Programa

usar while para repetir menu
usar system('cls') para limpiar pantalla'''

from os import system
from pathlib import Path
import shutil


def menu():
    eleccion = 0
    valor_incorrecto = False
    system('cls')
    print('''\t ***  Menu Recetario  *** \n  
        Seleccionar una Opcion:
            [1] Leer Receta   
            [2] Crear Receta
            [3] Crear Categoria
            [4] Eliminar Receta
            [5] Eliminar Categoria
            [6] Salir del Programa  ''')
    while eleccion not in ['1','2','3','4','5','6']:
        if valor_incorrecto == True:
            system('cls')
            print('''\t ***  Menu Recetario  *** \n 
        Seleccionar una Opcion:
            [1] Leer Receta   
            [2] Crear Receta
            [3] Crear Categoria
            [4] Eliminar Receta
            [5] Eliminar Categoria
            [6] Salir del Programa  ''')
            print('Ha ingresado un valor incorrecto. Vuelva a ingresar un Valor')
        eleccion = input('Ingresa la Opcion: ')
        if eleccion not in ['1','2','3','4','5','6']: valor_incorrecto = True

    else: return eleccion

def mostrar_categorias():
    system('cls')
    categoria = ''
    valor_incorrecto = False
    directorio = Path('Recetas')
    lista_categoria = [fichero.name for fichero in directorio.iterdir() if fichero.is_dir()]
    
    print('Categorias:')
    #mostrar carpetas    
    for cat in lista_categoria:
        print('\t-',cat)

    while categoria not in lista_categoria:
        if valor_incorrecto == True:
            system('cls')
            print('Categorias:')
            #mostrar carpetas
            for cat in lista_categoria:
                print('\t-',cat)
            print('Ingreso un valor incorrecto.')
        categoria = input('Ingrese el nombre de la Categoria o "s" para volver: ')
        if categoria not in lista_categoria: valor_incorrecto = True
        if categoria == 's': break
        
    return categoria

def mostrar_recetas(categoria):
    system('cls')
    receta = ''
    valor_incorrecto = False
    archivos = Path('Recetas', categoria)
    lista_receta = [fichero.name for fichero in archivos.iterdir() if fichero.is_file()]
    print(f'{categoria}: \n\tRecetas:')
    for rec in lista_receta:
        print('\t\t-', rec)
    while receta not in lista_receta:
        if valor_incorrecto == True:
            system('cls')
            print(f'{categoria}: \n\tRecetas:')
            #mostrar carpetas
            for rec in lista_receta:
                print('\t-',rec)
            print('Ingreso un valor incorrecto.')
        receta = input('Ingrese el nombre de la Receta o "s" para volver: ')
        if receta not in lista_receta: valor_incorrecto = True
        if receta == 's': break
        
    return receta

def leer_receta(categoria, receta):
    ruta = Path('Recetas',categoria, receta)
    archivo = ruta.open()
    system('cls')
    print('Receta:',receta, '\n')
    print(archivo.read())
    print('\nFin de la Receta!')
    input('Precione Enter para continuar')

def crear_receta(categoria):
    nombre_receta = input('Escribe el nombre de la receta: ') + '.txt'
    myfile = Path('Recetas', categoria, nombre_receta)
    myfile.touch(exist_ok=True)
    f = open(myfile, 'a')
    contenido = input('Introduce el contenido: ')
    f.write(contenido)
    f.close()
    
def crear_categoria():
    nombre_categoria = input('Ingresa el nombre de la nueva categoria: ')
    path = Path('Recetas', nombre_categoria)
    path.mkdir(parents=True, exist_ok=True)

def eliminar_receta(categoria):
    archivos = Path('Recetas', categoria)
    lista_receta = [fichero.name for fichero in archivos.iterdir() if fichero.is_file()]
    print(f'{categoria}: \n\tRecetas:')
    for rec in lista_receta:
        print('\t\t-', rec)
    nombre_receta = input('Escribe el nombre de la receta: ') + '.txt'
    
    myfile = Path('Recetas', categoria, nombre_receta)
    myfile.unlink(missing_ok= True)

def eliminar_categoria(categoria):
    directorio = Path('Recetas', categoria)
    shutil.rmtree(directorio)

#programa principal
opcion = '1'
while(opcion in ['1', '2', '3', '4', '5']):    
    opcion = menu()
    if opcion == '1':
        categoria = mostrar_categorias()
        if categoria == 's' or categoria == 'S': continue
        receta = mostrar_recetas(categoria)
        if receta == 's' or receta == 'S': continue
        leer_receta(categoria, receta)
    elif opcion == '2':
        categoria = mostrar_categorias()
        if categoria == 's' or categoria == 'S': continue
        crear_receta(categoria)
    elif opcion == '3':
        crear_categoria()
        
    elif opcion == '4':
        categoria = mostrar_categorias()
        if categoria == 's' or categoria == 'S': continue
        eliminar_receta(categoria)
        
    elif opcion == '5':
        categoria = mostrar_categorias()
        if categoria == 's' or categoria == 'S': continue
        eliminar_categoria(categoria)
        

if opcion == '6': print('Muchas Gracias por utilizar este Programa. Buen Provecho!! :-)')