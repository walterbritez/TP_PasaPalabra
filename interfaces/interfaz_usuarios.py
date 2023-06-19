import tkinter as tk
from tkinter import messagebox
COLOR_BOTON = "#014bad"
COLOR_ENTRADA="#fefffe"
NOMBRE=0
CLAVE=1
ARCHIVO_USUARIOS="./archivos/usarios.csv"
IMG_ENTRAR_JUGAR="./imagenes/Entrar_jugar.png"
IMG_REGISTRAR="./imagenes/registrar.png"
IMG_CONTINUAR="./imagenes/Continuar.png"
CANT_NOMBRE_MAX=20
CANT_NOMBRE_MIN=4
CANT_CLAVE_MAX=12
CANT_CLAVE_MIN=6
CANT_CLAVE_VALIDA=4
CANT_NOMBRE_VALIDA=3
CRITERIO_USARIO="-"
CANT_USARIOS_MAX=4

def salir_iniciar():
    '''
    Cierra la primer interfaz 
    Hecho por: Walter Britez
    Modificado por: 
    Corregido por:
    '''
    vent_entrada.destroy()

def interfaz_salida():
    '''
    Genera una interfaz de salida si el usuario a ingresado el máximo de jugadores permitidos
    Pre:
    Post:
    Hecho por: Walter Britez
    Modificado por:
    Corregido por:
    '''
    global vent_salida
    vent_entrada.withdraw()
    vent_salida=tk.Toplevel()
    vent_salida.title("PasaPalabra Registrarse")
    vent_salida.resizable(0, 0)
    vent_salida.geometry('800x600+400+60')
    fondo= tk.PhotoImage(file=IMG_CONTINUAR)
    fondo_1=tk.Label(vent_salida,image=fondo).place(x=0,y=0,relwidth=1,relheight=1)

    #Boton

    boton=tk.Button(vent_salida,text="CONTINUAR!", cursor="hand2", bg=COLOR_BOTON,width=15 ,height=2, relief="flat",font=("Open Sans", 18, "bold"),
                    command=lambda: salir_iniciar())
    boton.place(x=295,y=459)
    
    vent_salida.mainloop()

def validar_salida(jugadores):
    '''
    Valida que se haya ingresado al menos un usario
    Pre:
    Post:
    Hecho por: Walter Britez
    Modificado por:
    Corregido por: 
    '''
    if not jugadores:
        messagebox.showwarning('Error', 'No ha ingresado ningún usuario\nPor favor, ingrese una cuenta!')
    else:
        salir_iniciar()

def regresar_entrada():
    vent_registrar.withdraw()
    vent_entrada.deiconify()

def validar_ingreso_usuario(usuario):
    '''
    Valida que el nombre que haya ingresado el usuario esté dentro de los paramétros permitidos
    Pre: Recibe una cadena
    Post: Devuelve una validación
    Hecho por: Walter Britez
    Modificado por:
    Corregido por:
    '''
    valido=0
    letras=0
    numeros=0
    simbolo=0
    if len(usuario)<=CANT_NOMBRE_MAX and len(usuario)>=CANT_CLAVE_MIN:
        for caracter in usuario:
            if caracter.isalpha() and letras==0:
                letras+=1
            elif caracter.isdigit() and numeros==0:
                numeros+=1
            elif caracter==CRITERIO_USARIO:
                simbolo+=1
        valido=letras+numeros+simbolo
        if valido>=CANT_NOMBRE_VALIDA:
            valido=True
        else:
            valido=False
    else:
        valido=False
    return valido

