from tkinter import *
from tkcalendar import *
from PIL import ImageTk, Image
from tkinter import ttk # esto es para crear un desplegable de opciones
import tkinter.messagebox
from model.tabla import crear_tabla, borrar_tabla, contacto, acerca, volver
from model.conencion import conectar
from model.datosCliente import DATOS

raiz = Tk()
raiz.title("Prospecto")
raiz.resizable(1,1)
raiz.config(bg="cyan2")
raiz.geometry("+100+10")
icono=PhotoImage(file="D:\\ERIK\\CARPETA_PYTHON\\PYTHON\\PROYECTOS\\PROYECTO 1\\appCajaIca\\utils\\iconoCaja.png") # Agregar un icono 
raiz.iconphoto(True,icono)


# =====================================     CREAMOS LA BARRA DE MENÚ      =====================================
# LO PRIMERO, SI EXISTE UNA BASE DE DATOS SE ELIMINA PARA INICIAR CON UN REGISTRO VACIO

class inicio ():
    def __init__(self):
        try:
            self.conexion =conectar()
            self.sql="DROP DATABASE EVALUACION2"
            self.conexion.mycursor.execute(self.sql)
            self.conexion.cerrar()
            
        except:
            pass
           
inicio()


    
# ********* INICIO ******

barramenu = Menu(raiz)
raiz.config(menu=barramenu)
bdmenu = Menu(barramenu, tearoff=0)
bdmenu.add_command(label="Crear registro", command=crear_tabla)
bdmenu.add_command(label="Eliminar registro", command=borrar_tabla)
bdmenu.add_command(label="Salir", command=raiz.destroy)

bdayuda = Menu(barramenu, tearoff=0)
bdayuda.add_command(label="Contacto",command=contacto)
bdayuda.add_command(label="Acerca de...", command=acerca)

barramenu.add_cascade(label="Inicio", menu=bdmenu)
barramenu.add_cascade(label="Ayuda",menu=bdayuda)



# =====================================           PRIMER FRAME          ========================================
 
frame=LabelFrame(raiz,width=22)
frame.pack(fill="x") # esta opcion es para expndir(capitulo43)

Label(frame, text=" Evaluación de nuevo cliente",bg="cyan2",fg="darkblue",font=("comic Sans MS", 16),width=43,pady=1,padx=1).grid(column=0, row=0, sticky="e")


# ****************    CLIENTE     ***************
frame0 = Frame(raiz)
frame0.pack(fill="x") 
frame0.config(bg="cyan3")

cliente = Label(frame0, text='Cliente ',bg="cyan3",fg="black", font=("Arial black",10))
cliente.grid(column=0, row=0, sticky="w",pady=5, padx=20)

opciones1=["Nuevo","Recurrente","Otro"]
cmbOpciones1 = ttk.Combobox(frame0,values=opciones1,width=16)
cmbOpciones1.grid(column=1, row=0,padx=20)



# =====================================         DATOS DEL CLIENTE       =======================================



# Con el siguiente código se crea el frame

a = Frame(raiz)
a.pack(fill="x")
a.config(bg="cyan3")

# Con los siguientes códigos se crea los datos de cada frame
marco_datos_cliente = LabelFrame(a, text="Datos del cliente", bg="cyan3",fg="blue4",font=("Arial black",10))
marco_datos_cliente.grid(column=0, row=1,padx=20, sticky="w")

lbl_nombre=Label(marco_datos_cliente, text="Nombre completo", bg="cyan3",fg="black",font=("Arial", 8))
lbl_nombre.grid(column=0, row=2,padx=10)
entry_nombre = Entry(marco_datos_cliente,width= 25)
entry_nombre.grid(column=0, row=3,padx=10)

lbl_primer_apellido=Label(marco_datos_cliente, text="Primer apellido", bg="cyan3", fg="black", font=("Arial",8))
lbl_primer_apellido.grid(column=1, row=2,padx=15)
entry_primer_apellido=Entry(marco_datos_cliente,width= 25)
entry_primer_apellido.grid(column=1,row=3, padx=10)

