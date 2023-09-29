from model.conencion import conectar, crear_bd
import tkinter.messagebox
def crear_tabla():
    try:
        conexion = crear_bd() # con esta opcion se crea una base de datos
        conexion = conectar() # con esta opcion se crea la tabla
        
        sql = """CREATE TABLE DATOS(
                id INT AUTO_INCREMENT PRIMARY KEY,
                NOMBRES VARCHAR(150),
                APELLIDO_PATERNO VARCHAR(150),
                APELLIDO_MATERNO VARCHAR(150),
                DNI INT,
                CORREO VARCHAR(150),
                DIRECCION VARCHAR(50),
                CELULAR INT(50),
                FECHA_DE_NACIMIENTO DATE,
                ESTADO_CIVIL VARCHAR(50),
                GENERO VARCHAR(150))
                """
        conexion.mycursor.execute(sql)
        
        sql = """CREATE TABLE GASTOS(
                id INT AUTO_INCREMENT PRIMARY KEY,
                DESCRIPCION VARCHAR(150),
                MONTO VARCHAR(50))
                """
        conexion.mycursor.execute(sql)
        
        sql = """CREATE TABLE RESULTADOS(
                id INT AUTO_INCREMENT PRIMARY KEY,
                CLIENTE VARCHAR(30),
                CUOTA FLOAT,
                EXCEDENTE FLOAT,
                RATIO FLOAT,
                OBSERVACIÓN VARCHAR(150))
                """
        conexion.mycursor.execute(sql)
        
        conexion.cerrar()
        tkinter.messagebox.showinfo("Conexión","Se creo el registro correctamente")
        
    except:
        tkinter.messagebox.showerror("Error", "El registro ya existe")  
    
def borrar_tabla():
    #Con esto comprobamos si existe la base de datos para eliminarlo, sino existe pasa a la excepción
    try:
        conexion =conectar()
        sql="DROP DATABASE EVALUACION2"
        r=tkinter.messagebox.askquestion("Alerta","Estas seguro de borrar el registro?")
        if r=="yes":
            conexion.mycursor.execute(sql)
            conexion.cerrar()
            tkinter.messagebox.showinfo("Mensaje","El registro se borró correctamente")
        else:
            tkinter.messagebox.showinfo("Mensaje","Buena opción")
    except:
        tkinter.messagebox.showerror("Error", "No existe un registro")
        
def contacto():
    tkinter.messagebox.showinfo("Contacto","Contacto: \n Ing. Erik Torres \n Cel: 964626322")
    
def acerca():
    tkinter.messagebox.showinfo("Acerca","El programa te ayudará a evaluar si el cliente es apto o no \n Si existen dudas o errores comunicarse al número de contacto")
    
def volver(): # hace referencia al boton nuevo
    conexion =conectar()
    
    # PRIMERO BORRAMOS LA TABLA
    sql="DROP TABLE DATOS"
    sql1="DROP TABLE GASTOS"
    sql2="DROP TABLE RESULTADOS"
    r=tkinter.messagebox.askquestion("Alerta","Se borrará el registro guardado. \n ¿Desea continuar?")
    if r=="yes":
        conexion.mycursor.execute(sql)
        conexion.mycursor.execute(sql1)
        conexion.mycursor.execute(sql2)
                
    else:
        pass
    
    # CREAMOS LA NUEVA TABLA
    
    sql = """CREATE TABLE DATOS(
                id INT AUTO_INCREMENT PRIMARY KEY,
                NOMBRES VARCHAR(150),
                APELLIDO_PATERNO VARCHAR(150),
                APELLIDO_MATERNO VARCHAR(150),
                DNI INT,
                CORREO VARCHAR(150),
                DIRECCION VARCHAR(50),
                CELULAR INT(50),
                FECHA_DE_NACIMIENTO DATE,
                ESTADO_CIVIL VARCHAR(50),
                GENERO VARCHAR(150))
                """
    conexion.mycursor.execute(sql)
        
    sql = """CREATE TABLE GASTOS(
                id INT AUTO_INCREMENT PRIMARY KEY,
                DESCRIPCION VARCHAR(150),
                MONTO VARCHAR(50))
                """
    conexion.mycursor.execute(sql)
        
    sql = """CREATE TABLE RESULTADOS(
                id INT AUTO_INCREMENT PRIMARY KEY,
                CLIENTE VARCHAR(30),
                CUOTA FLOAT,
                EXCEDENTE FLOAT,
                RATIO FLOAT,
                OBSERVACIÓN VARCHAR(150))
                """
    conexion.mycursor.execute(sql) 
    conexion.cerrar()


    

    
    

    
    
            
    
    
    
    
    