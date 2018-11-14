# -*- coding: utf-8 -*-
import tkinter as tk

class Noticias():
	def __init__(self):
		raiz=Tk()
		raiz.geometry('300x200')
		raiz.configure(bg='white')
		raiz.title('Noticias')
		tk.Button(raiz, text='Seleccionar', command='submit').pack(side=BOTTOM)
		tk.Button(raiz, text='Salir', command='quit').pack(side=BOTTOM)
		raiz.mainloop()

def main():
	noticiero=Noticias()
	return 0

if __name__=='__main__':
	main()