lbl_segundo_apellido=Label(marco_datos_cliente, text="Segundo apellido", bg="cyan3", fg="black", font=("Arial",8))
lbl_segundo_apellido.grid(column=2, row=2,padx=10)
entry_segundo_apellido=Entry(marco_datos_cliente,width= 25)
entry_segundo_apellido.grid(column=2,row=3,padx=10)

lbl_dni = Label(marco_datos_cliente, text="DNI", bg="cyan3", fg="black", font=("Arial", 8))
lbl_dni.grid(column=0, row=4,padx=10)
entry_dni = Entry(marco_datos_cliente,width= 25)
entry_dni.grid(column=0, row=5, padx=10)

lbl_correo = Label(marco_datos_cliente, text="Correo electrónico", bg="cyan3", fg="black", font=("Arial", 8))
lbl_correo.grid(column=1, row=4,columnspan=2,padx=10)
entry_correo = Entry(marco_datos_cliente,width= 53)
entry_correo.grid(column=1, row=5, columnspan=2, padx=10)

lbl_direccion=Label(marco_datos_cliente, text="Dirección", bg="cyan3", fg="black", font=("Arial",8))
lbl_direccion.grid(column=0, row=6,columnspan=2,padx=10)
entry_direccion=Entry(marco_datos_cliente,width= 53) #width-- ancho de la celda, height--> largo de la celda
entry_direccion.grid(column=0,row=7,padx=10, columnspan=2)# columnspan--> expande la columna

lbl_celular = Label(marco_datos_cliente, text="Celular", bg="cyan3",fg="black", font=("Arial",8))
lbl_celular.grid(column=2,row=6,padx=10)
entry_celular = Entry(marco_datos_cliente,width= 25)
entry_celular.grid(column=2, row=7,padx=10)

# calendario
lbl_nacimiento = Label(marco_datos_cliente, text="Fecha de nacimiento", bg="cyan3",fg="black", font=("Arial",8))
lbl_nacimiento.grid(column=0, row=8,padx=10)
entry_calendario = DateEntry(marco_datos_cliente,width= 22) # Se importa el calendario
entry_calendario.grid(column=0, row=9,padx=10)

# CREAR UN DESPLEGABLE DE OPCIONES
# Estado civil
lbl_estado_civil = Label(marco_datos_cliente, text="Estado civil", bg="cyan3",fg="black", font=("Arial",8))
lbl_estado_civil.grid(column=1, row=8,padx=10)
opciones_estado_civil = ["Soltero(a)","Casado(a)"]
cmbOpciones_estado_civil= ttk.Combobox(marco_datos_cliente,values=opciones_estado_civil,width= 22)
cmbOpciones_estado_civil.grid(column= 1, row=9,padx=10 )

# Género
lbl_genero = Label(marco_datos_cliente, text="Género", bg="cyan3",fg="black", font=("Arial",8))
lbl_genero.grid(column=2,row=8, padx=10)
opciones_genero=["Masculino","Femenino","No me decido"]
cmbOpciones_genero = ttk.Combobox(marco_datos_cliente,values=opciones_genero,width= 22)
cmbOpciones_genero.grid(column=2, row=9,padx=10,pady=2)
 

# ***************   INGRESOS      ****************
frame1 = Frame(raiz)
frame1.pack(fill="x") 
frame1.config(bg="cyan3")

marcoIngresos = LabelFrame(frame1, text=" INGRESOS",bg="cyan3",fg="blue4",font=("Arial black",10))
marcoIngresos.grid(column=0, row=0,padx=20,sticky="w")

ingresos = Label(marcoIngresos,text="Ingresos: ", bg="cyan3", fg="black", font=("Arial black",10))
ingresos.grid(column=0, row=2, sticky="w",pady=10,padx=15)

entry_ingreso = Entry(marcoIngresos)
entry_ingreso.grid(column=1,row=2,padx=5)

otros_ingresos = Label(marcoIngresos,text="Otros Ingresos: ", bg="cyan3", fg="black", font=("Arial black",10))
otros_ingresos.grid(column=0, row=3, sticky="w",pady=5)

