from tkinter import Tk, Button, Entry, Label, filedialog, ttk, PhotoImage, StringVar, Scrollbar, Frame
import numpy as np
import sounddevice as sd
import soundfile as sf
import random

lista = []

for i in range(50,200,10):
	lista.append(i)

class Ventana(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.frame_top = Frame(self.master, bg='black', height=70)
        self.frame_top.grid(columnspan=2, row=0, sticky='nsew')
        self.frame_menu = Frame(self.master, bg='#272A31', width=50)
        self.frame_menu.grid(column=0, row=1, sticky='nsew')
        self.frame_principal = Frame(self.master, bg='black')
        self.frame_principal.grid(column=1, row=1, sticky='nsew')
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.frame_principal.columnconfigure(0, weight=1)
        self.frame_principal.rowconfigure(0, weight=1)

        self.widgets()

    def widgets(self):
        ####### IMAGENES #######
        self.imagen_play = PhotoImage(file='proyecto/img/play.png')
        self.imagen_folder = PhotoImage(file='proyecto/img/folder.png')
        self.imagen_stop = PhotoImage(file='proyecto/img/stop.png')
        self.imagen_pause = PhotoImage(file='proyecto/img/pause.png')
        self.logo = PhotoImage(file='proyecto/img/connection.png')

        ####### BOTONES DEL MENU LATERAL #######
        self.btn_play = Button(self.frame_menu, image=self.imagen_play, bg='#272A31', activebackground='black', bd=0, command=self.pantalla_play).grid(column=0, row=0)

        ####### CREAR PAGINAS #######
        estilo_paginas = ttk.Style()
        estilo_paginas.theme_use('default')
        estilo_paginas.configure("TNotebook", background='black', borderwidth=0)
        estilo_paginas.configure("TNotebook.Tab", background="black", borderwidth=0)
        estilo_paginas.map("TNotebook.Tab", background=[("selected", 'black')])

        self.paginas = ttk.Notebook(self.frame_principal, style='TNotebook')
        self.paginas.grid(column=0, row=0, sticky='nsew')
        self.frame_uno = Frame(self.paginas, bg='black')
        self.frame_dos = Frame(self.paginas, bg='black')
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

        ####### FRAME DOS #######
        self.frame1 = Frame(self.frame_dos, bg='black', width=600, height=350)
        self.frame1.grid(column=0, row=0)
        self.frame2 = Frame(self.frame_dos, bg='black', width=600, height=50)
        self.frame2.grid(column=0, row=1)

        self.pantalla_bumetro()

        boton1 = Button(self.frame2, image=self.imagen_play, bg='black', command=self._play)
        boton1.grid(column=0, row=0, pady=10)
        boton2 = Button(self.frame2, image=self.imagen_pause, bg='black', command=self._stop)
        boton2.grid(column=1, row=0, pady=10)
        boton3 = Button(self.frame2, image=self.imagen_stop, bg='black', command=self._stop)
        boton3.grid(column=2, row=0, pady=10)

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
            self.bumetro()
        except:
            print('Ingrese una cancion')

    def _stop(self):
        sd.stop()
        self.frame1.after_cancel(self.actualizar)

    def bumetro(self):
        self.barra1['value'] = random.choice(lista)
        self.barra2['value'] = random.choice(lista)
        self.barra3['value'] = random.choice(lista)
        self.barra4['value'] = random.choice(lista)
        self.barra5['value'] = random.choice(lista)
        self.barra6['value'] = random.choice(lista)
        self.barra7['value'] = random.choice(lista)
        self.barra8['value'] = random.choice(lista)
        self.barra9['value'] = random.choice(lista)
        self.barra10['value'] = random.choice(lista)
        self.barra11['value'] = random.choice(lista)
        self.barra12['value'] = random.choice(lista)
        self.barra13['value'] = random.choice(lista)
        self.barra14['value'] = random.choice(lista)
        self.barra15['value'] = random.choice(lista)
        self.barra16['value'] = random.choice(lista)
        self.barra17['value'] = random.choice(lista)
        self.barra18['value'] = random.choice(lista)
        self.barra19['value'] = random.choice(lista)
        self.barra20['value'] = random.choice(lista)

        self.actualizar = self.frame1.after(100, self.bumetro)
    
    def pantalla_play(self):
        self.paginas.select([self.frame_dos])
        self.frame_dos.columnconfigure(0, weight=1)
        self.frame_dos.rowconfigure(0, weight=1)
        self.frame_dos.rowconfigure(1, weight=1)

    def pantalla_bumetro(self):
        estilo = ttk.Style()
        estilo.configure("Vertical.TProgressbar", foreground='green2', background='green2',troughcolor='black',bordercolor='black', borderwidth=0, lightcolor='green2', darkcolor='green2')

        self.barra1 = ttk.Progressbar(self.frame1, orient='vertical', length=300, maximum=300)
        self.barra1.grid(column=0, row=0, padx=1)
        self.barra2 = ttk.Progressbar(self.frame1, orient= 'vertical',length=300,  maximum=300, style="Vertical.TProgressbar")
        self.barra2.grid(column=1, row=0, padx = 1)
        self.barra3 = ttk.Progressbar(self.frame1, orient= 'vertical',length=300,  maximum=300, style="Vertical.TProgressbar")
        self.barra3.grid(column=2, row=0, padx = 1)
        self.barra4 = ttk.Progressbar(self.frame1, orient= 'vertical',length=300,  maximum=300, style="Vertical.TProgressbar")
        self.barra4.grid(column=3, row=0, padx = 1)
        self.barra5 = ttk.Progressbar(self.frame1, orient= 'vertical',length=300,  maximum=300, style="Vertical.TProgressbar")
        self.barra5.grid(column=4, row=0, padx = 1)
        self.barra6 = ttk.Progressbar(self.frame1, orient= 'vertical',length=300,  maximum=300, style="Vertical.TProgressbar")
        self.barra6.grid(column=5, row=0, padx = 1)
        self.barra7 = ttk.Progressbar(self.frame1, orient= 'vertical', length=300,  maximum=300, style="Vertical.TProgressbar")
        self.barra7.grid(column=6, row=0, padx = 1)
        self.barra8 = ttk.Progressbar(self.frame1, orient= 'vertical',length=300,  maximum=300, style="Vertical.TProgressbar")
        self.barra8.grid(column=7, row=0, padx = 1)
        self.barra9 = ttk.Progressbar(self.frame1, orient= 'vertical',length=300,  maximum=300, style="Vertical.TProgressbar")
        self.barra9.grid(column=8, row=0, padx = 1)
        self.barra10 = ttk.Progressbar(self.frame1, orient= 'vertical',length=300,  maximum=300, style="Vertical.TProgressbar")
        self.barra10.grid(column=9, row=0, padx = 1)
        self.barra11 = ttk.Progressbar(self.frame1, orient= 'vertical',length=300,  maximum=300, style="Vertical.TProgressbar")
        self.barra11.grid(column=10, row=0, padx = 1)
        self.barra12 = ttk.Progressbar(self.frame1, orient= 'vertical',length=300,  maximum=300, style="Vertical.TProgressbar")
        self.barra12.grid(column=11, row=0, padx = 1)
        self.barra13 = ttk.Progressbar(self.frame1, orient= 'vertical',length=300,  maximum=300, style="Vertical.TProgressbar")
        self.barra13.grid(column=12, row=0, padx = 1)
        self.barra14 = ttk.Progressbar(self.frame1, orient= 'vertical', length=300,  maximum=300, style="Vertical.TProgressbar") 
        self.barra14.grid(column=13, row=0, padx = 1)
        self.barra15 = ttk.Progressbar(self.frame1, orient= 'vertical', length=300,  maximum=300, style="Vertical.TProgressbar") 
        self.barra15.grid(column=14, row=0, padx = 1)
        self.barra16 = ttk.Progressbar(self.frame1, orient= 'vertical', length=300,  maximum=300, style="Vertical.TProgressbar") 
        self.barra16.grid(column=15, row=0, padx = 1)
        self.barra17 = ttk.Progressbar(self.frame1, orient= 'vertical', length=300,  maximum=300, style="Vertical.TProgressbar") 
        self.barra17.grid(column=16, row=0, padx = 1)
        self.barra18 = ttk.Progressbar(self.frame1, orient= 'vertical', length=300,  maximum=300, style="Vertical.TProgressbar") 
        self.barra18.grid(column=17, row=0, padx = 1)
        self.barra19 = ttk.Progressbar(self.frame1, orient= 'vertical', length=300,  maximum=300, style="Vertical.TProgressbar") 
        self.barra19.grid(column=18, row=0, padx = 1)
        self.barra20 = ttk.Progressbar(self.frame1, orient= 'vertical', length=300,  maximum=300, style="Vertical.TProgressbar") 
        self.barra20.grid(column=19, row=0, padx = 1)