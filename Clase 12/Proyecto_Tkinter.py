from tkinter import *
from tkinter.tix import ROW

# Iniciamos Tkinter
app = Tk()

#Tamaño de la ventana
app.geometry('1150x720+200+20')

# evitar maximizar
app.resizable(0,0)

# titulo de la ventana
app.title('Mi Restaurante - v1.0')

# color de Fondo
app.config(bg= 'burlywood')

# panel superiror
panel_superior = Frame(app, bd= 1, relief= FLAT ) # Creamos un panel dentro de app
panel_superior.pack(side = TOP) # Ubicamos el panel en la parte superior

# etiqueta titulo
etiqueta_titulo = Label(panel_superior, 
                        text= 'Modulo Ventas',
                        fg= 'azure4',
                        font= ('Dosis', 58),
                        bg= 'burlywood',
                        width= 25) #Creacion de la etiqueta
etiqueta_titulo.grid(row= 0, column= 0) #Ubicacion dentro del panel superior

# panel izquierdo
panel_izquierdo = Frame(app, bd= 1, relief= FLAT)
panel_izquierdo.pack(side= LEFT)

# Panel Costos
panel_costos = Frame(panel_izquierdo, bd= 1, relief= FLAT, bg= 'azure4', padx= 55)
panel_costos.pack(side= BOTTOM)

# Panel Comidas
panel_comidas = LabelFrame(panel_izquierdo,
                            text= 'Comida',
                            font= ('Dosis', 19, 'bold'),
                            bd= 1,
                            relief= FLAT,
                            fg= 'azure4')
panel_comidas.pack(side= LEFT)

# Panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo,
                            text= 'Bebida',
                            font= ('Dosis', 19, 'bold'),
                            bd= 1,
                            relief= FLAT,
                            fg= 'azure4')
panel_bebidas.pack(side= LEFT)

# Panel Postres
panel_postres = LabelFrame(panel_izquierdo,
                            text= 'Postre',
                            font= ('Dosis', 19, 'bold'),
                            bd= 1,
                            relief= FLAT,
                            fg= 'azure4')
panel_postres.pack(side= LEFT)

# panel derecha
panel_derecha = Frame(app, bd= 1, relief= FLAT)
panel_derecha.pack(side= RIGHT)

# panel calculadora
panel_calculadora = Frame(panel_derecha, bd= 1, relief= FLAT, bg= 'burlywood')
panel_calculadora.pack()

# panel recibo
panel_recibo = Frame(panel_derecha, bd= 1, relief= FLAT, bg= 'burlywood')
panel_recibo.pack()

# panel botones
panel_botones = Frame(panel_derecha, bd= 1, relief= FLAT, bg= 'burlywood')
panel_botones.pack()

# lista productos
lista_comidas = ['Pollo', 'Cordero', 'Salmon', 'Merluza', 'Kebab', 'Pizza1', 'Pizza2', 'Pizza3']
lista_bebidas = ['Agua', 'Coca', 'Sprite', 'Cerveza A', 'Cerveza B', 'Vino A', 'Vino B', 'Soda']
lista_postres = ['Helado', 'Fruta', 'Flan', 'Tiramizu', 'Budin', 'Torta', 'Postre1', 'Postre2']

# Generar items comidas
variables_comida = []
cuadros_comida = []
texto_comida = []
contador= 0
for comida in lista_comidas:

    # crear checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                        text= comida.title(),
                        font=('Dosis', 19, 'bold'),
                         onvalue= 1,
                         offvalue= 0,
                         variable= variables_comida[contador])
    comida.grid(row= contador, 
                column= 0, 
                sticky= W)
    

    # crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar() #seteamos en cero los valores de los cuadros de texto
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                    font=('Dosis', 18, 'bold'),
                                    bd= 1,
                                    width= 6,
                                    state= DISABLED,
                                    textvariable= texto_comida[contador])
    cuadros_comida[contador].grid(row= contador,
                                column= 1)

    contador += 1

# Generar items bebidas
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador= 0
for bebida in lista_bebidas:
    
    # crear bebidas checkbutton
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                        text= bebida.title(),
                        font=('Dosis', 19, 'bold'),
                         onvalue= 1,
                         offvalue= 0,
                         variable= variables_bebida[contador])
    bebida.grid(row= contador, column= 0, sticky= W)
    
    # crear los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar() #seteamos en cero los valores de los cuadros de texto
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                    font=('Dosis', 18, 'bold'),
                                    bd= 1,
                                    width= 6,
                                    state= DISABLED,
                                    textvariable= texto_bebida[contador])
    cuadros_bebida[contador].grid(row= contador,
                                column= 1)

    contador += 1

# Generar items postres
variables_postre = []
cuadros_postre = []
texto_postre = []
contador= 0
for postre in lista_postres:
    
    # crear checkbutton
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres,
                        text= postre.title(),
                        font=('Dosis', 19, 'bold'),
                         onvalue= 1,
                         offvalue= 0,
                         variable= variables_postre[contador])
    postre.grid(row= contador, column= 0, sticky= W)
    
    # crear los cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar() #seteamos en cero los valores de los cuadros de texto
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres,
                                    font=('Dosis', 18, 'bold'),
                                    bd= 1,
                                    width= 6,
                                    state= DISABLED,
                                    textvariable= texto_postre[contador])
    cuadros_postre[contador].grid(row= contador,
                                column= 1)

    contador += 1

# variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()


# etiquetas de costo y campos de entrada
etiqueta_costo_comida = Label(panel_costos,
                            text= 'Costo Comida',
                            font= ('Dosis', 12, 'bold'),
                            bg= 'azure4',
                            fg= 'white')
etiqueta_costo_comida.grid(row= 0,
                            column= 0)

texto_costo_comida = Entry(panel_costos,
                            font= ('Dosis', 12, 'bold'),
                            bd= 1,
                            width= 10,
                            state= 'readonly',
                            textvariable= var_costo_comida)
texto_costo_comida.grid(row= 0,
                        column= 1, 
                        padx= 41)

# etiquetas de costo bebida y campos de entrada
etiqueta_costo_bebida = Label(panel_costos,
                            text= 'Costo Bebida',
                            font= ('Dosis', 12, 'bold'),
                            bg= 'azure4',
                            fg= 'white')
etiqueta_costo_bebida.grid(row= 1,
                            column= 0)

texto_costo_bebida = Entry(panel_costos,
                            font= ('Dosis', 12, 'bold'),
                            bd= 1,
                            width= 10,
                            state= 'readonly',
                            textvariable= var_costo_bebida)
texto_costo_bebida.grid(row= 1,
                        column= 1, 
                        padx= 41)

# etiquetas de costo  postre y campos de entrada
etiqueta_costo_postre = Label(panel_costos,
                            text= 'Costo Postre',
                            font= ('Dosis', 12, 'bold'),
                            bg= 'azure4',
                            fg= 'white')
etiqueta_costo_postre.grid(row= 2,
                            column= 0)

texto_costo_postre = Entry(panel_costos,
                            font= ('Dosis', 12, 'bold'),
                            bd= 1,
                            width= 10,
                            state= 'readonly',
                            textvariable= var_costo_postre)
texto_costo_postre.grid(row= 2,
                        column= 1, 
                        padx= 41)

# etiquetas de subtotal y campos de entrada
etiqueta_subtotal = Label(panel_costos,
                            text= 'Subtotal',
                            font= ('Dosis', 12, 'bold'),
                            bg= 'azure4',
                            fg= 'white')
etiqueta_subtotal.grid(row= 0,
                            column= 2)

texto_subtotal = Entry(panel_costos,
                            font= ('Dosis', 12, 'bold'),
                            bd= 1,
                            width= 10,
                            state= 'readonly',
                            textvariable= var_subtotal)
texto_subtotal.grid(row= 0,
                    column= 3, 
                    padx= 41)

# etiquetas de impuesto y campos de entrada
etiqueta_impuesto = Label(panel_costos,
                            text= 'Impuesto',
                            font= ('Dosis', 12, 'bold'),
                            bg= 'azure4',
                            fg= 'white')
etiqueta_impuesto.grid(row= 1,
                            column= 2, 
                            )

texto_impuesto = Entry(panel_costos,
                            font= ('Dosis', 12, 'bold'),
                            bd= 1,
                            width= 10,
                            state= 'readonly',
                            textvariable= var_impuesto)
texto_impuesto.grid(row= 1,
                    column= 3, 
                    padx= 41)

# etiquetas de total y campos de entrada
etiqueta_costo_total = Label(panel_costos,
                            text= 'TOTAL',
                            font= ('Dosis', 12, 'bold'),
                            bg= 'azure4',
                            fg= 'white')
etiqueta_costo_total.grid(row= 2,
                            column= 2, 
                            )

texto_total = Entry(panel_costos,
                            font= ('Dosis', 12, 'bold'),
                            bd= 1,
                            width= 10,
                            state= 'readonly',
                            textvariable= var_total)
texto_total.grid(row= 2,
                column= 3, 
                padx= 41)

# botones
botones = ['Total', 'Recibo', 'Guardar', 'Reset']
columna = 0
for boton in botones:
    boton = Button(panel_botones,
                    text= boton.title(),
                    font= ('Dosis', 14, 'bold'),
                    fg= 'white',
                    bg= 'azure4',
                    bd= 1,
                    width= 9)
    boton.grid(row= 0,
                column= columna)
    columna += 1

# Area de recibo
texto_recibo = Text(panel_recibo,
                    font= ('Dosis', 12, 'bold'),
                    bd= 1,
                    width= 50,
                    height= 10)
texto_recibo.grid(row= 0, column= 0)
    
# calculadora
botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', 'x', 'CE', 'Borrar', '0', '/']

visor_calculadora = Entry(panel_calculadora,
                        font= ('Dosis', 18, 'bold'),
                        width= 35,
                        bd= 1)
visor_calculadora.grid(row=0,
                        column= 0,
                        columnspan=4)

fila=1
columnas= 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                    text= boton.title(),
                    font= ('Dosis', 16, 'bold'),
                    fg= 'white',
                    bg= 'azure4',
                    bd= 1,
                    width= 8)
    boton.grid(row= fila,
                column= columnas)

    if columnas == 3:
        fila += 1

    columnas +=1

    if columnas == 4:
        columnas = 0









# Evitamos que la ventana e cierre
app.mainloop()