entry_otroingreso = Entry(marcoIngresos)
entry_otroingreso.grid(column=1,row=3,padx=5)

ingresototal = Label(marcoIngresos,text="",bg="gray75", fg="black", font=("Arial black",10), width=13)
ingresototal.grid(column=1,row=4,padx=5)

rpt=0
def total():
    try:
        global rpt
        n1=eval(entry_ingreso.get())
        n2=eval(entry_otroingreso.get())
        rpt=round(n1+n2,3)
        ingresototal.configure(text=str(rpt))
        return rpt
        
    except:
        tkinter.messagebox.showerror("ERROR","Datos erróneos o vacios")
        

btn_total = Button(marcoIngresos, text=" Total ",bg= "bisque2",border=4,fg="black",font=("Arial black",8),command=total)
btn_total.grid(column=0, row=4, pady=10,sticky="e")


# =====================================          FRAME DOS           =========================================

# *****************      GASTOS     **************
#frame2=Frame(raiz)
#frame2.pack(fill="x")
#frame2.config(bg="cyan3")


marcoGastos = LabelFrame(frame1, text=" GASTOS",bg="cyan3",fg="blue4",font=("Arial black",10))
marcoGastos.grid(column=0, row=1,padx=20, sticky="w")

lblTotal=Label(marcoGastos, text=" TOTAL : ",bg="cyan3",fg="black",font=("Arial black",10)).grid(column=0, row=2, pady=10, sticky="e")

gastofinal = Label(marcoGastos,text="", bg="gray75", fg="black", font=("Arial black",10), width=13)
gastofinal.grid(column=1,row=2,padx=5)


# BOTON PARA EVALUAR UN NUEVO CLIENTE
def nuevo():
    volver()
    
    cmbOpciones1.delete(0,END)
    entry_ingreso.delete(0,END) 
    entry_otroingreso.delete(0,END) 
    ingresototal.configure(text="")
    gastofinal.configure(text="")
    entry_cuota.delete(0,END)
    excedente.configure(text="")
    ratio.configure(text="")
    observacion.configure(text="",bg="gray75")
    btn_nuevo.configure(state=DISABLED,bg="gray77")
    

btn_nuevo = Button(frame0, text="Nuevo",bg= "bisque2",font=("Arial black",8), border=4, width=8, command=nuevo)
btn_nuevo.grid(column=3, row=0, pady=10, padx=30)


                # *******************      VENTANA2        *********************
