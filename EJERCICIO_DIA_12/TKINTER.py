from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

# operador
operador = ''

# precios 
precios_comida = [1.32, 1.65, 2.32, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postre = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

# funcionalidad a las teclas de la calculadora
def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)

# función borrar (b)
def borrar():
    global operador 
    operador = ''
    visor_calculadora.delete(0, END)

# función de total en calculadora
def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = resultado

# funcion revisar check
def revisar_check():

    # revisar check comida
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == 0:
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1
    
    # revisar check bebida
    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == 0: 
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1

    # revisar check postre
    x = 0
    for c in cuadros_postre:
        if variables_postre[x].get() == 1:
            cuadros_postre[x].config(state=NORMAL)
            if cuadros_postre[x].get() == 0:
                cuadros_postre[x].delete(0, END)
            cuadros_postre[x].focus()
        else:
            cuadros_postre[x].config(state=DISABLED)
            texto_postre[x].set('0')
        x += 1

# función total
def total():

    # total para la comida
    sub_total_comida = 0
    p = 0

    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1
        

    # total para la bebida
    sub_total_bebida = 0
    p = 0

    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1
    

        # total para el postre
    sub_total_postre = 0
    p = 0

    for cantidad in texto_postre:
        sub_total_postre = sub_total_postre + (float(cantidad.get()) * precios_postre[p])
        p += 1
    

    #sub_total
    sub_total = sub_total_comida + sub_total_bebida + sub_total_postre

    # impuesto
    impuesto = sub_total * 0.07
    total = sub_total + impuesto
    
    # para las comidas
    var_costo_comida.set(f'$ {round(sub_total_comida, 2)}')
    var_costo_bebida.set(f'$ {round(sub_total_bebida, 2)}')
    var_costo_postre.set(f'$ {round(sub_total_postre, 2)}')

    # para el sub total
    var_subtotal.set(f'$ {round(sub_total, 2)}')

    # para el impuesto 
    var_impuesto.set(f'$ {round(impuesto, 2)}')

    # para el total
    var_total.set(f'$ {round(total, 2)}')

# función recibo
def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos: \t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 63 + '\n')
    texto_recibo.insert(END, f'Items \t\tCant\tCost Items\n')
    texto_recibo.insert(END, f'-' * 75 + '\n')

    # factura para comida
    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t'
                                    f'${round(int(comida.get()) * precios_comida[x], 2)}\n')
        x += 1

    # factura para bebida
    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t'
                                    f'${round(int(bebida.get()) * precios_bebida[x], 2)}\n')
        x += 1

    # factura para postre
    x = 0
    for postre in texto_postre:
        if postre.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postre.get()}\t'
                                    f'${round(int(postre.get()) * precios_postre[x], 2)}\n')
        x += 1

    # factura totalizada
    texto_recibo.insert(END, f'-' * 75 + '\n')
    texto_recibo.insert(END, f' Costo de la comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f' Costo de la bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f' Costo de la postre: \t\t\t{var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'-' * 75 + '\n')

    # Factura totalizada completa
    texto_recibo.insert(END, f' Subtotal: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f' Impuesto: \t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f' Total: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'-' * 75 + '\n')

    # despedida
    texto_recibo.insert(END, 'Lo esperamos pronto')

# función de guardar
def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)

    archivo.close()

    messagebox.showinfo('Información', "Su recibo se ha guardado")

# función recetear
def recetear():
    texto_recibo.delete(0.1, END)

    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postre:
        texto.set('0')
    
    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postre:
        cuadro.config(state=DISABLED)
    
    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postre:
        v.set(0)
    
    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')

# iniciar tkinter
aplicacion = Tk()


# tamaño de la ventana
aplicacion.geometry('1020x620+0+0')

# evitar maximizar
aplicacion.resizable(0, 0)

# titulo de la venta
aplicacion.title('Mi RESTAURANTE - FACTURACIÓN')

# colo de fondo
aplicacion.config(bg='burlywood')

# panel superior
panel_superior = Frame(aplicacion, bd=1, relief= FLAT)
panel_superior.pack(side=TOP)

# etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturación', fg= 'azure4',
                        font=('Dosis', 49), bg='burlywood', width=27)

etiqueta_titulo.grid(row= 0, column=0)

# panel izquierdo
panel_izqueierdo = Frame(aplicacion, bd=1, relief= FLAT, pady=72)
panel_izqueierdo.pack(side=LEFT)

# panel costos
panel_costos = Frame(panel_izqueierdo, bd=1, relief= FLAT, bg='azure4', padx=41)
panel_costos.pack(side=BOTTOM)