def validar_ingreso_clave(clave):
    '''
    Valida que la clave que el usuario haya ingresado esté dentro de los paramétros establecidos
    Pre: Recibe una cadena
    Post: Devuelve una validación
    Hecho por: Walter Britez
    Modificado por: 
    Corregido por:
    '''
    valido=0
    simbolos="#!"
    mayus=0
    minus=0
    numero=0
    simbolo=0
    if len(clave)<=CANT_CLAVE_MAX and len(clave)>=CANT_CLAVE_MIN:
        for caracter in clave:
            if caracter.isupper() and mayus==0:
                mayus+=1
            elif caracter.lower() and minus==0:
                minus+=1
            elif caracter.isdigit() and numero==0:
                numero+=1
            elif caracter in simbolos:
                simbolo+=1
        valido=simbolo+numero+minus+mayus
        if valido>=CANT_CLAVE_VALIDA:
            valido=True
        else:
            valido=False
    else:
        valido=False
    return valido

def registrar_contraseña(usuario_1,clave_1):
    '''
    Registra la entrada del usuario en un archivo csv si ambas son validas
    Pre: Recibe dos cadenas 
    Post:
    Hecho por: Walter Britez
    Modificado por:
    Corregido por:
    '''

    usuario=usuario_1.get()
    clave=clave_1.get()
    if validar_ingreso_clave(clave) and validar_ingreso_usuario(usuario):
        archivo=open(ARCHIVO_USUARIOS,"a+")
        archivo.write(f"\n{usuario},{clave}")
        archivo.close()
        messagebox.showinfo('Registrado' , 'Usuario y Clave correctos.\nVuelva a Ingresar con su nueva cuenta')
    else: 
        messagebox.showwarning('Error', 'Usaurio y/o contraseña NO cumplen con los requisitos\n')

def es_registrable(usuario,clave):
    no_registrado=False
    archivo=open(ARCHIVO_USUARIOS,"r")
    for linea in archivo:
        linea=linea.rstrip("\n").split(",")
        if linea[NOMBRE]==usuario.get():
            no_registrado=True
    archivo.close()
    if not no_registrado:
        registrar_contraseña(usuario,clave)
    else:
        messagebox.showwarning('Error', 'El nombre de usuario ya está registrado\nRegistrese con otro nombre')

def interfaz_registra_usuario():
    '''
    Genera una interfaz para registrar las entradas del usurio
    Pre:
    Post:
    Hecho por:
    Modificado por:
    Corregido por:
    '''
    global vent_registrar
    vent_entrada.withdraw()
    vent_registrar=tk.Toplevel()
    vent_registrar.title("PasaPalabra Registrarse")
    vent_registrar.resizable(0, 0)
    vent_registrar.geometry('800x600+400+60')
    fondo= tk.PhotoImage(file=IMG_REGISTRAR)
    fondo_1=tk.Label(vent_registrar,image=fondo).place(x=0,y=0,relwidth=1,relheight=1)

    usuario=tk.StringVar()
    contraseña=tk.StringVar()
    contraseña_1=tk.StringVar()

    #Entradas

    entrada = tk.Entry(vent_registrar, textvar=usuario, width=18, relief="flat", bg=COLOR_ENTRADA, font=("Open sans",15))
    entrada.config(fg = 'green', justify = 'center')
    entrada.place(x=480,y=311)

    entrada_1 = tk.Entry(vent_registrar, textvar=contraseña, width=18, relief="flat", bg=COLOR_ENTRADA, font=("Open sans",15))
    entrada_1.config(fg = 'green', justify = 'center',show="*")
    entrada_1.place(x=480,y=405)

    entrada_2 = tk.Entry(vent_registrar, textvar=contraseña_1, width=18, relief="flat", bg=COLOR_ENTRADA, font=("Open sans",15))
    entrada_2.config(fg = 'green', justify = 'center',show="*")
    entrada_2.place(x=480,y=510)


    #Botones

    boton=tk.Button(vent_registrar,text="REGISTRAR!", cursor="hand2", bg=COLOR_BOTON,width=14, relief="flat",font=("Open Sans", 16, "bold"),
                    command=lambda: es_registrable(usuario,contraseña))
    boton.place(x=25,y=485)

    boton_1=tk.Button(vent_registrar,text="INGRESAR", cursor="hand2", bg=COLOR_BOTON,width=14, relief="flat",font=("Open Sans", 16, "bold"),
                    command=lambda: regresar_entrada())
    boton_1.place(x=25,y=543)
    
    vent_registrar.mainloop()