# declaramos variable para usar posteriormente
resultado=0
nuevoResultado=0 # Esta variable se usará para calcular el excedente
excedent =0
rat = 0
def ingresarGastos():
    
    try:
        
        gastofinal.configure(text="")
        excedente.configure(text="")
        ratio.configure(text="")
        observacion.configure(text="",bg="gray75")
        
        global resultado
        ventana2=Toplevel()
        ventana2.title("Gastos")
        ventana2.geometry("+500+200")
        ventana2.resizable(1,1)
        ventana2.config(bg="lightblue")
        
        ventana2.iconbitmap('D:\\ERIK\\CARPETA_PYTHON\\PYTHON\\PROYECTOS\\PROYECTO 1\\appCajaIca\\utils\\iconoCaja.png') # Para agregar el ícono
        
        frameventana = Frame(ventana2)
        frameventana.pack(fill="x")
        frameventana.config(bg="cyan4")
        
        marcoVentana = LabelFrame(frameventana, text=" INGRESAR GASTOS",bg="cyan4",fg="gray15",font=("Arial black",10))
        marcoVentana.grid(column=0, row=0, pady=15,padx=15, sticky="w")
        
        # LOS ENTRYS DE DESCRIPCION Y MONTO
            # DESCRIPCIÓN
        entry_descipcion=Entry(marcoVentana)
        entry_descipcion.grid(column=0,row=1, padx=5)
        
        lbl_descripcion=Label(marcoVentana, text="Descripción", bg="cyan4", fg="black", font=("Arial",10))
        lbl_descripcion.grid(column=0, row=2)
        
            # MONTO
        entry_monto=Entry(marcoVentana)
        entry_monto.grid(column=1,row=1, pady= 5, padx=5)
        
        lbl_monto=Label(marcoVentana, text="Monto (S/.)", bg="cyan4", fg="black", font=("Arial",10))
        lbl_monto.grid(column=1, row=2)

            # CUADRO DE GASTOS
        cuadro = ttk.Treeview(marcoVentana, columns=("col1"))
        cuadro.grid(column=0, row=4, columnspan=3, pady=10, sticky="nse")
        
                # Colocaremos un scrollbar para deslizar y visualizar
        scroll = ttk.Scrollbar(marcoVentana,orient=VERTICAL,command=cuadro.yview)
        scroll.place(x=260, y=95, height=240)
        cuadro.configure(yscrollcommand=scroll.set)
        
        cuadro.column("#0",width=180)
        cuadro.column("col1",width=95, anchor=CENTER)

        cuadro.heading("#0", text="Descripción", anchor=CENTER)
        cuadro.heading("col1", text="Monto (S/.)", anchor=CENTER)
        
                # SUB TOTAL
        lblSubTotal=Label(marcoVentana, text=" SUB TOTAL : ",bg="cyan4",fg="black",font=("Arial black",10)).grid(column=0, row=5, sticky="e")
        
        gastoSubtotal = Label(marcoVentana,text="", fg="black", font=("Arial black",10), width=13)
        gastoSubtotal.grid(column=1,row=5,padx=5)
        
    # NOTA: Lo que haremos es recuperar los datos, si existen, sino estara vacio
    # RECUPERAMOS LOS DATOS DE LA BD
        conexion = conectar()
        lista_gastos=[]
        sql="SELECT * FROM GASTOS"
        conexion.mycursor.execute(sql)
        lista_gastos = conexion.mycursor.fetchall()
        conexion.cerrar()
        
    # MOSTRAMOS LOS DATOS EN EL CUADRO DE GASTOS, SINO HAY ESTARÁ EN BLANCO
        
        for x in lista_gastos:
            cuadro.insert("",END, text=x[1], values= eval(x[2]))
            resultado+=eval(x[2]) # suma los montos que ya estan guardados
            
        gastoSubtotal.configure(text=str(resultado)) 

    # **********************   INSERTAR DATOS DE LOS GASTOS  ********************
        def insertar():
            try:
                global resultado
                desc=entry_descipcion.get()
                mont=entry_monto.get()
                
                # PARA INSERTAR LOS DATOS EN LA TABLA 
                try:
                    eval(desc)/eval(desc)==1
                    return tkinter.messagebox.showerror("ERROR","Datos erróneos\n\n Descripcion-->Texto \n Monto--> Moneda")
                
                except:
                    cuadro.insert("",END, text=desc, values= eval(mont))
                    resultado+=eval(mont) 
                    gastoSubtotal.configure(text=str(resultado))
                        # LIMPIA LA PANTALLA
                    entry_descipcion.delete(0,END)
                    entry_monto.delete(0,END)
                    print(type(desc))
                    
                #except SyntaxError:
                   # return tkinter.messagebox.showerror("ERROR","Falta completar los datos") ---> evita que se envia la descripcion vacio, esta para evaluar si es util o no
              
                  
                ##########################################    
                # ingresar gastos a la base de datos
                conexion = conectar()
                sql = "INSERT INTO GASTOS(DESCRIPCION,MONTO) VALUES(%s,%s)"
                valores = [desc,mont]
                conexion.mycursor.execute(sql,valores)
                conexion.cerrar()
                ##########################################
            
            except:
                tkinter.messagebox.showerror("ERROR","Datos erróneos\n\n Descripcion-->Texto \n Monto--> Moneda")
            
        btn_insertar = Button(marcoVentana, text="Insertar",width=12, bg= "bisque2",border=4,font=("Arial",10),command=insertar)
        btn_insertar.grid(column=0, row=3,padx=3, pady=5)
        
        
    # ***********************    EDITAR LOS DATOS    ****************************
        
        def editar():
            
            try:
            
                # Deshabilitaremos los botones que no corresponden a editar
                btn_insertar.configure(state=DISABLED,bg="gray77",text="")
                btn_eliminar.configure(state=DISABLED,bg="gray77",text="")
                btn_guardar.configure(state=DISABLED,bg="gray77",text="")
                
                # **** MUESTRA LOS DATOS QUE SE QUIEREN MODIFICAR EN LOS ENTRYS ****
                global resultado
            
                entry_descipcion.delete(0,END) # Caundo se vuelve a llamar a editar() limpia los valores existentes
                entry_monto.delete(0,END)
                
                editarDescripcion=cuadro.item(cuadro.selection())['text']
                editarMonto = cuadro.item(cuadro.selection())['values'][0]
                
                entry_descipcion.insert(0,editarDescripcion) # Se asignan los nuevos valores a descripcion y monto para ser guardados posteriormente
                entry_monto.insert(0,editarMonto)
                
                # ******    GUARDAR LOS CAMBIOS REALIZADOS     ******* 
                # ESTE CODIGO guardar_cambio ES SOLO PARTE DE LA FUNCION EDITAR, NO ES PARTE DEL CRUD
                
                def guardar_cambios():
                    global resultado
                    
                    # Recoge los nuevos valores
                    nuevaDescripcion=entry_descipcion.get()
                    nuevoMonto=entry_monto.get()
                    
                    lista_gastos=[]
                    conexion = conectar()
                    sql="SELECT * FROM GASTOS"
                    conexion.mycursor.execute(sql)
                    lista_gastos = conexion.mycursor.fetchall()
                    conexion.cerrar()
                    
                    # GUARDA LOS CAMBIOS EN LA BASE DE DATOS
                    
                    for x in lista_gastos:
                        if x[1]== editarDescripcion:
                            nuevoid=x[0]
                            conexion = conectar()
                            sql=f"""UPDATE GASTOS SET DESCRIPCION='{nuevaDescripcion}', MONTO='{nuevoMonto}'  WHERE id= '{nuevoid}'"""
                            conexion.mycursor.execute(sql)
                            conexion.cerrar()
                    
                    
                    mostrarCambiosTabla() # LLamamos a la funcion, para cargar los nuevos datos en la tabla
                    btn_guardar_cambios.destroy() # Cuando terminamos de realizar los cambios el boton guardar_cambios se destruye para volver a un inicio(editar)

                    
                    # Volvemos habilitar los botones 
                    btn_insertar.configure(state=NORMAL,bg= "bisque2",text="Insertar")
                    btn_eliminar.configure(state=NORMAL,bg= "bisque2",text="Eliminar")
                    btn_guardar.configure(state=NORMAL,bg= "bisque2",text="Guardar")
        
                
                btn_guardar_cambios = Button(marcoVentana, text="Guardar cambios",bg= "bisque2",border=4,font=("Arial",9),width=13,command=guardar_cambios)
                btn_guardar_cambios.grid(column=1, row=3, padx=5, pady=5)
                
                
                # MUESTRA EN LA TABLA(CUADRO) LOS NUEVOS VALORES
                def mostrarCambiosTabla():
                    global resultado
                    resultado=0
                    cuadro.delete(*cuadro.get_children()) # Con este código se limpia todos los datos que estan en la tabla
                    
                    # Con este codigo cargamos denuevo los datos de la BD para mostrarlo en la tabla(cuadro)
                    nueva_lista_gastos=[]
                    conexion = conectar()
                    sql="SELECT * FROM GASTOS"
                    conexion.mycursor.execute(sql)
                    nueva_lista_gastos = conexion.mycursor.fetchall()
                    conexion.cerrar()
                    for x in nueva_lista_gastos:
                        cuadro.insert("",END, text=x[1], values= eval(x[2]))
                        resultado+=eval(x[2])
                    gastoSubtotal.configure(text=str(resultado))
                    
                    # Limpiamos los entrys
                    entry_descipcion.delete(0,END) 
                    entry_monto.delete(0,END)
            
            except:
                tkinter.messagebox.showwarning("Alerta", " Debe seleccionar el dato para editar")
                btn_insertar.configure(state=NORMAL)
                btn_eliminar.configure(state=NORMAL)
                btn_guardar.configure(state=NORMAL)
            
            
        btn_editar = Button(marcoVentana, text="Editar",width=12, bg= "bisque2",border=4,font=("Arial",10),command=editar)
        btn_editar.grid(column=1, row=3, padx=5, pady=5)
        
        
        # ojo: cuando no existe registro en el cuadro y se comete un error debe de salir un mensaje que indique que no hay ningun registro
        
    # **********************  ELIMINAR UN REGISTRO   ****************************
        
        def eliminar_registro():
             # **** MUESTRA LOS DATOS QUE SE QUIEREN ELIMINAR EN LOS ENTRYS ****
            global resultado
        
            entry_descipcion.delete(0,END) #  limpia los valores existentes
            entry_monto.delete(0,END)
            
            eliminarDescripcion=cuadro.item(cuadro.selection())['text']
            #eliminarMonto = cuadro.item(cuadro.selection())['values'][0]
            
            if eliminarDescripcion:
            
                #entry_descipcion.insert(0,editarDescripcion) # Se asignan los nuevos valores a descripcion y monto para ser guardados posteriormente
                #entry_monto.insert(0,editarMonto)
                
                eliminar_lista_gastos=[]
                conexion = conectar()
                sql="SELECT * FROM GASTOS"
                conexion.mycursor.execute(sql)
                eliminar_lista_gastos = conexion.mycursor.fetchall()
                conexion.cerrar()
                for x in eliminar_lista_gastos:
                    if x[1]== eliminarDescripcion:
                        eliminar_id=x[0]
                        conexion = conectar()
                        sql=f"""DELETE FROM GASTOS   WHERE id= '{eliminar_id}'"""
                        conexion.mycursor.execute(sql)
                        conexion.cerrar()
                
                # MUESTRA EN LA TABLA(CUADRO) LOS NUEVOS VALORES
                # El método mostrarCambiosTabla() se podria mejorar o reducir si se trabaja con herencia, eso para tener un código más limpio
                # Se esta repitiendo el mismo código en los botones  de editar y eliminar
                
                def mostrarCambiosTabla():
                    global resultado
                    resultado=0
                    cuadro.delete(*cuadro.get_children()) # Con este código se limpia todos los datos que estan en la tabla
                    
                    # Con este codigo cargamos denuevo los datos de la BD para mostrarlo en la tabla(cuadro)
                    nueva_lista_gastos=[]
                    conexion = conectar()
                    sql="SELECT * FROM GASTOS"
                    conexion.mycursor.execute(sql)
                    nueva_lista_gastos = conexion.mycursor.fetchall()
                    conexion.cerrar()
                    for x in nueva_lista_gastos:
                        cuadro.insert("",END, text=x[1], values= eval(x[2]))
                        resultado+=eval(x[2])
                    gastoSubtotal.configure(text=str(resultado))
                
                mostrarCambiosTabla()
            else:
                tkinter.messagebox.showwarning("Alerta", " Debe seleccionar el dato para eliminar")
            
            
        btn_eliminar = Button(marcoVentana, text="Eliminar",width=12, bg= "bisque2",border=4,font=("Arial",10), command=eliminar_registro)
        btn_eliminar.grid(column=0, row=6,padx=5, pady=5)
        
        
    # ***********************  GUARDAR LOS GASTOS INGRESADOS   **********************  

        def guardar():
            global nuevoResultado
            global resultado
            gastofinal.configure(text=str(resultado))
            nuevoResultado= resultado
            
            
            # Muestra los resultados del excedente
            ingresos=rpt
            gastos=nuevoResultado
            excedent=ingresos-gastos
            excedent=round(excedent,3)
            excedente.configure(text=str(excedent))
            
            resultado=0
            ventana2.destroy()
                
        
        btn_guardar = Button(marcoVentana, text="Guardar",width=12, bg= "bisque2",border=4,font=("Arial",10), command=guardar)
        btn_guardar.grid(column=1, row=6,padx=5, pady=5)
    
    except:
        ventana2.destroy() # Se elimina la ventana2 si sale un error
        tkinter.messagebox.showerror("Error", "No existe un registro.\nDebe crear uno.\n1. Inicio\n2. Crear registro")
        

