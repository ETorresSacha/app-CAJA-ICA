# NUEVO CAPITAL
from tkinter import *
from tkcalendar import *
from tkinter import ttk # esto es para crear un desplegable de opciones


"""raiz = Tk()
raiz.title("NUEVO CAPITAL")
raiz. resizable(1,1)
raiz.iconbitmap("logo.ico")
#raiz.geometry("650x350")
raiz.config(bg="white")

# primer frame
frame=Frame(raiz)
frame.pack(fill="x") # esta opcion es para expndir(capitulo43)
frame.config(bg="lightgray")
#frame.config(cursor="hand2") # es para cambiar el cursor
# SE CREA EL FRAME PARA EL TÍTULO DE LA FINANCIERAMAS EL LOGO
Label(frame, text=" NUEVO CAPITAL",fg="darkblue",font=("comic Sans MS", 18), pady= 10).grid(column=0, row=0, sticky="w")

#imagen = PhotoImage(file="logoo.png")
#Label(frame1, image=imagen).grid(column=2, row=3, sticky="e")

frame1 = Frame(raiz)
frame1.pack(fill="x") # esta opcion es para expndir(capitulo43)
frame1.config(bg="lightgray")
NOperacion = Label(frame1, text='N° Operación: ',fg="black", font=("Arial black",10))
NOperacion.grid(column=0, row=0,pady=5,padx=10)
entryoperacion = Entry(frame1)
entryoperacion.grid(column=1, row=0,pady=5,padx=10)

fecha = Label(frame1, text = "Fecha: ", fg="black", font=("Arial black",10))
fecha.grid(column=2, row=0,pady=5,padx=10)
entryfecha= Entry(frame1)
entryfecha.grid(column=3, row= 0,pady=5,padx=10)"""


# SE CREA UNA CLASE PARA GENERAR DIFERENTES FRAMES, CON LA FINALIDAD DE NO HACER MUCHOS CODIGOS

class DATOS():
    def datos(self,a):

        # Con el siguiente código se crea el frame

        self.a = Frame(raiz)
        self.a.pack(fill="x")
        self.a.config(bg="lightgray")
        if a==7:
            self.datos_cliente = Label(self.a, text="Datos del cliente", fg="black", font=("Arial Black", 10))
        elif a==3:
            self.datos_cliente = Label(self.a, text="Datos del aval", fg="black", font=("Arial Black", 10))
        self.datos_cliente.grid(column=0, row=1, sticky="w", pady=15)


        # Con los siguientes códigos se crea los datos de cada frame

        self.lbl_nombre=Label(self.a, text="Nombre completo",fg="black",font=("Arial", 8))
        self.lbl_nombre.grid(column=0, row=2)
        self.entry_nombre = Entry(self.a)
        self.entry_nombre.grid(column=0, row=3, pady=5)

        self.lbl_primer_apellido=Label(self.a, text="Primer apellido", fg="black", font=("Arial",8))
        self.lbl_primer_apellido.grid(column=1, row=2)
        self.entry_primer_apellido=Entry(self.a)
        self.entry_primer_apellido.grid(column=1,row=3, padx=5)

        self.lbl_segundo_apellido=Label(self.a, text="Segundo apellido", fg="black", font=("Arial",8))
        self.lbl_segundo_apellido.grid(column=2, row=2)
        self.entry_segundo_apellido=Entry(self.a)
        self.entry_segundo_apellido.grid(column=2,row=3,padx=5)

        self.lbl_dni = Label(self.a, text="DNI", fg="black", font=("Arial", 8))
        self.lbl_dni.grid(column=0, row=4,pady=5)
        self.entry_dni = Entry(self.a)
        self.entry_dni.grid(column=0, row=5, padx=5,pady=5)

        self.lbl_correo = Label(self.a, text="Correo electrónico", fg="black", font=("Arial", 8))
        self.lbl_correo.grid(column=1, row=4,pady=5,columnspan=2)
        self.entry_correo = Entry(self.a,width= 42)
        self.entry_correo.grid(column=1, row=5, columnspan=2, padx=5,pady=5)

        self.lbl_direccion=Label(self.a, text="Dirección", fg="black", font=("Arial",8))
        self.lbl_direccion.grid(column=0, row=6,columnspan=2)
        self.entry_direccion=Entry(self.a,width= 42) #width-- ancho de la celda, height--> largo de la celda
        self.entry_direccion.grid(column=0,row=7,padx=5, columnspan=2)# columnspan--> expande la columna

        self.lbl_celular = Label(self.a, text="Celular",fg="black", font=("Arial",8))
        self.lbl_celular.grid(column=2,row=6)
        self.entry_celular = Entry(self.a)
        self.entry_celular.grid(column=2, row=7,padx=5)

        # calendario
        self.lbl_nacimiento = Label(self.a, text="Fecha de nacimiento",fg="black", font=("Arial",8))
        self.lbl_nacimiento.grid(column=0, row=8,pady=5)
        self.entry_calendario = DateEntry(self.a,width=16) # Se importa el calendario
        self.entry_calendario.grid(column=0, row=9)

        # CREAR UN DESPLEGABLE DE OPCIONES
        # Estado civil
        self.lbl_estado_civil = Label(self.a, text="Estado civil",fg="black", font=("Arial",8))
        self.lbl_estado_civil.grid(column=1, row=8,padx=5)
        self.opciones = ["Soltero(a)","Casado(a)"]
        self.cmbOpciones= ttk.Combobox(self.a,values=self.opciones,width=16)
        self.cmbOpciones.grid(column= 1, row=9 )

        # Género
        self.lbl_genero = Label(self.a, text="Género",fg="black", font=("Arial",8))
        self.lbl_genero.grid(column=2,row=8, padx=5)
        self.opciones1=["Masculino","Femenino","No me decido"]
        self.cmbOpciones1 = ttk.Combobox(self.a,values=self.opciones1,width=16)
        self.cmbOpciones1.grid(column=2, row=9,padx=5)






#raiz.mainloop()