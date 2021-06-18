from tkinter import *
from tkinter import messagebox
import sqlite3

#-------------------------Conexion Base datos------------------------
def conexionBBDD():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    try:
        miCursor.execute('''
        CREATE TABLE DatosUsuarios (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        NombreUsuario VARCHAR(50),
        Password VARCHAR(50),
        Apellido VARCHAR(10),
        Direccion VARCHAR(50),
        Comentarios VARCHAR(100)
        )
        ''')
        messagebox.showinfo("BBDD","BBDD creada con exito")
    except:
        messagebox.showwarning("Atencion!","BBDD ya existe")

def salirAplicacion():
    respuesta = messagebox.askquestion("Salir","Desea salir de la app")
    if(respuesta=="yes"):
        root.destroy()

#--------------------Borrar campos----------------
def limpiarCampos():
    miId.set("")
    miNombre.set("")
    miApellido.set("")
    miDireccion.set("")
    miPass.set("")
    textoEntry.delete(1.0,END) #borra desde el primer caracter hasta el final

#---------------CRUD--------------------------
#Crear
def crear():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    '''
    miCursor.execute("INSERT INTO DatosUsuarios VALUES (NULL, '"+miNombre.get()+
    "' , '"+miPass.get()+
    "' , '"+miApellido.get()+
    "' , '"+miDireccion.get()+
    "' , '"+textoEntry.get("1.0", END)+"')")
    '''
    parametros = miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),textoEntry.get("1.0", END)
    miCursor.execute("INSERT INTO DatosUsuarios VALUES(NULL,?,?,?,?,?)",parametros)
    
    miConexion.commit()

    messagebox.showinfo("BBDD","Registro insertado con exito")

#Leer
def leer():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT * FROM DatosUsuarios WHERE Id="+miId.get())
    elUsuario = miCursor.fetchall()
    limpiarCampos()
    for u in elUsuario:
        miId.set(u[0])
        miNombre.set(u[1])
        miApellido.set(u[2])
        miDireccion.set(u[3])
        miPass.set(u[4])
        textoEntry.insert(1.0, u[5])

    miConexion.commit()
    
#Actualizar
def actualizar():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    """
    miCursor.execute("UPDATE DatosUsuarios SET NombreUsuario= '"+miNombre.get()+
    "', Password= '"+miPass.get()+
    "', Apellido= '"+miApellido.get()+
    "', Direccion= '"+miDireccion.get()+
    "', Comentarios= '"+textoEntry.get("1.0", END)+
    "' WHERE ID= "+miId.get())
    """
    parametros = miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),textoEntry.get("1.0", END)
    miCursor.execute("UPDATE DatosUsuarios SET NombreUsuario=?, Password=?, Apellido=?, Direccion=?, Comentarios=? WHERE ID="+miId.get(),parametros)
   
    miConexion.commit()
    messagebox.showinfo("BBDD","Registro actualizado con exito")

def eliminar():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    miCursor.execute("DELETE FROM DatosUsuarios Where Id="+miId.get())
    miConexion.commit()
    messagebox.showinfo("BBDD","Registro borrado con exito")
#---------------Codigo para los menus--------------
root = Tk()
menuSuperior = Menu(root)
root.config(menu=menuSuperior,width=300, height=300)

#Opcion 1
bbddMenu = Menu(menuSuperior, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir",command=salirAplicacion)

#Opcion 2
borrarMenu = Menu(menuSuperior,tearoff=0)
borrarMenu.add_command(label="Borrar campos",command=limpiarCampos)
#Opcion 3
crudMenu = Menu(menuSuperior,tearoff=0)
crudMenu.add_command(label="Crear",command=crear)
crudMenu.add_command(label="Leer",command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=eliminar)
#Opcion 4
ayudaMenu = Menu(menuSuperior,tearoff=0)
ayudaMenu.add_command(label="Licensia")
ayudaMenu.add_command(label="Acerca de....")

#Agregamos las opcines creadas a la interfaz grafica
menuSuperior.add_cascade(label="BBDD",menu=bbddMenu)
menuSuperior.add_cascade(label="Borrar",menu=borrarMenu)
menuSuperior.add_cascade(label="CRUD",menu=crudMenu)
menuSuperior.add_cascade(label="Ayuda",menu=ayudaMenu)


#----------------------Codigo para el formulario label y entrys------
frame1 = Frame(root)
frame1.pack()
frame1.config(width=300,height=300)


miId = StringVar()
idLabel = Label(frame1,text="Id: ",justify="right")
idLabel.grid(row=0,column=0,sticky="e", padx=10, pady=10)
idEntry = Entry(frame1,textvariable=miId)
idEntry.grid(row=0,column=1,padx=10,pady=10)


miNombre=StringVar()
nombreLabel = Label(frame1,text="Nombre: ",justify="right")
nombreLabel.grid(row=1,column=0,sticky="e", padx=10, pady=10)
nombreEntry = Entry(frame1, textvariable=miNombre)
nombreEntry.grid(row=1,column=1,padx=10,pady=10)
nombreEntry.config(fg="red",justify="right")

miPass=StringVar()
passLabel = Label(frame1,text="Contrasena: ",justify="right")
passLabel.grid(row=2,column=0,sticky="e", padx=10, pady=10)
passEntry = Entry(frame1, textvariable=miPass)
passEntry.grid(row=2,column=1,padx=10,pady=10)
passEntry.config(show="*")

miApellido = StringVar()
apellidoLabel = Label(frame1,text="Apellido: ",justify="right")
apellidoLabel.grid(row=3,column=0,sticky="e", padx=10, pady=10)
apellidoEntry = Entry(frame1,textvariable=miApellido)
apellidoEntry.grid(row=3,column=1,padx=10,pady=10)

miDireccion = StringVar()
direccionLabel = Label(frame1,text="Direccion: ",justify="right")
direccionLabel.grid(row=4,column=0,sticky="e", padx=10, pady=10)
direccionEntry = Entry(frame1,textvariable=miDireccion)
direccionEntry.grid(row=4,column=1,padx=10,pady=10)

#miTexto = StringVar()
textoLabel = Label(frame1,text="Comentario: ",justify="right")
textoLabel.grid(row=5,column=0,sticky="e", padx=10, pady=10)
textoEntry = Text(frame1,width=16,height=5)
textoEntry.grid(row=5,column=1,padx=10,pady=10)
barraVertical = Scrollbar(frame1,command=textoEntry.yview)
barraVertical.grid(row=5,column=2,sticky="nsew")
textoEntry.config(yscrollcommand=barraVertical.set)

#----------------------Codigo para los botones------------
frame2 = Frame(root)
frame2.pack()

crearBoton = Button(frame2,text="Crear",command=crear)
crearBoton.grid(row=0,column=0, sticky="e",padx=10,pady=10)

leerBoton = Button(frame2,text="Leer",command=leer)
leerBoton.grid(row=0,column=1, sticky="e",padx=10,pady=10)

actualizarBoton = Button(frame2,text="Actualizar",command=actualizar)
actualizarBoton.grid(row=0,column=2, sticky="e",padx=10,pady=10)

borrarBoton = Button(frame2,text="Borrar",command=eliminar)
borrarBoton.grid(row=0,column=3, sticky="e",padx=10,pady=10)

root.mainloop()