insertargastos= Button(marcoGastos, text=" Ingresar gastos",bg= "bisque2",border=4,fg="black",font=("Arial black",8), command=ingresarGastos)
insertargastos.grid(column=0, row=1, sticky="w")


#  =========================================            FRAME TRES              ===========================================
# *****************           RESULTADOS         **************************
#frame0=Frame(raiz)
#frame3.pack(fill="x")
#frame3.config(bg="cyan3")

marcoResultado=LabelFrame(frame1, text=" RESULTADOS",bg="cyan3",fg="blue4",font=("Arial black",10))
marcoResultado.grid(column=1, row=0,padx=13,pady =10, sticky="w")

Label(marcoResultado, text=" Cuota ",bg="cyan3",fg="black",font=("Arial black",10)).grid(column=0, row=1, sticky="w")
entry_cuota = Entry(marcoResultado)
entry_cuota.grid(column=3,row=1,pady=5,padx=5)

Label(marcoResultado, text=" Excedentes ",bg="cyan3",fg="black",font=("Arial black",10)).grid(column=0, row=3)
excedente=Label(marcoResultado,text="", bg="gray75", fg="black",font=("Arial black",10),width=13)
excedente.grid(column=3, row=3, padx=5, pady=5, sticky="e")

Label(marcoResultado, text=" Ratio (%)",bg="cyan3",fg="black",font=("Arial black",10)).grid(column=0, row=4, sticky="w")
ratio=Label(marcoResultado,text="", bg="gray75", fg="black",font=("Arial black",10),width=13)
ratio.grid(column=3, row=4, padx=4, pady=5, sticky="e")

