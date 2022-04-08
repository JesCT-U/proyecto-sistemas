from tkinter import Tk, Button, Entry, Label, filedialog, ttk, PhotoImage, StringVar, Scrollbar, Frame
import numpy as np
import sounddevice as sd
import soundfile as sf


class Ventana(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.frame_top = Frame(self.master, bg='black', height=70)
        self.frame_top.grid(columnspan=2, row=0, sticky='nsew')
        self.frame_menu = Frame(self.master, bg='black', width=50)
        self.frame_menu.grid(column=0, row=1, sticky='nsew')
        self.frame_principal = Frame(self.master, bg='black')
        self.frame_principal.grid(column=1, row=1, sticky='nsew')
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.frame_principal.columnconfigure(0, weight=1)
        self.frame_principal.rowconfigure(0, weight=1)

        self.widgets()

    def widgets(self):
        self.imagen_play = PhotoImage(file='proyecto/img/play.png')
        self.imagen_folder = PhotoImage(file='proyecto/img/folder.png')
        self.logo = PhotoImage(file='proyecto/img/connection.png')

        self.btn_play = Button(self.frame_menu, image=self.imagen_play, bg='black', activebackground='black', bd=0, command=self._play).grid(column=0, row=0)

        ####### CREAR PAGINAS #######
        estilo_paginas = ttk.Style()
        estilo_paginas.theme_use('default')
        estilo_paginas.configure("TNotebook", background='black', borderwidth=0)
        estilo_paginas.configure("TNotebook.Tab", background="black", borderwidth=0)
        #estilo_paginas.map("TNotebook", background=[("selected", 'black')])
        estilo_paginas.map("TNotebook.Tab", background=[("selected", 'black')])

        self.paginas = ttk.Notebook(self.frame_principal, style='TNotebook')
        self.paginas.grid(column=0, row=0, sticky='nsew')
        self.frame_uno = Frame(self.paginas, bg='black')
        self.frame_dos = Frame(self.paginas, bg='white')
        self.paginas.add(self.frame_uno)
        self.paginas.add(self.frame_dos)

        ####### FRAME TOP #######
        self.titulo = Label(self.frame_top, text="Cargue un archivo de audio", bg='black', fg='gray', font=('Arial', 15, 'bold'))
        self.titulo.pack(side='left')
        self.btn_cargar = Button(self.frame_top, image=self.imagen_folder, bg='black', activebackground='red', bd=0, command=self.cargar_archivo).pack(side='right')

        ####### FRAME UNO #######
        Label(self.frame_uno, text='Jesus Capriel - 201908009', bg='black', fg='white', font=('Arial', 20, 'bold')).pack(expand=1)
        Label(self.frame_uno, text='Gelder Tubac - 2018XXXXX', bg='black', fg='white', font=('Arial', 20, 'bold')).pack(expand=1)
        Label(self.frame_uno, image=self.logo, bg='black').pack(expand=1)

    def cargar_archivo(self):
        self.direccion = filedialog.askopenfilename(initialdir='/', title='Escoger archivo', filetypes=(('mp3 files', '*.mp3*'),('All files', '*.*')))

        if self.direccion != '':
            nombre_cancion = self.direccion.split('/')
            nombre_cancion = nombre_cancion[-1]
            self.titulo['text'] = nombre_cancion

    def _play(self):
        try:
            s, fs = sf.read(self.direccion)
            sd.play(s, fs)
        except:
            print('Ingrese una cancion')