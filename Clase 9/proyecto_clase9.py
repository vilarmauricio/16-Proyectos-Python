import shutil
import os


ruta = 'C:\\Users\\Mauricio\\Desktop\\PythonTotal\\Clase 9\\Proyecto Día 9.zip'
archivo = 'Proyecto Día 9.zip' 
shutil.unpack_archive(ruta, 'Practica Dia 9', 'zip')

directorio = os.walk('Practica Dia 9')

for carpeta in directorio:
    print('Carpeta : ', carpeta, 'Archivo: ', archivo)
    