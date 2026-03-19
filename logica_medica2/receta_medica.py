import customtkinter as ctk
class VentanaReceta(ctk.CTkToplevel):
    def __init__(self, parent, datos_paciente, riesgo, consejos):
        super().__init__(parent)
        self.title("Receta Medica Digital")
        self.geometry("600x800")
        self.configure(fg_color ="#FFF9E3")
        
        #ventana 
        self.attributes("-topmost", True)
        ctk
        #encabezado
        self.header = ctk.CTkFrame(self, fg_color="#2c3e50", height=100, corner_radius=0) # Cambiado a Frame
        self.header.pack(fill="x", padx=0, pady=0)
        self.header.pack_propagate(False) # Para que mantenga su altura de 100

        ctk.CTkLabel(self.header, text="CLINICA CARDIOVASCULAR", font=("Times New Roman", 24, "bold"), text_color="white").pack(pady=30)
        
        #receta
        self.cuerpo = ctk.CTkFrame(self, fg_color="transparent")
        self.cuerpo.pack(fill="both", expand=True, padx=40, pady=20)
        
        #Datos del paciente 
        info_paciente = f"PACIENTE: {datos_paciente['nombre']}\nFECHA: {datos_paciente['fecha']}\nEDAD: {datos_paciente['edad']} años"
        ctk.CTkLabel(self.cuerpo, text=info_paciente, justify = "left", font=("Courier", 16, "bold"), text_color="black").pack(anchor="w", pady=10)
        
        
        ctk.CTkLabel(self.cuerpo, text="PRESCRIPCION Y RECOMENDACIONES:", font=("Courier", 18, "underline", "bold"), text_color="black").pack(anchor="w", pady=10)
        #caja de texto de recomendacion
        self.txt_consejos = ctk.CTkTextbox(self.cuerpo, fg_color="white", text_color="black",font=("Courier", 14), border_color="#cccccc", border_width=1)
        self.txt_consejos.pack(fill="both", expand=True, pady=10)
        self.txt_consejos.insert("0.0", consejos)
        self.txt_consejos.configure(state="disabled")
        
        # sello peligro
        self.footer = ctk.CTkFrame(self.cuerpo, fg_color="transparent")
        self.footer.pack(fill="x", pady=20)
        
        # sello circular
        self.sello = ctk.CTkFrame(self.footer, width=150, height=150, corner_radius=75, 
                                  border_width=3, border_color="#8B0000", fg_color="transparent")
        self.sello.pack(side="right", padx=20)
        self.sello.pack_propagate(False)
        
        ctk.CTkLabel(self.sello, text=f"RIESGO:\n{riesgo}%", font=("Courier", 20, "bold"), 
                     text_color="#8B0000").place(relx=0.5, rely=0.5, anchor="center")

        # Botenes 
        self.btn_cerrar = ctk.CTkButton(self, text="VOLVER A EVALUAR", fg_color="#2c3e50",command=self.destroy) 
        self.btn_cerrar.pack(pady=20)
        
