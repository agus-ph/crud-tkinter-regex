import tkinter as tk
from modulo_app import MiApp


class Controler:
    """
    Esta es una clase controlador
    utilizada para lanzar la aplicación
    """

    def __init__(
            self,
            root,
    ):
        self.mi_ventana = root
        self.mi_app()

    def mi_app(
            self,
    ):
        """
        Este es el método utilizado para lanzar la ventana principal
        que se encuentra en el módulo 'modulo_app.py'
        """
        MiApp(self.mi_ventana)


if __name__ == "__main__":
    root = tk.Tk()
    app_crud = Controler(root)

    root.mainloop()