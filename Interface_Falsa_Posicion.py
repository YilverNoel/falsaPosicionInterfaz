from tkinter import *#libreria para poder usar la interfaz grafica 
from tkinter import ttk
from tkinter import font#para poder usar las fuentes
from math import *#libreria para usar funciones matematicas
import numpy as np#libreria para vectorizar
import matplotlib.pyplot as plt #libreria para poder graficar funciones matematicas

raiz=Tk()#creamos la raiz de la interfaz 
raiz.title("MÉTODO DE LA FALSA POSICIÓN")
tituloLabel=Label(raiz,text="Método De La Falsa Posición", font = ("Arial", 18, "bold"), bg = "#e3553d", fg = "#E6E9ED", width = "250", height = "2")
tituloLabel.pack()
miFrame=Frame(raiz, width=950, height=550)#agregamos un lienzo a nuestra raiz 
miFrame.pack()

#globales(valores ingresados por el usuario

funcionX=StringVar()
valorXl=DoubleVar()
valorXu=DoubleVar()
valorTolerancia=DoubleVar()
respuestaTxt=StringVar()
operacion=""




#--creacion de etiquetas y cajas de texto--

funcionLabel=Label(miFrame, text="Función f(x):",  font = ("Arial", 12, "bold"))
funcionLabel.place(x=110, y=50)

cuadroFuncion=Entry(miFrame, textvariable=funcionX, font = ("Arial", 14, "italic"))
cuadroFuncion.place(x=230, y=50, width=250, height=30)

xlLabel=Label(miFrame, text="Intervalo XL:",  font = ("Arial", 12, "bold") )
xlLabel.place(x=110, y=100)

cuadroXl=Entry(miFrame, textvariable=valorXl, font = ("Arial", 10, "bold"))
cuadroXl.place(x=230, y=100, height=30)

xuLabel=Label(miFrame, text="Intervalo XU:",  font = ("Arial", 12, "bold"))
xuLabel.place(x=110, y=150)

cuadroXu=Entry(miFrame,textvariable=valorXu, font = ("Arial", 10, "bold"))
cuadroXu.place(x=230, y=150, height=30)

toleranciaLabel=Label(miFrame, text="Tolerancia:",  font = ("Arial", 12, "bold"))
toleranciaLabel.place(x=110, y=200)

cuadroTolerancia=Entry(miFrame, textvariable=valorTolerancia, font = ("Arial", 10, "bold"))
cuadroTolerancia.place(x=230, y=200,height=30)

respuestaLabel=Label(miFrame, textvariable=respuestaTxt, font = ("", 12, "italic") )
respuestaLabel.place(x=120,y=545)

#-botones para el panel de ayuda--
def numeroPulsado(num):

	global operacion

	if operacion!="":

		funcionX.set(num)
		operacion=""


	else:

		funcionX.set(funcionX.get()+num)

#--primera fila de los botones auxiliares--
botonSen=Button(miFrame, text="sin(x)",font = ("Arial", 12, "bold"),  bg="#434A54",  fg = "#E6E9ED",width=4, relief="raised", borderwidth=5, command=lambda:numeroPulsado("sin(x)"))
botonSen.place(x=680, y=50)


botonCos=Button(miFrame, text="cos(x)",font = ("Arial", 12, "bold"),  bg="#434A54",  fg = "#E6E9ED",width=4, relief="raised", borderwidth=5, command=lambda:numeroPulsado("cos(x)"))
botonCos.place(x=740, y=50)

botonTan=Button(miFrame, text="tan(x)",font = ("Arial", 12, "bold"),  bg="#434A54",  fg = "#E6E9ED",width=4, relief="raised", borderwidth=5, command=lambda:numeroPulsado("tan(x)"))
botonTan.place(x=800, y=50)

#----segunda fila de botones auxiliares --
botonLn=Button(miFrame, text="ln(x)",font = ("Arial", 12, "bold"),  bg="#434A54",  fg = "#E6E9ED",width=4, relief="raised", borderwidth=5, command=lambda:numeroPulsado("log(x)"))
botonLn.place(x=680, y=100)


botonE=Button(miFrame, text="e",font = ("Arial", 12, "bold"),  bg="#434A54",  fg = "#E6E9ED",width=4, relief="raised", borderwidth=5, command=lambda:numeroPulsado("e"))
botonE.place(x=740, y=100)

