from tkinter import *

ventana= Tk()

ventana.geometry("700x400")
ventana.title("Formularios")


#Encabezado del formulario
encabezado = Label(ventana, text='Formularios con Tkinter - Aldayr RDZ')
encabezado.config(
    fg="white", 
    bg="darkgray",
    font=("Open Sans", 18),
    padx=10, 
    pady=10
)
encabezado.grid(row=0, column=0,columnspan=12, sticky=W)

#label para el campo 
label = Label(ventana, text="Nombre")
label.grid(row=1, column=0, padx=5, pady=5)

# Campo de texto 
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1 ,sticky=W,padx=5, pady=5)
campo_texto.config(justify="left", state="normal")


#label para el campo (apellidos)
label = Label(ventana, text="Apellidos")
label.grid(row=2, column=0, padx=5, pady=5)

# Campo de texto (apellidos)
campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1,sticky=W,padx=5, pady=5)
campo_texto.config(justify="left", state="normal")

#label para el campo (descripcion)
label = Label(ventana, text="Descripcion")
label.grid(row=3, column=0, sticky=N,padx=5, pady=5)

#campo de texto grande (descripcion)
campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1)
campo_grande.config(
    width=30, 
    height=5,
    font=("Arial", 12),
    padx=15,
    pady=15
    )

# Boton 

Label(ventana).grid(row=4, column=1)

boton =Button(ventana, text='Enviar')
boton.grid(row=5, column=1, sticky= W)
boton.config(
    padx=10,
    pady=10,
    bg='green',
    fg='white',

)
ventana.mainloop()
