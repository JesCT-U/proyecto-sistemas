from tkinter import Tk, Button, Entry, Label, filedialog, ttk, PhotoImage, StringVar, Scrollbar, Frame
import numpy as np
import sounddevice as sd
import soundfile as sf


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

        self.valor_amplitud = 0.10

        self.widgets()

    def widgets(self):
        ####### IMAGENES #######
        self.imagen_play = PhotoImage(file='proyecto/img/play.png')
        self.imagen_reflejar = PhotoImage(file='proyecto/img/al_reves.png')
        self.imagen_amplitud = PhotoImage(file='proyecto/img/volumen.png')
        self.imagen_efecto = PhotoImage(file='proyecto/img/_efecto.png')
        self.imagen_intercambio = PhotoImage(
            file='proyecto/img/intercambio.png')
        self.imagen_folder = PhotoImage(file='proyecto/img/folder.png')
        self.imagen_stop = PhotoImage(file='proyecto/img/stop.png')
        self.imagen_pause = PhotoImage(file='proyecto/img/pause.png')
        self.imagen_subir = PhotoImage(file='proyecto/img/subir.png')
        self.imagen_bajar = PhotoImage(file='proyecto/img/baja.png')
        self.logo = PhotoImage(file='proyecto/img/connection.png')

        ####### BOTONES DEL MENU LATERAL #######
        self.btn_play = Button(self.frame_menu, image=self.imagen_play, bg='#272A31',
                               activebackground='black', bd=0, command=self.pantalla_play).grid(column=0, row=0)
        self.btn_intercambio = Button(self.frame_menu, image=self.imagen_intercambio, bg='#272A31',
                                      activebackground='black', bd=0, command=self.pantalla_intercambiar).grid(column=0, row=1)
        self.btn_reflejar = Button(self.frame_menu, image=self.imagen_reflejar, bg='#272A31',
                                   activebackground='black', bd=0, command=self.pantalla_reflejar).grid(column=0, row=2)
        self.btn_amplitud = Button(self.frame_menu, image=self.imagen_amplitud, bg='#272A31',
                                   activebackground='black', bd=0, command=self.pantalla_amplitud).grid(column=0, row=3)
        self.btn_efecto = Button(self.frame_menu, image=self.imagen_efecto, bg='#272A31',
                                 activebackground='black', bd=0, command=self.pantalla_efecto).grid(column=0, row=4)

        ####### CREAR PAGINAS #######
        estilo_paginas = ttk.Style()
        estilo_paginas.theme_use('default')
        estilo_paginas.configure(
            "TNotebook", background='black', borderwidth=0)
        estilo_paginas.configure(
            "TNotebook.Tab", background="black", borderwidth=0)
        estilo_paginas.map("TNotebook.Tab", background=[("selected", 'black')])

        self.paginas = ttk.Notebook(self.frame_principal, style='TNotebook')
        self.paginas.grid(column=0, row=0, sticky='nsew')
        self.frame_uno = Frame(self.paginas, bg='black')
        self.frame_dos = Frame(self.paginas, bg='black')
        self.frame_tres = Frame(self.paginas, bg='black')
        self.frame_cuatro = Frame(self.paginas, bg='black')
        self.frame_cinco = Frame(self.paginas, bg='black')
        self.frame_seis = Frame(self.paginas, bg='black')
        self.paginas.add(self.frame_uno)
        self.paginas.add(self.frame_dos)
        self.paginas.add(self.frame_tres)
        self.paginas.add(self.frame_cuatro)
        self.paginas.add(self.frame_cinco)
        self.paginas.add(self.frame_seis)

        ####### FRAME TOP #######
        self.titulo = Label(self.frame_top, text="Cargue un archivo de audio",
                            bg='black', fg='gray', font=('Arial', 15, 'bold'))
        self.titulo.pack(side='left')
        self.btn_cargar = Button(self.frame_top, image=self.imagen_folder, bg='black',
                                 activebackground='red', bd=0, command=self.cargar_archivo).pack(side='right')

        ####### FRAME UNO #######
        Label(self.frame_uno, text='Jesus Capriel - 201908009', bg='black',
              fg='white', font=('Arial', 20, 'bold')).pack(expand=1)
        Label(self.frame_uno, text='Gelder Tubac - 201808036', bg='black',
              fg='white', font=('Arial', 20, 'bold')).pack(expand=1)
        Label(self.frame_uno, image=self.logo, bg='black').pack(expand=1)

        ####### FRAME DOS #######
        self.frame1 = Frame(self.frame_dos, bg='black', width=600, height=350)
        self.frame1.grid(column=0, row=0)
        Label(self.frame1, text='Reproducir audio', bg='black',
              fg='white', font=('Calibri', 20, 'bold')).pack(expand=1)

        self.frame2 = Frame(self.frame_dos, bg='black', width=600, height=50)
        self.frame2.grid(column=0, row=1)
        boton1 = Button(self.frame2, image=self.imagen_play,
                        bg='black', command=self._play)
        boton1.grid(column=0, row=0, pady=10)
        boton2 = Button(self.frame2, image=self.imagen_stop,
                        bg='black', command=self._stop)
        boton2.grid(column=2, row=0, pady=10)

        ####### FRAME TRES #######
        self.frame3 = Frame(self.frame_tres, bg='black', width=600, height=350)
        self.frame3.grid(column=0, row=0)
        Label(self.frame3, text='Intercambiar canales', bg='black',
              fg='white', font=('Calibri', 20, 'bold')).pack(expand=1)

        self.frame4 = Frame(self.frame_tres, bg='black', width=600, height=50)
        self.frame4.grid(column=0, row=1)
        boton3 = Button(self.frame4, image=self.imagen_play,
                        bg='black', command=self._intercambiar)
        boton3.grid(column=0, row=0, pady=10)
        boton4 = Button(self.frame4, image=self.imagen_stop,
                        bg='black', command=self._stop)
        boton4.grid(column=2, row=0, pady=10)

        ####### FRAME CUATRO #######
        self.frame5 = Frame(self.frame_cuatro, bg='black',
                            width=600, height=350)
        self.frame5.grid(column=0, row=0)
        Label(self.frame5, text='Reflejar canales', bg='black',
              fg='white', font=('Calibri', 20, 'bold')).pack(expand=1)

        self.frame6 = Frame(self.frame_cuatro, bg='black',
                            width=600, height=50)
        self.frame6.grid(column=0, row=1)
        boton5 = Button(self.frame6, image=self.imagen_play,
                        bg='black', command=self._reflejar)
        boton5.grid(column=0, row=0, pady=10)
        boton6 = Button(self.frame6, image=self.imagen_stop,
                        bg='black', command=self._stop)
        boton6.grid(column=2, row=0, pady=10)

        ####### FRAME CINCO #######
        self.frame7 = Frame(self.frame_cinco, bg='black',
                            width=600, height=350)
        self.frame7.grid(column=0, row=0)
        self.nivel_amplitud = Label(self.frame7, text='Incrementar o decrementar amplitud',
                                    bg='black', fg='white', font=('Calibri', 20, 'bold'))
        self.nivel_amplitud.pack(expand=1)

        self.frame8 = Frame(self.frame_cinco, bg='black', width=600, height=50)
        self.frame8.grid(column=0, row=1)
        boton7 = Button(self.frame8, image=self.imagen_play,
                        bg='black', command=self._amplitud)
        boton7.grid(column=0, row=0, pady=10)
        boton8 = Button(self.frame8, image=self.imagen_stop,
                        bg='black', command=self._stop)
        boton8.grid(column=1, row=0, pady=10)
        boton9 = Button(self.frame8, image=self.imagen_subir,
                        bg='black', command=self._subir)
        boton9.grid(column=2, row=0, pady=10)
        boton10 = Button(self.frame8, image=self.imagen_bajar,
                         bg='black', command=self._bajar)
        boton10.grid(column=3, row=0, pady=10)

        ####### FRAME SEIS #######
        self.frame11 = Frame(self.frame_seis, bg='black',
                            width=600, height=350)
        self.frame11.grid(column=0, row=0)
        Label(self.frame11, text='Filtro', bg='black',
              fg='white', font=('Calibri', 20, 'bold')).pack(expand=1)

        self.frame12 = Frame(self.frame_seis, bg='black',
                            width=600, height=50)
        self.frame12.grid(column=0, row=1)
        boton11 = Button(self.frame12, image=self.imagen_play,
                        bg='black', command=self._filtro)
        boton11.grid(column=0, row=0, pady=10)
        boton12 = Button(self.frame12, image=self.imagen_stop,
                        bg='black', command=self._stop)
        boton12.grid(column=2, row=0, pady=10)

    def cargar_archivo(self):
        self.direccion = filedialog.askopenfilename(
            initialdir='/Users/jesus/Desktop', title='Escoger archivo', filetypes=(('Audio Files', '.wav .ogg .flac'), ('All files', '*.*')))

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

    def _stop(self):
        sd.stop()

    def _intercambiar(self):
        try:
            s, fs = sf.read(self.direccion)

            ffs = 0
            fss = 0
            longitud = len(s)

            for x in range(0, longitud):
                for y in [0, 1]:
                    if y == 0:
                        ffs = s[x, y]
                    else:
                        fss = s[x, y]

                s[x, 0] = fss
                s[x, 1] = ffs

            sd.play(s, fs)
        except:
            print('Ingrese una cancion')

    def _reflejar(self):

        try:
            s, fs = sf.read(self.direccion)
            s = s[:: -1]
            sd.play(s, fs)
        except:
            print('Ingrese una cancion')

    def _amplitud(self):
        try:
            s, fs = sf.read(self.direccion)
            s = np.multiply(s, self.valor_amplitud)

            sd.play(s, fs)
        except:
            print('Ingrese una cancion')

    def _subir(self):
        if self.valor_amplitud < 0.90:
            self.valor_amplitud = self.valor_amplitud + 0.10
            self.nivel_amplitud['text'] = str(
                int(self.valor_amplitud*100)) + '%'

    def _bajar(self):
        if self.valor_amplitud > 0.10:
            self.valor_amplitud = self.valor_amplitud - 0.10
            self.nivel_amplitud['text'] = str(
                int(self.valor_amplitud*100)) + '%'

    def _filtro(self):
        try:
            s, fs = sf.read(self.direccion)
            h = np.array([0.25, 0.5])
            s = np.convolve(s, h)

            sd.play(s, fs)
        except:
            print('Ingrese una cancion para el filtro')

    def pantalla_play(self):
        sd.stop()
        self.paginas.select([self.frame_dos])
        self.frame_dos.columnconfigure(0, weight=1)
        self.frame_dos.rowconfigure(0, weight=1)
        self.frame_dos.rowconfigure(1, weight=1)

    def pantalla_intercambiar(self):
        sd.stop()
        self.paginas.select([self.frame_tres])
        self.frame_tres.columnconfigure(0, weight=1)
        self.frame_tres.rowconfigure(0, weight=1)
        self.frame_tres.rowconfigure(1, weight=1)

    def pantalla_reflejar(self):
        sd.stop()
        self.paginas.select([self.frame_cuatro])
        self.frame_cuatro.columnconfigure(0, weight=1)
        self.frame_cuatro.rowconfigure(0, weight=1)
        self.frame_cuatro.rowconfigure(1, weight=1)

    def pantalla_amplitud(self):
        sd.stop()
        self.paginas.select([self.frame_cinco])
        self.frame_cinco.columnconfigure(0, weight=1)
        self.frame_cinco.rowconfigure(0, weight=1)
        self.frame_cinco.rowconfigure(1, weight=1)

    def pantalla_efecto(self):
        sd.stop()
        self.paginas.select([self.frame_seis])
        self.frame_seis.columnconfigure(0, weight=1)
        self.frame_seis.rowconfigure(0, weight=1)
        self.frame_seis.rowconfigure(1, weight=1)
