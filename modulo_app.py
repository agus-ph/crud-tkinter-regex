import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from modulo_validar import ValidarCampos


class MiApp:
    """
    Esta clase contiene la estructura de la ventana principal,
    sus widget y las funciones que realizan el ABMC
    """

    def __init__(
            self,
            ventana,
    ):

        self.root = ventana
        self.root.title("ABMC App - UTN Python3")
        self.root.geometry("550x300")
        self.mi_id = tk.StringVar()
        self.mi_nombre = tk.StringVar()
        self.mi_email = tk.StringVar()

        self.objeto_validar = ValidarCampos()

        self.mi_frame = ttk.Frame(self.root)
        self.mi_frame.pack(fill="both", expand=1)

        # Comienza el bloque de Botones.

        self.boton_tabla = tk.Button(
            self.mi_frame, text="Conectar", command=lambda: self.crear_tabla()
        )
        self.boton_tabla.grid(row=0, column=3, padx=10, pady=10)

        self.boton_crear = tk.Button(
            self.mi_frame,
            text="Crear Registro",
            command=lambda: self.alta(
                self.mi_nombre.get(), 
                self.mi_email.get(),
            ),
        )
        self.boton_crear.grid(row=6, column=1, padx=10, pady=10)

        self.boton_consultar = tk.Button(
            self.mi_frame,
            text="Consultar Registro",
            command=lambda: self.consultas(self.mi_id.get()),
        )
        self.boton_consultar.grid(row=6, column=2, padx=10, pady=10)

        self.boton_modificar = tk.Button(
            self.mi_frame,
            text="Modificar Registro",
            command=lambda: self.modificaciones(
                self.mi_id.get(),
                self.mi_nombre.get(),
                self.mi_email.get(),
            ),
        )

        self.boton_modificar.grid(row=6, column=3, padx=10, pady=10)

        self.boton_borrar = tk.Button(
            self.mi_frame,
            text="Borrar Registro",
            command=lambda: self.baja(self.mi_id.get()),
        )
        self.boton_borrar.grid(row=6, column=4, padx=10, pady=10)

        # Comienza el bloque de Campos / Entrys.

        self.campo_id = tk.Entry(self.mi_frame, textvariable=self.mi_id)
        self.campo_id.grid(row=2, column=3, padx=10, pady=10)

        self.campo_nombre = tk.Entry(
            self.mi_frame, 
            textvariable=self.mi_nombre
        )
        self.campo_nombre.grid(row=3, column=3, padx=10, pady=10)

        self.campo_email = tk.Entry(self.mi_frame, textvariable=self.mi_email)
        self.campo_email.grid(row=4, column=3, padx=10, pady=10)

        # # Comienza el bloque de Labels de los Campos y de boton 'Conectar'

        label_id = tk.Label(self.mi_frame, text="ID:")
        label_id.grid(row=2, column=2, sticky="w", padx=10, pady=10)

        label_nombre = tk.Label(self.mi_frame, text="Nombre:")
        label_nombre.grid(row=3, column=2, sticky="w", padx=10, pady=10)

        label_email = tk.Label(self.mi_frame, text="Email:")
        label_email.grid(row=4, column=2, sticky="w", padx=10, pady=10)

        label_conectar = tk.Label(
            self.mi_frame, 
            text="Oprima para empezar a operar:"
        )
        label_conectar.grid(row=0, column=2, sticky="w", padx=10, pady=10)

    # Acontinucion se encuentran los Metodos de la clase

    def conexion(
            self,
    ):
        """
        Este método crea la bbdd y retorna el objeto de conexión.
        """
        try:
            con = sqlite3.connect("basetpfinal.db")
            return con
        except:
            messagebox.showwarning(
                "¡Atención!", "No se a podido conectar a la base de datos"
            )

    def crear_tabla(
            self,
    ):
        """
        Este método crea la tabla 'usuariosapptp' cuando pulsamos
        el boton 'Conectar' por primera vez. Una vez creada, cada
        ves que pulsemos el botón lanzará un mensaje diciendo
        'Conectado con éxito a la base de datos'
        """
        try:
            con_tabla = self.conexion()
            mi_cursor = con_tabla.cursor()

            mi_cursor.execute(
                """CREATE TABLE usuariosapptp(
                    Id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    Nombre VARCHAR(50), 
                    Email VARCHAR(70))
                    """
            )

            con_tabla.commit()
            messagebox.showinfo(
                "Conexión", "Conectado con éxito a la base de datos"
            )

        except:
            messagebox.showinfo(
                "Conexión", "Conectado con éxito a la base de datos"
            )

    def alta(
            self,
            nombre,
            email,
    ):
        """
        Este método realiza el alta de registro. Hay que completar los
        campos 'Nombre' e 'Email' (el campo 'Id' se autocompleta)
        y presionar el botón 'Crear Registro'. Utiliza métodos del módulo
        'modulo_validar.py' para validar los datos
        """
        try:
            con_alta = self.conexion()
            mi_cursor = con_alta.cursor()

            self.objeto_validar.validar_nombre(nombre)
            if self.objeto_validar.validar_nombre(nombre):
                pass

            self.objeto_validar.validar_email(email)
            if self.objeto_validar.validar_email(email):
                pass

            datos_alta = (nombre, email)

            mi_cursor.execute(
                "INSERT INTO usuariosapptp VALUES(NULL,?,?)", (datos_alta)
            )

            con_alta.commit()
            messagebox.showinfo("BaseDatos", "Registro creado con éxito")
        except:
            pass

    def baja(
            self,
            Id,
    ):
        """
        Este método realiza la baja de registro. Hay que completar solo
        el campo 'Id' y presionar el botón 'Borrar Registro'. Utiliza 
        métodos del módulo 'modulo_validar.py' para validar los datos
        """
        try:
            con_baja = self.conexion()
            mi_cursor = con_baja.cursor()

            self.objeto_validar.validar_id(Id)
            if self.objeto_validar.validar_id(Id):
                pass

            dato_baja = Id

            mi_cursor.execute(
                "DELETE FROM usuariosapptp WHERE Id =" + dato_baja
            )

            con_baja.commit()
            messagebox.showinfo(
                "BaseDatos", 
                "Registro eliminado con éxito"
            )
        except:
            pass

    def modificaciones(
            self,
            Id,
            nombre,
            email,
    ):
        """
        Este método realiza la modificación registro. Todos
        los campos deben estar completos y luego presionar
        el botón 'Modificar Registro'. Utiliza métodos del
        módulo 'modulo_validar.py' para validar los datos
        """
        try:
            con_modif = self.conexion()
            mi_cursor = con_modif.cursor()

            self.objeto_validar.validar_id(Id)
            if self.objeto_validar.validar_id(Id):
                pass

            self.objeto_validar.validar_nombre(nombre)
            if self.objeto_validar.validar_nombre(nombre):
                pass

            self.objeto_validar.validar_email(email)
            if self.objeto_validar.validar_email(email):
                pass

            dato_id = Id

            datos_modif = (nombre, email)

            mi_cursor.execute(
                ("UPDATE usuariosapptp SET Nombre=?, Email=? WHERE Id =" 
                + dato_id),
                (datos_modif),
            )

            con_modif.commit()
            messagebox.showinfo(
                "BaseDatos", 
                "Registro modificado con éxito"
            )
        except:
            pass

    def consultas(
            self,
            Id,
    ):
        """
        Este método realiza la consulta de registro. Solo
        se requiere completar el campo 'Id' y luego presionar
        el botón 'Consultar Registro' para que traiga el resto
        de los datos. Utiliza métodos del módulo
        'modulo_validar.py' para validar los datos
        """
        try:
            con_consul = self.conexion()
            mi_cursor = con_consul.cursor()

            self.objeto_validar.validar_id(Id)
            if self.objeto_validar.validar_id(Id):
                pass

            dato_consulta = Id

            mi_cursor.execute(
                "SELECT * FROM usuariosapptp WHERE Id=" + dato_consulta
            )

            datos_usuario = mi_cursor.fetchall()

            for dato in datos_usuario:

                self.mi_id.set(dato[0])
                self.mi_nombre.set(dato[1])
                self.mi_email.set(dato[2])

            con_consul.commit()
        except:
            pass
