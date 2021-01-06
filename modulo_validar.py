import re
from tkinter import messagebox


class ValidarCampos:
    """
    Esta clase utiliza expresiones
    regulares para validar datos
    """

    def __init__(
            self,
    ):
        
        self.val_id = (r"[0-9]{1,6}$")
        self.val_nombre = (r"[\D]{1,20}'?-?\s?[\D]{1,20}?'?-?[\D]{1,20}?$")
        self.val_email = (r"[\S]{1,20}@[\w-]{2,20}\.\w{2,3}(\.\w{2,3})?$")

    def validar_id(
            self,
            Id,
    ):
        """
        Este método valida el campo 'Id' de la app
        y evita que el dato quede en blanco
        """
        if len(Id) == 0:
            messagebox.showwarning(
                "Error",
                "Debe completar el campo 'Id'",
            )
            raise TypeError
        else:
            if re.match(self.val_id, Id):
                return Id
            else:
                messagebox.showwarning(
                    "Error", 
                    "Ingrese un Id valido"
                )
                raise TypeError

    def validar_nombre(
            self,
            nombre,
    ):
        """
        Este método valida el campo 'Nombre' de la app
        y evita que el dato quede en blanco
        """
        if len(nombre) == 0:
            messagebox.showwarning(
                "Error",
                "Debe completar el campo 'nombre'",
            )
            raise TypeError
        else:
            if re.match(self.val_nombre, nombre):
                return nombre
            else:
                messagebox.showwarning(
                    "Error", 
                    "Ingrese un nombre valido"
                )
                raise TypeError

    def validar_email(
            self,
            email,
    ):
        """
        Este método valida el campo 'Email' de la app
        y evita que el dato quede en blanco
        """
        if len(email) == 0:
            messagebox.showwarning(
                "Error",
                "Debe completar el campos 'email'",
            )
            raise TypeError
        else:
            if re.match(self.val_email, email):
                return email
            else:
                messagebox.showwarning(
                    "Error", 
                    "Ingrese un email valido"
                )
                raise TypeError
