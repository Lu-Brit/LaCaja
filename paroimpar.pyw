from tkinter import *


def respuestas():
	respuesta=str(input("quiere añadir otro? si o no: "))	
				
	if respuesta=="SI" or "si" or "Si" or "Sí":
							    
						 parimpar()
	elif respuesta =="NO" or "no" or "No":
			             print("Gracias")
	else: 
			              print("Disculpa, no te he entendido")
			              respuesta==""
			              respuestas()




def parimpar():
		try: numero=float(input("En que numero esta pensando? "))
		except Exception:
			print("Ese no es un número")
			parimpar()
		
		if float(numero)>=1 and float(1000)>= numero:
				if (float(numero % 2)) == 0:
					print("El numero",numero,"es par")
				elif float(numero)<=1 or float(numero)>=1000:
				 	print("El numero",numero,"es impar")



				
		else:
				print("introduzca un numero de 1 a 1000")

		respuestas()

parimpar()