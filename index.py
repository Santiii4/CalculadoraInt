from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from tkinter import *




# PARTE MATEMATICA



def Derivar():
    try:
        x = symbols('x')
        fun_escrita = funcion.get()
        f = parse_expr(fun_escrita)
        derivada = diff(f, x)
        etiqueta.configure(text=derivada)
    except:
        etiqueta.configure(text="Introduce la función correctamente")

def Integrales_Indefinidas():
    try:
        x = symbols('x')
        fun_escrita2 = funcion.get()
        g = parse_expr(fun_escrita2)
        integral = integrate(g, x)
        etiqueta.configure(text=integral)
    except:
        etiqueta.configure(text="Introduce la función correctamente")

def Integrales_Definidas():
    try:
        x = symbols('x')
        fun_escrita3 = funcion.get()
        g = parse_expr(fun_escrita3)
        limite_inf = float(input("Ingrese el límite inferior: "))
        limite_sup = float(input("Ingrese el límite superior: "))
        integral_definida = integrate(g, (x, limite_inf, limite_sup))
        etiqueta.configure(text=integral_definida)
    except:
        etiqueta.configure(text="Introduce la función correctamente")



# PARTE GRAFICA



ventana = Tk()
ventana.geometry('400x350')
ventana.title("Cálculo Diferencial e Integral: f(x)")

anuncio = Label(ventana, text="Introduce una función de x:", font=("Arial", 15), fg="blue")
anuncio.pack()

funcion = Entry(ventana, font=("Arial", 15))
funcion.pack()

etiqueta = Label(ventana, text="Resultado", font=("Arial", 15), fg="red")
etiqueta.pack()

boton1 = Button(ventana, text="Derivar Función", font=("Arial", 15), command=Derivar)
boton1.pack()

boton2 = Button(ventana, text="Integrar Función (Indefinida)", font=("Arial", 15), command=Integrales_Indefinidas)
boton2.pack()

boton3 = Button(ventana, text="Integrar Función (Definida)", font=("Arial", 15), command=Integrales_Definidas)
boton3.pack()

ventana.mainloop()

# 3*x**2+4*x**2