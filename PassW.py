import random
import string
import json
import tkinter as tk

def generar_contrasena(longitud, complejidad):
    caracteres = ''
    
    if complejidad == 'baja':
        caracteres = string.ascii_letters + string.digits  # Solo letras y números
    elif complejidad == 'media':
        caracteres = string.ascii_letters + string.digits + string.ascii_uppercase  # Letras mayúsculas y minúsculas y números 
    elif complejidad == 'alta':
        caracteres = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase  # Agregar signos de puntuación
    
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena

def guardar_contrasenas(contrasenas):
    try:
        with open('contrasenas.txt', 'r') as archivo:
            data = json.load(archivo)
    except FileNotFoundError:
        data = {}  # Si el archivo no existe, inicializa un diccionario vacío

    data.update(contrasenas)

    with open('contrasenas.txt', 'w') as archivo:
        json.dump(data, archivo)

def generar_y_mostrar_contrasena():
    longitud = int(longitud_entry.get())
    complejidad = complejidad_var.get()
    sitio = sitio_entry.get()

    nueva_contrasena = generar_contrasena(longitud, complejidad)
    resultado_label.config(text=f"Tu nueva contraseña segura para {sitio} es: {nueva_contrasena}")

    contrasenas_guardadas[sitio] = nueva_contrasena

def guardar_y_salir():
    guardar_contrasenas(contrasenas_guardadas)
    root.destroy()

root = tk.Tk()
root.title("Generador de Contraseñas")

contrasenas_guardadas = {}

root.configure(bg='#90e0ef')  # Cambio de color de fondo
titulo = tk.Label(root, text="Generador de Contraseñas", font=("Arial", 15), bg='#90e0ef')
titulo.pack()

formulario_frame = tk.Frame(root, bg='#90e0ef')  # Marco para el formulario
formulario_frame.pack(padx=20, pady=10)

formulario_frame = tk.Frame(root, bg='#90e0ef')  # Marco para el formulario
formulario_frame.pack(padx=20, pady=10)

tk.Label(formulario_frame, text="Longitud de la contraseña:", bg='#90e0ef').grid(row=0, column=0)
longitud_entry = tk.Entry(formulario_frame)
longitud_entry.grid(row=0, column=1)

tk.Label(formulario_frame, text="Complejidad de la contraseña:", bg='#90e0ef').grid(row=1, column=0)
complejidad_var = tk.StringVar(root)
complejidad_var.set("baja")
complejidad_menu = tk.OptionMenu(formulario_frame, complejidad_var, "baja", "media", "alta")
complejidad_menu.config(bg='#dda15e')
complejidad_menu.grid(row=1, column=1)



tk.Label(formulario_frame, text="Sitio web o servicio:", bg='#90e0ef').grid(row=2, column=0)
sitio_entry = tk.Entry(formulario_frame)
sitio_entry.grid(row=2, column=1)

generar_button = tk.Button(root, text="Generar Contraseña", command=generar_y_mostrar_contrasena , bg='#dda15e')
generar_button.pack(pady=10)

resultado_label = tk.Label(root, text="", font=("Arial", 12), bg='#90e0ef')
resultado_label.pack()

guardar_button = tk.Button(root, text="Guardar y Salir", command=guardar_y_salir , bg='#dda15e')
guardar_button.pack(pady=15)

root.mainloop()
