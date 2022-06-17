# Calculadora de NOMINALES

from tkinter import *

def clear_all() :
 
    # whole content of entry boxes is deleted
    dolares.delete(0, END)  
    precio.delete(0, END)
    comision.delete(0, END)
    nominales.delete(0, END)
   
    # set focus on the principle_field entry box 
    nominales.focus_set()

def venta():
    dolaresv = float(dolares.get())

    preciov = float(precio.get())
 
    comisionv = float(comision.get())
    comisionv = comisionv/100
     
    # Calculates compound interest 
    NOM = int((dolaresv/preciov)*(1-comisionv))
 
    # insert method inserting the 
    # value in the text entry box.
    nominales.delete(0, END)
    nominales.insert(10, NOM)

if __name__ == "__main__" :
   
    # Create a GUI window
    root = Tk()
   
    # Set the background colour of GUI window
    root.configure(background = 'navy blue')
   
    # # Set the configuration of GUI window
    # root.geometry("250x250")
   
    # set the name of tkinter GUI window
    root.title("Calculadora Nominales") 

    labeldolares = Label(root, text="MONTO: ").grid(pady=5, row=0, column=0)
    labelprecio = Label(root, text="PRECIO: ").grid( pady=5, row=1, column=0)
    labelcomision = Label(root, text="COMISION: ").grid( pady=5, row=2, column=0)
    labelnominales = Label(root, text="NOMINALES: ").grid( pady=5, row=5, column=0)
 
    # Create a entry box 
    # for filling or typing the information.
    dolares = Entry(root) 
    precio = Entry(root) 
    comision = Entry(root)
    nominales = Entry(root)
 

    dolares.grid(row = 0, column = 1, padx = 10, pady = 10) 
    precio.grid(row = 1, column = 1, padx = 10, pady = 10) 
    comision.grid(row = 2, column = 1, padx = 10, pady = 10)
    nominales.grid(row = 5, column = 1, padx = 10, pady = 10)
 
    # to calculate_ci function 
    button1 = Button(root, text = "Calcular", command = venta)
   
    # Create a Clear Button and attached 
    # to clear_all function 
    button2 = Button(root, text = "Borrar",  command = clear_all)
   
    button1.grid(row = 4, column = 1, pady = 10)
    button2.grid(row = 6, column = 1, pady = 10)
 
    # Start the GUI 
    root.mainloop()

