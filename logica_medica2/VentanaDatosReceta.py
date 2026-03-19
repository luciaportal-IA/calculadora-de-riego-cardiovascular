import customtkinter as ctk
import datetime
class VentanaDatosReceta(ctk.CTkToplevel):
    def __init__(self, parent, callback):
        super().__init__(parent)
        self.title("Datos para la Receta")
        self.geometry("400x500")
        self.callback = callback  
        
        # Centrar ventana y poner al frente
        self.attributes("-topmost", True)
        
        ctk.CTkLabel(self, text="RELLENAR DATOS", 
                     font=("Roboto", 16, "bold")).pack(pady=20)

        
        self.entry_nombre = self.crear_input("Nombre Completo del Paciente:")
        self.entry_fecha = self.crear_input("Fecha (DD/MM/AAAA):", 
            datetime.date.today().strftime("%d/%m/%Y"))
        self.entry_edad = self.crear_input("Confirmar Edad:", parent.entry_edad.get())
        self.entry_actividad = self.crear_input("Actividad Física (si/no):")

        # Botón para generar
        ctk.CTkButton(self, text="GENERAR RECETA", fg_color="#2ecc71",
                      command=self.enviar_datos).pack(pady=30)

    def crear_input(self, texto, valor_defecto=""):
        ctk.CTkLabel(self, text=texto).pack(pady=(10, 0))
        entry = ctk.CTkEntry(self, width=300)
        entry.insert(0, valor_defecto)
        entry.pack(pady=5)
        return entry

    def enviar_datos(self):
        # Recolección en diccionario
        datos = {
            "nombre": self.entry_nombre.get().upper(),
            "fecha": self.entry_fecha.get(),
            "edad": self.entry_edad.get(),
            "actividad": self.entry_actividad.get()
        }
        # Cerramos esta ventana
        self.destroy() 
        self.callback(datos) 
