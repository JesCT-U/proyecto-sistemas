from tkinter import Tk
from client.gui_app import Ventana

def main():
    root = Tk()
    root.title('Teoria de sistemas')
    root.minsize(height=475, width=795)

    app = Ventana(root)
    app.mainloop()

if __name__ == '__main__':
    main()