observacion=Label(marcoResultado,text="",bg="gray75", fg="black",font=("Arial black",10),width=13, height=2)
observacion.grid(column=3, row=5, padx=5, pady=5, sticky="e")


def evaluar_cliente():
    
    global nuevoResultado
    
    try:
        ingresos=rpt
        gastos=nuevoResultado
        excedent=ingresos-gastos
        
        cuota=eval(entry_cuota.get())
        
        rat=(cuota/excedent)*100
        rat=round(rat,2)
    
        
        global cmbOpciones1
        opc=cmbOpciones1.get()
        if opc=="":
            tkinter.messagebox.showwarning("Alerta", " Falta seleccionar el tipo de cliente ha evaluar")
            
        else:
            ratio.configure(text=str(rat))
            
            if opc=="Nuevo":
                if rat<=75:
                    observacion.configure(bg="green",text="Aprobado \n \U0001F600")
                    
                else:
                    observacion.configure(bg="red",text="Desaprobado \n \U0001F622")
            
            if opc=="Recurrente":
                if rat<=80:
                    observacion.configure(bg="green",text="Aprobado \n \U0001F600")
                else:
                    observacion.configure(bg="red",text="Desaprobado \n \U0001F622")
                    
            if opc=="Otro":
                if rat<=90:
                    observacion.configure(bg="green",text="Aprobado \n \U0001F600")
                else:
                    observacion.configure(bg="red",text="Desaprobado \n \U0001F622")

        # SE HABILITA EN BOTON "NUEVO"
        btn_nuevo.configure(state=NORMAL,bg= "bisque2")
    except:
        tkinter.messagebox.showerror("ERROR","Datos erróneos o vacios")
        btn_nuevo.configure(state=DISABLED,bg="gray77")
        
    