botonTanPot=Button(miFrame, text="^",font = ("Arial", 12, "bold"),  bg="#434A54",  fg = "#E6E9ED",width=4, relief="raised", borderwidth=5, command=lambda:numeroPulsado("**"))
botonTanPot.place(x=800, y=100)
#---tercera fila botones auxiliares-
botonX=Button(miFrame, text="x^(2)",font = ("Arial", 12, "bold"),  bg="#434A54",  fg = "#E6E9ED",width=4, relief="raised", borderwidth=5, command=lambda:numeroPulsado("x**(2)"))
botonX.place(x=680, y=150)


botonEx=Button(miFrame, text="e^(x)",font = ("Arial", 12, "bold"),  bg="#434A54",  fg = "#E6E9ED",width=4, relief="raised", borderwidth=5, command=lambda:numeroPulsado("e**(x)"))
botonEx.place(x=740, y=150)

botonTanPi=Button(miFrame, text="π",font = ("Arial", 12, "bold"),  bg="#434A54",  fg = "#E6E9ED",width=4, relief="raised", borderwidth=5, command=lambda:numeroPulsado("pi"))
botonTanPi.place(x=800, y=150)

#----cuarta fila de botones auxiliares-
botonPor=Button(miFrame, text="x",font = ("Arial", 12, "bold"),  bg="#434A54",  fg = "#E6E9ED",width=4, relief="raised", borderwidth=5, command=lambda:numeroPulsado("*"))
botonPor.place(x=680, y=200)


botonDiv=Button(miFrame, text="/",font = ("Arial", 12, "bold"),  bg="#434A54",  fg = "#E6E9ED",width=4, relief="raised", borderwidth=5, command=lambda:numeroPulsado("/"))
botonDiv.place(x=740, y=200)

botonMas=Button(miFrame, text="+",font = ("Arial", 12, "bold"),  bg="#434A54",  fg = "#E6E9ED",width=4, relief="raised", borderwidth=5, command=lambda:numeroPulsado("+"))
botonMas.place(x=800, y=200)
	
#-----quinta fila de botones auxiliares-
botonMenos=Button(miFrame, text="-",font = ("Arial", 12, "bold"),  bg="#434A54",  fg = "#E6E9ED",width=4, relief="raised", borderwidth=5, command=lambda:numeroPulsado("-"))
botonMenos.place(x=680, y=250)


botonRaiz=Button(miFrame, text="√(x)",font = ("Arial", 12, "bold"),  bg="#434A54",  fg = "#E6E9ED",width=10, relief="raised", borderwidth=5, command=lambda:numeroPulsado("sqrt(x)"))
botonRaiz.place(x=740, y=250)




#-funcion que muestra el resultado-
def mostrar():
	f=lambda x:eval(funcionX.get())#recibimos la funcion en texto y la transformamos en expresion 
	xl=(valorXl.get())#obtenemos el valor de las cajas de texto de la interfaz
	xu=(valorXu.get())#obtenemos xu
	tolerancia=(valorTolerancia.get())#obtenemos la tolerancia
	bandera=True
	

	iteraciones=100
	xr=None
	contador=0
	error_calculado=101

	if f(xl)*f(xu) <=0:#evaluamos si hay raiz en el intervalo dado

		while contador <= iteraciones and error_calculado>=tolerancia:#controlamos el flujo de interaciones con el ciclo while

			contador+=1
			fxl=f(xl)
			fxu=f(xu)
			xr=xu-(fxu*(xl-xu))/(fxl-fxu)#evaluamos para obtener xr
			fxr=f(xr)

			try:#para evitar division entre 0 

				if bandera:
					error_calculado = abs((xr-xl)/xr)*100#error para cuando el intervalo està entre xl y xr
				else:
					error_calculado = abs((xr-xu)/xr)*100#error para intervalos entre xr y xu 

				if contador==1:
					#para no mostrar el primer error calculado en vez imprimir '-----'
					llenarTabla(contador, '{:.4f}'.format(xl), '{:.4f}'.format(xr), '{:.4f}'.format(xu), '{:.4f}'.format(fxl), '{:.4f}'.format(fxr), '{:.4f}'.format(fxu),'-------')

				else:
					#llamado a la funcion para llenar la tabla con los valor iterados en el ciclo

					llenarTabla(contador, '{:.4f}'.format(xl), '{:.4f}'.format(xr), '{:.4f}'.format(xu), '{:.4f}'.format(fxl), '{:.4f}'.format(fxr), '{:.4f}'.format(fxu), '{:.4f}'.format(error_calculado)+'%')

				if fxl*fxr>=0:# saber en que intervalo va a estar el nuevo reajuste
					xl=xr
				else:
					bandera=False
					xu=xr
			    #imprimir resultado en consola
				print('la solucion aproximada es: {:.4f}'.format(xr))
				print('encontrada en: {:.4f}'.format(contador) + 'iteraciones')
				print('con un error relativo de: {:.4f}'.format(error_calculado) + '%')

				rta=str('El valor de la raiz es: {:.4f}'.format(xr)+' con un error de:  {:.4f}'.format(error_calculado) + '% que es menor o igual a: '+'{:.4f}'.format(tolerancia)+'%')

				respuestaTxt.set(rta)#mostrar respuesta escrita



			except ZeroDivisionError as e:
				return print(e)#imprimir en consola el error de division por cero


	else:
		print("no hay solucion en el intervalo")

