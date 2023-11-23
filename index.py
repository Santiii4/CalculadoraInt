from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np




# PARTE MATEMATICA



def Derivar():
    try:
        x = symbols('x')
        funcion_escrita = funcion.get()
        f = parse_expr(funcion_escrita)
        derivada = diff(f, x)
        etiqueta.configure(text=derivada)

        plot_grafico(f, derivada)
    
    except:
        etiqueta.configure(text="Introduce la función correctamente")

def Integrales_Indefinidas():
    try:
        x = symbols('x')
        funcion_escrita2 = funcion.get()
        g = parse_expr(funcion_escrita2)
        integral = integrate(g, x)
        etiqueta.configure(text=integral)

        plot_grafico(g)

    except:
        etiqueta.configure(text="Introduce la función correctamente")

def Integrales_Definidas():
    try:
        x = symbols('x')
        funcion_escrita3 = funcion.get()
        g = parse_expr(funcion_escrita3)
        limite_inferior = float(input("Límite inferior: "))
        limite_superior = float(input("Límite superior: "))
        integral_definida = integrate(g, (x, limite_inferior, limite_superior))
        etiqueta.configure(text=integral_definida)

        plot_grafico(g, limite_inferior, limite_superior)

    except:
        etiqueta.configure(text="Introduce la función correctamente")

def plot_grafico(f, limite_inf=None, limite_sup=None):
    x_vals = np.linspace(-10, 10, 400)
    y_vals = [f.evalf(subs={'x': x_val}) for x_val in x_vals]

    plt.figure()
    plt.plot(x_vals, y_vals, label='f(x)')

    if limite_inf is not None and limite_sup is not None:
        plt.axvline(x=limite_inf, color='r', linestyle='--', label='Límite Inferior')
        plt.axvline(x=limite_sup, color='g', linestyle='--', label='Límite Superior')

    plt.title('Gráfico de la Función')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()



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
# raiz cuadrada = sqrt()