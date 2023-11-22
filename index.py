from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from tkinter import *



# PARTE MATEMATICA



def Derivar():
    try:
        x = symbols('x')
        fun_escrita = funcion.get()
        f = parse_expr(fun_escrita)
        derivada = diff(f,x)
        etiqueta.configure(text=derivada)
    except:
        etiqueta.configure(text="Introduce la función correctamente")
        
        
def Integrar():
    try:
        x = symbols('x')
        fun_escrita2 = funcion.get()
        g = parse_expr(fun_escrita2)
        integral = integrate(g,x)
        etiqueta.configure(text=integral)
    except:
        etiqueta.configure(text="Introduce la función correctamente")




# PARTE GRAFICA



ventana = Tk()
ventana.geometry('400x280')
ventana.title("Cálculo Diferencial e Integral: f(x)")

anuncio = Label(ventana, text="Introduce una función de x:", font=("Arial", 15), fg="blue")
anuncio.pack()

funcion = Entry(ventana, font=("Arial", 15))
funcion.pack()

etiqueta = Label(ventana, text="Resultado", font=("Arial", 15), fg="red")
etiqueta.pack()

boton1 = Button(ventana, text="Derivar Función", font=("Arial", 15), command=Derivar)
boton1.pack()

boton2 = Button(ventana, text="Integrar Función", font=("Arial", 15), command=Integrar)
boton2.pack()

ventana.mainloop()