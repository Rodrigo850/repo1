from dataclasses import replace
from gettext import find
from tkinter import *
from tkinter import messagebox

def meses():
    archivo = open("syslog","r") 
    lineas = archivo.readlines()
    periodo = set()

    for texto in lineas:
        mes = texto.split()[0:1]
        mes = " ".join(mes)
        periodo.add (mes)
        

        archivo_texto = open("doclog.txt", "a")

        archivo_texto.write(mes + "\n")
        
        archivo_texto.close()
    messagebox.showinfo('Mensaje', 'Archivo de texto generado.')
    print("Se ha escrito con éxito!")
    print(periodo)
#---------------------------------------

def eventos():
     archivo = open("syslog","r")  
     lineas = archivo.readlines()
     
     for texto in lineas:
        programa = texto.split()[4]
        if '[' in programa:
            #averiguar posicin en q esta el cracter
            pos = programa.index("[")
            programa = programa [:pos]
            print(programa)
        archivo_texto = open("doclog.txt", "a")

        archivo_texto.write(programa + "\n")
            
        archivo_texto.close()
     messagebox.showinfo('Mensaje', 'Archivo de texto generado.')
     print("Se ha escrito con éxito!")

#---------------------------------------
window = Tk()  
window.geometry('640x480')  

window.title("Procesamiento de logs")

botonmeses = Button(window,
	text = 'Meses en que se registraron los eventos',
    bg = 'LightBlue',
	command = meses)  
botonmeses.pack()  

botoneventos = Button(window,
	text = 'programas registrados',
    bg = 'LightBlue',
	command = eventos)  
botoneventos.pack() 

window.mainloop()