btn_calcular = Button(marcoResultado, text="Evaluar",bg= "bisque2",font=("Arial black",8), border=4, width=10, command=evaluar_cliente)
btn_calcular.grid(column=3, row=2, pady=10)

# EN EL INICIO EL BOTON "NUEVO" ESTARÁ DESHABILITADO
btn_nuevo.configure(state=DISABLED,bg="gray77")



# LOGO, PIE DE PAGINA
marcoImagen=LabelFrame(frame1,bg="cyan3",fg="blue4",font=("Arial black",10))
marcoImagen.grid(column=1, row=1,pady =15, padx=35, sticky="w")

image = Image.open("D:\\ERIK\\CARPETA_PYTHON\\PYTHON\\PROYECTOS\\PROYECTO 1\\appCajaIca\\utils\\iconoCaja.png")
image = image.resize((190,190))

img = ImageTk.PhotoImage(image)
lbl_img = Label(marcoImagen,image=img)
lbl_img.grid(column=1, row=1, rowspan=2, pady=1,padx=1)




# EXPORTAR LOS DATOS TODOS LOS DATOS EN UN PDF

# Ingresar datos a la base de datos

def guardarDatos():
    
    try:
    
        conexion = conectar()
        
        sqlEliminar=f"""DELETE FROM DATOS"""
        conexion.mycursor.execute(sqlEliminar)
        
        sqlEliminar1=f"""DELETE FROM RESULTADOS """
        conexion.mycursor.execute(sqlEliminar1)
        
        # ......   PRIMERO AGREGAMOS LOS DATOS A LA BD   .......
        # DATOS
        nombre = entry_nombre.get()
        apelledo_paterno = entry_primer_apellido.get()
        apellido_materno = entry_segundo_apellido.get()
        dni = entry_dni.get() 
        correo = entry_correo.get()
        direccion = entry_direccion.get()
        celular = entry_celular.get()
        calendario = entry_calendario.get()
        estado_civil = cmbOpciones_estado_civil.get()
        genero = cmbOpciones_genero.get()
        
        # GASTOS--> Ya se cargó estos datos con la funcion de INGRESAR GASTOS (linea 345)
        
        # RESULTADOS
        global nuevoResultado
    
        ingresos=rpt
        gastos=nuevoResultado
        
        tipoCliente =cmbOpciones1.get()
        cuotaMonto = entry_cuota.get()
        excedenteResultado = ingresos-gastos
        ratioResultado = round((eval(cuotaMonto)/excedenteResultado)*100,2)
        observacionFinal = ""
            
        if tipoCliente=="Nuevo":
            if (eval(cuotaMonto)/excedenteResultado)*100<=75:
                observacionFinal= "Aprobado"            
            else:
                observacionFinal= "Desaprobado"
                
        if tipoCliente=="Recurrente":
            if (eval(cuotaMonto)/excedenteResultado)*100<=80:
                observacionFinal= "Aprobado"
            else:
                observacionFinal= "Desaprobado"
                        
        if tipoCliente=="Otro":
            if (eval(cuotaMonto)/excedenteResultado)*100<=90:
                observacionFinal= "Aprobado"
            else:
                observacionFinal= "Desaprobado"
        

        
        sql = "INSERT INTO DATOS(NOMBRES,APELLIDO_PATERNO,APELLIDO_MATERNO,DNI,CORREO,DIRECCION,CELULAR,FECHA_DE_NACIMIENTO,ESTADO_CIVIL,GENERO) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        valores = [nombre,apelledo_paterno,apellido_materno,dni,correo,direccion,celular,calendario,estado_civil,genero]
        conexion.mycursor.execute(sql,valores)
        
        sql1 = "INSERT INTO RESULTADOS(CLIENTE,CUOTA,EXCEDENTE,RATIO,OBSERVACIÓN) VALUES(%s,%s,%s,%s,%s)"
        valores1 = [tipoCliente,cuotaMonto,excedenteResultado,ratioResultado,observacionFinal]
        conexion.mycursor.execute(sql1,valores1)
        conexion.cerrar()
        
        tkinter.messagebox.showwarning("Alerta", " Se guardo correctamente")
    
    except:
        tkinter.messagebox.showwarning("Alerta", " Falta completar los datos")
        
    


btn_datos = Button(frame0, text=" Guardar datos ",bg= "bisque2",border=4,fg="black",font=("Arial black",8),command=guardarDatos)
btn_datos.grid(column=4, row=0, pady=10,sticky="e")
    
#falta aumentar los botones de editar eliminar 
# falta exporter en pdf para imprimir










raiz.mainloop()


