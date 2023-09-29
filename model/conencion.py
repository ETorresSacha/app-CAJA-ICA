import mysql.connector
import tkinter.messagebox

# CONECTAR A MYSQL Y CREAR UNA BASE DE DATOS NUEVO
class crear_bd():
    
    def __init__(self):
        self.conexion = mysql.connector.connect(
        host = "localhost",
               user ="root",
               port = "3307",
               password ="123456"
            )
        
        self.mycursor = self.conexion.cursor()
        self.mycursor.execute(" CREATE DATABASE EVALUACION2")
        self.conexion.commit()
        self.conexion.close()
        
class conectar():

    def __init__(self):
        self.conexion = mysql.connector.connect(
        host = "localhost",
                user ="root",
                port = "3307",
                password ="123456",
                database="EVALUACION2"
            )
        
        self.mycursor = self.conexion.cursor()
        #self.conexion.commit() --> si ocurre un error habilitar
        
            
    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()