#-boton de envio-
botonEnvio=Button(miFrame, text="EJECUTAR",font = ("Arial", 12, "bold"), command=mostrar, bg="#37BC98",  fg = "#E6E9ED")
botonEnvio.place(x=220, y=250)

#--funcion para mostrar la grafica--
def grafica():
	f=lambda x:eval(funcionX.get())
	xl=(valorXl.get())
	xu=(valorXu.get())
	tolerancia=(valorTolerancia.get())
	bandera=True
	

	iteraciones=100
	xr=None
	contador=0
	error_calculado=101

	if f(xl)*f(xu) <=0:

		while contador <= iteraciones and error_calculado>=tolerancia:

			contador+=1
			fxl=f(xl)
			fxu=f(xu)
			xr=xu-(fxu*(xl-xu))/(fxl-fxu)
			fxr=f(xr)

			try:

				if fxl*fxr>=0:
					xl=xr
				else:
					bandera=False
					xu=xr
			except ZeroDivisionError as e:
				return print(e)

		f1=lambda x: eval(funcionX.get())
		
		x=np.linspace(0,10,100)#creamos la linea de espacio de o a 10 en la cuadricula de la grafica
		f2=np.vectorize(f1)#vectorizamos la funcion para poderla graficar
		plt.plot(x,f2(x), color="red",label="Funcion")#mostrar la funcion
		plt.axhline(0, 0, 1, label='Eje x')#mostrar el eje x para el intercepto
		plt.plot(xr,0,"o",color="green", label="Raiz")#mostrar el punto de la raiz 
		plt.grid()
		plt.legend()
		plt.show()


	else:
		print("no hay solucion en el intervalo")




#----boton de la grafica-- 
botonGrafica=Button(miFrame, text="GRAFICAR",font = ("Arial", 12, "bold"), command=grafica, bg="#656078",  fg = "#E6E9ED")
botonGrafica.place(x=350, y=250)


#---crear la tabla---
tv=ttk.Treeview(miFrame,columns=('I','XL','XR','XU','F(XL)','F(XR)','F(XU)','|EA|'), show='headings')
tv.column('I',minwidth=0, width=50, anchor='n')
tv.column('XL',minwidth=0, width=100, anchor='n')
tv.column('XR',minwidth=0, width=100, anchor='n')
tv.column('XU',minwidth=0, width=100, anchor='n')
tv.column('F(XL)',minwidth=0, width=100, anchor='n')
tv.column('F(XR)',minwidth=0, width=100, anchor='n')
tv.column('F(XU)',minwidth=0, width=100, anchor='n')
tv.column('|EA|',minwidth=0, width=100, anchor='n')
tv.heading('I',text='I')
tv.heading('XL',text='XL')
tv.heading('XR',text='XR')
tv.heading('XU',text='XU')
tv.heading('F(XL)',text='F(XL)')
tv.heading('F(XR)',text='F(XR)')
tv.heading('F(XU)',text='F(XU)')
tv.heading('|EA|',text='|EA|')
tv.place(x=110,y=310)

#--metodo para llenar la tabla---
def llenarTabla(i,xl,xr,xu,fl,fr,fu,ea):
	
	tv.insert("","end",values=(i,xl,xr,xu,fl,fr,fu,ea))

	
#--funcion para limpiar los campos---
def borrarCampos():
	
	funcionX.set("")
	valorXl.set("")
	valorXu.set("")
	valorTolerancia.set("")
	respuestaTxt.set("")
	for clean in tv.get_children():
		tv.delete(clean)

#--boton para limpiar la tabla y los campos---
botonDeLimpiar=Button(miFrame, text="LIMPIAR", font = ("Arial", 12, "bold"), command=borrarCampos, bg="#e3553d",  fg = "#E6E9ED")
botonDeLimpiar.place(x=110, y=250)

#mostramos lo que tenga el archivo raiz para iniciar la interfaz de usuario
raiz.mainloop()





#creado por Yilver Noel Sanchez Cañizares 2021
