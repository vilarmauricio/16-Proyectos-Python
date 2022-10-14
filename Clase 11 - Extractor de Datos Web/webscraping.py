import bs4
import requests
import pandas as pd

# creamos url de las paginas
url_base = 'http://books.toscrape.com/catalogue/page-{}.html'

# Creamos lista vacia para guardar los libros
lista_libros_top = []

# Bucle para itinerar en cada pagina
for num in range(1, 51):
    
    # Obtenenoms Html de la pagina
    pagina = requests.get(url_base.format(num))
    
    # Ordenamos Html
    sopa = bs4.BeautifulSoup(pagina.text, 'lxml')

    # Obtenemos los datos de los libros que se encuentran dentro de una clase
    libros = sopa.select('.product_pod')

    # Itineramos en la lista obtenida de datos de los libros

    for libro in libros:

        # Condicion de Seleccion
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            titulo = libro.select('a')[1]['title']
            precio = libro.select('p')[1].getText()[2:]
            lista_libros_top.append([titulo, precio]) 

df = pd.DataFrame(lista_libros_top, columns= ['titulo', 'precio'])
df.to_csv('./libros_top.csv', index= False)