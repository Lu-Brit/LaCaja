from tkinter import *
raiz =Tk()
from tkinter import messagebox
raiz.title("Calculadora")
raiz.config(bg="black")
raiz.resizable(0,0)
raiz.config(relief="groove")
raiz.config(bd=15)
miFrame=Frame(raiz, width=300, height=500)
miFrame.config(cursor="target",background="darkslategrey")
miFrame.pack()

numeroPantalla=StringVar()
cuenta=""
reserva=""
resultado=0

#---------------------Pulsaciones teclado
def numeroPulsado(num):
	global cuenta
	if cuenta == "":
		(numeroPantalla.set(numeroPantalla.get() + num))
	else:
		
		numeroPantalla.set(num)
		cuenta=""
		



#---------------------Funcion suma
def suma(valor):
	global cuenta
	global reserva
	global resultado
	resultado+=int(valor)
	cuenta="suma"
	reserva="suma"
	numeroPantalla.set(resultado)
#---------------------Funcion resta
def resta(valor):
	global cuenta
	global reserva
	global resultado
	resultado+=int(valor)
	cuenta="resta"
	reserva= "resta"
	numeroPantalla.set(valor)

	
#---------------------Funcion multiplicacion
def multiplicacion(valor):
	global cuenta
	global reserva
	global resultado
	resultado+= int(valor)
	cuenta="multiplicacion"
	reserva="multiplicacion"
	numeroPantalla.set(resultado)
#---------------------Funcion division
def division (valor):
	global cuenta
	global reserva
	global resultado
	resultado= int(valor)
	cuenta="division"
	reserva="division"
	numeroPantalla.set(resultado)


#---------------------Funcion coma
def coma():
	global cuenta
	global reserva
	numeroPantalla.set(float(numeroPantalla.get()))

#--------------Funcion retroceso/ borra lo la escrito
def clear():
	global cuenta
	global reserva
	cuenta =""
	reserva=""
	numeroPantalla.set("")
	
#---------------Funcion igual

def Igual():
	global resultado
	global operacion
	global reserva
	try:
		if reserva == "division":

			numeroPantalla.set(resultado/float(numeroPantalla.get()))
		
		elif reserva == "resta":
			numeroPantalla.set(resultado-float(numeroPantalla.get()))

		elif reserva == "multiplicacion":
			numeroPantalla.set(resultado*float(numeroPantalla.get()))
		
		elif reserva == "suma":
			numeroPantalla.set(resultado+float(numeroPantalla.get()))

	except:
			numeroPantalla.set("Syntax Error")		  
		
	resultado=0
#---------------------Pantalla-----------------
pantalla=Entry(miFrame,font=("Copperplate",15), textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=2, pady=2, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

#---------------Fila1---------------
boton7=Button(miFrame, text="7", width=6,height=3,font=("Verdana",9), command = lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text="8", width=6,height=3,font=("Verdana",9), command =lambda: numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text="9", width=6,height=3,font=("Verdana",9), command = lambda:numeroPulsado("9"),)
boton9.grid(row=2, column=3)
botonDiv=Button(miFrame, text="/",background="lightslategrey",height=3,font=("Verdana",9), width=6, command=lambda:division(numeroPantalla.get()))
botonDiv.grid(row=2, column=4)

#---------------Fila2---------------
Boton4=Button(miFrame, text="4", width=6,height=3,font=("Verdana",9), command = lambda:numeroPulsado("4"))
Boton4.grid(row=3, column=1)
Boton5=Button(miFrame, text="5", width=6,height=3,font=("Verdana",9), command = lambda:numeroPulsado("5"))
Boton5.grid(row=3, column=2)
Boton6=Button(miFrame, text="6", width=6,height=3,font=("Verdana",9), command = lambda:numeroPulsado("6"))
Boton6.grid(row=3, column=3)
botonMult=Button(miFrame,background="lightslategrey",font=("Verdana",9), text="x",height=3, width=6,command=lambda:multiplicacion(numeroPantalla.get()))
botonMult.grid(row=3, column=4)

#---------------Fila3---------------
boton1=Button(miFrame, text="1",height=3, width=6,font=("Verdana",9), command = lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2=Button(miFrame, text="2",height=3, width=6,font=("Verdana",9), command = lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3=Button(miFrame, text="3",height=3, width=6,font=("Verdana",9), command = lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonMen=Button(miFrame,background="lightslategrey",font=("Verdana",9), text="-",height=3, width=6,command=lambda:resta(numeroPantalla.get()))
botonMen.grid(row=4, column=4)

#---------------Fila4---------------
Boton0=Button(miFrame, text="0",height=3,font=("Verdana",9), width=6, command = lambda:numeroPulsado("0"))
Boton0.grid(row=5, column=1)
BotonComa=Button(miFrame, text=".",background="lightslategrey",font=("Verdana",9), width=6,height=3, command = lambda:numeroPulsado("."))
BotonComa.grid(row=5, column=2)
BotonIgual=Button(miFrame, text="=",background="maroon",font=("Verdana",9) ,width=6,height=3, command = lambda:Igual())
BotonIgual.grid(row=5, column=4)
botonSum=Button(miFrame, text="+",background="lightslategrey",font=("Verdana",9),height=3, width=6, command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5, column=3)

botonRetro=Button(miFrame, text="C",background="lightslategrey",font=("Verdana",7),height=3, width=5,command = lambda:clear())
botonRetro.grid(row=1, column=5)
 
barraMenu=Menu(raiz)
raiz.config(menu=barraMenu,width=300,height=300)

def infoAdicional():
	messagebox.showinfo("Procesador de texto", "Version 2020 Python 3.x")
def avisoLicencia():
	messagebox.showwarning("Licencia", "Calculadora en proceso TM - 2022")

def salirAplicacion():
	valor=messagebox.askokcancel("Salir", "¿Deseas salir de al aplicación?")
	if valor =="yes":
		raiz.destroy()

def cerrarDocumento():
	valor=messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado")

def noimplementado():
	messagebox.showinfo("Error", "No disponible en la versión gratuita.")

archivoMenu=Menu(barraMenu, tearoff=0) # se crea el nombre y a que menú corresponde
HerramientaMenu=Menu(barraMenu, tearoff=0)
AyudaMenu=Menu(barraMenu, tearoff=0)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Herramientas", menu=HerramientaMenu)
barraMenu.add_cascade(label="Ayuda", menu=AyudaMenu)


archivoMenu.add_command(label="Salir",command=salirAplicacion)

HerramientaMenu.add_command(label="Modo Avanzado",command=noimplementado)
HerramientaMenu.add_separator()
HerramientaMenu.add_command(label="Modo Gráfico",command=noimplementado)


AyudaMenu.add_command(label="Licencia",command=avisoLicencia)
AyudaMenu.add_separator()
AyudaMenu.add_command(label="Acerca de:",command=infoAdicional)




raiz.mainloop()

