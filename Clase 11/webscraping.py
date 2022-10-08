import bs4
import requests

# Obtenemos la busqueda con requests.get
resultado =  requests.get('https://escueladirecta-blog.blogspot.com/2022/10/el-modulo-secreto-de-python.html')

#print(resultado.text)

# Hacemos identificacion (pharsing) de elementos con bs4

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

# Buscamos por nombre de etiqueta, nos trae como lista
print(sopa.select('title'))

# traemos solo el texto de la lista sin etiquetas
print(sopa.select('title')[0].getText())