# panel comidas
panel_comidas = LabelFrame(panel_izqueierdo, text= 'Comidas', font= ('Dosis', 15, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

# panel bebidas 
panel_bebidas = LabelFrame(panel_izqueierdo, text= 'Bebidas', font= ('Dosis', 15, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

# panel postres
panel_postres = LabelFrame(panel_izqueierdo, text= 'Postres', font= ('Dosis', 15, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)


# panel derecha
panel_derecho = Frame(aplicacion, bd=1, relief= FLAT)
panel_derecho.pack(side=RIGHT)

# panel calculadora
panel_calculadora = Frame(panel_derecho, bd=1, relief= FLAT, bg= 'burlywood')
panel_calculadora.pack(side=TOP)

# panel recibo
panel_recibo = Frame(panel_derecho, bd=1, relief= FLAT, bg= 'burlywood')
panel_recibo.pack()

# panel Botones
panel_botones = Frame(panel_derecho, bd=1, relief= FLAT, bg= 'burlywood')
panel_botones.pack(side=BOTTOM)

# listas de productos
lista_comidas = ['Pollo', 'Res', 'Cerdo', 'Salmon', 'Pizza 1', 'Pizza 2', 'Kebab', 'Pizza 3']
lista_bebidas = ['Agua', 'Soda', 'Juago 1', 'Jugos 2', 'Gaseosas', 'Vino', 'Cerveza', 'Sake']
lista_postres = ['Helado', 'Brownies', 'Flan', 'Pastel 1', 'Pastel 2', 'Muffin', 'Cherry', 'Arequipe']

# generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []


contador = 0
for comida in lista_comidas:


    # check Button comida
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, 
                         text=comida.title(), 
                         font=('Dosis', 15, 'bold',),
                         onvalue=1 , 
                         offvalue=0, 
                         variable=variables_comida[contador],
                         command=revisar_check)
    comida.grid(row=contador, 
                column=0, 
                sticky="w")


    # cuadros de entrada comida
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                   font=('Dosis', 15, 'bold'),
                                   bd=1,
                                   width=6,
                                   state=DISABLED,
                                   textvariable= texto_comida[contador])
    
    cuadros_comida[contador].grid(row=contador,
                                  column=1)



    contador += 1

# generar items bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []

contador = 0
for bebida in lista_bebidas:

    # check Button bebida 
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, 
                         text=bebida.title(), 
                         font=('Dosis', 15, 'bold'),
                         onvalue=1 , 
                         offvalue=0, 
                         variable=variables_bebida[contador],
                         command=revisar_check)
    bebida.grid(row=contador, 
                column=0, 
                sticky="w")
    

    # cuadros de entrada bebidas
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')

    cuadros_bebida[contador] = Entry(panel_bebidas,
                                   font=('Dosis', 15, 'bold'),
                                   bd=1,
                                   width=6,
                                   state=DISABLED,
                                   textvariable= texto_bebida[contador])
    
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)
    

    contador += 1

# generar items postre
variables_postre = []
cuadros_postre = []
texto_postre = []

contador = 0
for postre in lista_postres:

    # check Button postre 
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres, 
                         text=postre.title(), 
                         font=('Dosis', 15, 'bold'),
                         onvalue=1 , 
                         offvalue=0, 
                         variable=variables_postre[contador],
                         command=revisar_check)
    postre.grid(row=contador,
                column=0, 
                sticky="w")
    

    # cuadros de entrada postre
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')

    cuadros_postre[contador] = Entry(panel_postres,
                                   font=('Dosis', 15, 'bold'),
                                   bd=1,
                                   width=6,
                                   state=DISABLED,
                                   textvariable= texto_postre[contador])
    
    cuadros_postre[contador].grid(row=contador,
                                  column=1)

   
    contador += 1

# lista variables comida
var_costo_comida = StringVar()
# lista variables comida
var_costo_bebida = StringVar()
# lista variables postre
var_costo_postre = StringVar()

var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# estiquetas de costo y campos de entrada de comida 
etiqueta_costos_comida = Label(panel_costos,
                               text='Costo comida',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_costos_comida.grid(row=0, column=0)

# Entrada comida 
texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)

texto_costo_comida.grid(row=0, column=1)


# estiquetas de costo y campos de entrada de bebida 
etiqueta_costos_bebida = Label(panel_costos,
                               text='Costo bebida',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_costos_bebida.grid(row=1, column=0)

# Entrada bebida
texto_costo_bebida= Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)

texto_costo_bebida.grid(row=1, column=1)


# estiquetas de costo y campos de entrada de postre 
etiqueta_costos_postre = Label(panel_costos,
                               text='Costo postre',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_costos_postre.grid(row=2, column=0)

# Entrada postre
texto_costo_postre= Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postre)

texto_costo_postre.grid(row=2, column=1)

# subtotal
etiqueta_subtotal = Label(panel_costos,
                               text='Subtotal',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_subtotal.grid(row=0, column=2, padx=41)

# Entrada subtotal
texto_subtotal= Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

# impuesto
etiqueta_impuesto = Label(panel_costos,
                               text='Impuesto',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_impuesto.grid(row=1, column=2, padx=41)

# Entrada impuesto
texto_impuesto= Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_impuesto)
texto_impuesto.grid(row=1, column=3, padx=41)

# Total
etiqueta_total = Label(panel_costos,
                               text='Total',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_total.grid(row=2, column=2, padx=41)

# Entrada impuesto
texto_total= Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)

# botones
botones = ['Total', 'Recibo', 'Guardar', 'Recetear']
botones_creados = []
columnas = 0

for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 13, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)
    botones_creados.append(boton)
    
    boton.grid(row=0,
               column=columnas)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=recetear)


# area de recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=42,
                    height=10)
texto_recibo.grid(row=0,
                  column=0)

# calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 14, 'bold'),
                          width=32,
                          bd=1)
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

# botones calculadora
botones_calculadora = ['7','8','9','+',
                       '4','5','6','-',
                       '1','2','3','x',
                       '=','b','0','/']
botones_guardados = []

fila = 1
columna = 0

for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis', 14, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=8)
    botones_guardados.append(boton)

    boton.grid(row=fila,
               column=columna)
    
    if columna == 3:
        fila += 1
    
    columna += 1

    if columna == 4:
        columna = 0

# funcionalidad a los botones de la calculadora
botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))


# evitar que la pantalla se cierre
aplicacion.mainloop()