def validar_ingreso(usuario_1,clave_1,jugadores):
    '''
    Valida las dos entradas del usuario 
    Pre: Recibe dos cadenas y una lista
    Post:
    Hecho por: Walter Britez
    Modificado por:
    Corregido por:
    '''
    usuario_valido = False
    archivo=open(ARCHIVO_USUARIOS,"r")
    if not usuario_1.get() in jugadores:
        for linea in archivo:
            linea=linea.rstrip("\n").split(",")
            if linea[NOMBRE]==usuario_1.get() and linea[CLAVE]==clave_1.get():
                usuario_valido=True
                jugadores.append(usuario_1.get())
        archivo.close()
        if len(jugadores)==CANT_USARIOS_MAX:
            interfaz_salida()
        if usuario_valido and len(jugadores)<CANT_USARIOS_MAX:
            messagebox.showinfo('Bienvenido' , 'Usuario y Clave correctos')
        elif not usuario_valido and len(jugadores)<CANT_USARIOS_MAX:
            messagebox.showwarning('Error', 'Usaurio y/o contraseña incorrecto/s\nsi no tiene cuenta por favor registrese')
    else:
        messagebox.showwarning('Error', 'El usuario ya se ha ingresado.')
  
def interfaz_entrada(jugadores):
    '''
    Genera la primer interfaz. Esta permitirá dos entradas
    Pre:Recibe una lista vacia
    Post: Genera una interfaz
    Hecho por: Walter 
    '''  

    global vent_entrada
    vent_entrada=tk.Tk()
    vent_entrada.title("PasaPalabra Entrada")
    vent_entrada.resizable(0, 0)
    vent_entrada.geometry("800x600+400+60")
    fondo=tk.PhotoImage(file=IMG_ENTRAR_JUGAR)
    fondo_1=tk.Label(vent_entrada, image=fondo).place(x=0,y=0,relheight=1,relwidth=1)
    
        
    #Variables
    

    usuario=tk.StringVar()
    clave=tk.StringVar()

    #Entradas

    entrada= tk.Entry(vent_entrada, textvar=usuario, width=18, relief="flat",bg=COLOR_ENTRADA, font=("Open sans",15))
    entrada.config(fg="green", justify="center")
    entrada.place(x=480, y=311)

    entrada_1=tk.Entry(vent_entrada, textvar=clave, width=18, relief="flat", bg=COLOR_ENTRADA, font=("Open sans",15))
    entrada_1.config(fg="green", justify="center", show="*")
    entrada_1.place(x=480, y=400)

    #Botones

    boton=tk.Button(vent_entrada, text="REGISTRARSE", cursor="hand2", bg=COLOR_BOTON, width=11, relief="flat", font=("Open sans",16,"bold"),
                    command=lambda: interfaz_registra_usuario())
    boton.place(x=66,y=522)

    boton_1=tk.Button(vent_entrada,text="INGRESAR", cursor="hand2", bg=COLOR_BOTON,width=10, relief="flat",font=("Open Sans", 16, "bold"),
                    command=lambda: (validar_ingreso(usuario,clave,jugadores)))
    boton_1.place(x=423,y=464)

    boton_2=tk.Button(vent_entrada,text="INICIAR", cursor="hand2", bg=COLOR_BOTON,width=10, relief="flat",font=("Open Sans", 16, "bold"),
                    command=lambda : validar_salida(jugadores))
    boton_2.place(x=600,y=464)
    vent_entrada.mainloop()
    return jugadores

def iniciar_interfaz():
    '''
    Pre:
    Post: Devuelve una lista 
    Hecho por: Waltre Britez
    Modificado por:
    Corregido por:
    '''
    jugadores=[]
    jugadores=interfaz_entrada(jugadores)
    return jugadores