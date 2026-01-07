import customtkinter as ctk
from calcular_puntos_edad import calcular_puntos_edad
import webbrowser
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AppCardio(ctk.CTk):
    def abrir_guia(self):
        webbrowser.open("https://sigeps.sis.gob.pe/BuscadorEESS/PortalSIS/BuscarXDEP")
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Riesgo Cardiovascular")
        self.geometry("850x550")
        self.configure(fg_color="#1a1a1a") # Fondo muy oscuro

        # --- COLUMNA IZQUIERDA (Entrada de datos) ---
        self.sidebar = ctk.CTkFrame(self, width=300, corner_radius=15, fg_color="#252525")
        self.sidebar.pack(side="left", fill="y", padx=20, pady=20)

        ctk.CTkLabel(self.sidebar, text="DATOS MÉDICOS", font=("Roboto", 18, "bold"), text_color="#3b8ed0").pack(pady=15)
        
        # Botón de ayuda con estilo de "enlace"
        self.btn_ayuda = ctk.CTkButton(
        self.sidebar, 
        text="¿No conoces tus datos? Haz clic aquí", 
        fg_color="transparent",      # Sin fondo para que parezca texto
        text_color="#3b8ed0",         # Color azul de link
        font=("Roboto", 11, "underline"),
        hover_color="#252525",        # Color del fondo al pasar el mouse
        command=self.abrir_guia
        )
        self.btn_ayuda.pack(pady=1)
        
        # Campos con labels integrados
        self.entry_edad = self.crear_campo(self.sidebar, "Edad:")
        self.entry_genero = self.crear_campo(self.sidebar, "Género (masculino/femenino):")
        self.entry_presion = self.crear_campo(self.sidebar, "Presión Sistólica:")
        self.entry_colesterol = self.crear_campo(self.sidebar, "Colesterol Total:")
        self.entry_hdl = self.crear_campo(self.sidebar, "Colesterol HDL:")

        self.check_fumar = ctk.CTkCheckBox(self.sidebar, text="Suele fumar?", text_color="white")
        self.check_fumar.pack(pady=10)
        self.check_antecedentesF = ctk.CTkCheckBox(self.sidebar, text="Antecedentes familiares?", text_color="white")
        self.check_antecedentesF.pack(pady=10)

        self.check_diabetico = ctk.CTkCheckBox(self.sidebar, text="Diabetico?", text_color="white")
        self.check_diabetico.pack(pady=10)

        self.btn_calcular = ctk.CTkButton(self.sidebar, text="CALCULAR RIESGO", font=("Roboto", 14, "bold"),
                                          height=40, command=self.obtener_resultado)
        self.btn_calcular.pack(pady=2, padx=20, fill="x")

        # --- COLUMNA DERECHA (Resultados) ---
        self.main_view = ctk.CTkFrame(self, fg_color="transparent")
        self.main_view.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(self.main_view, text="RESULTADO DEL ANÁLISIS", font=("Roboto", 22, "bold")).pack(pady=10)

        # Círculo de porcentaje (Más grande y moderno)
        self.circulo_riesgo = ctk.CTkFrame(self.main_view, width=220, height=220, corner_radius=110, fg_color="#333333", border_width=5, border_color="#444444")
        self.circulo_riesgo.pack(pady=30)
        self.circulo_riesgo.pack_propagate(False)

        self.label_porcentaje = ctk.CTkLabel(self.circulo_riesgo, text="0%", font=("Roboto", 50, "bold"))
        self.label_porcentaje.place(relx=0.5, rely=0.5, anchor="center")

        self.label_status = ctk.CTkLabel(self.main_view, text="Esperando datos...", font=("Roboto", 16, "italic"), text_color="gray")
        self.label_status.pack(pady=10)
        
        # Título de la simulación
        self.label_tiempo = ctk.CTkLabel(self.main_view, text="Proyección temporal: Año 10", font=("Roboto", 14))
        self.label_tiempo.pack(pady=(20, 0))

# El Slider: va de 1 a 10
        self.label_status = ctk.CTkLabel(self.main_view, text="Esperando datos...", 
            font=("Roboto", 16, "bold"), wraplength=350)
        self.label_status.pack(pady=10)
        self.slider_tiempo = ctk.CTkSlider(self.main_view, from_=1, to=10, number_of_steps=9, 
            command=self.actualizar_proyeccion)
        self.slider_tiempo.set(10)
        self.slider_tiempo.pack(pady=10, padx=50, fill="x")
        self.label_aviso_fijo = ctk.CTkLabel(self.main_view, 
             text="Recuerde que siempre es mejor consular a un porfesional", 
             font=("Roboto", 12, "italic"), text_color="gray", wraplength=400)
        self.label_aviso_fijo.pack(side="bottom", pady=20)
        # MOSTRAR BIENVENIDA AL FINAL
        self.mostrar_bienvenida()

    def mostrar_bienvenida(self):
    # Fondo de la pantalla de bienvenida
        self.frame_bienvenida = ctk.CTkFrame(self, fg_color="#1a1a1a")
        self.frame_bienvenida.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Este Frame invisible asegura que todo se mantenga en el centro
        self.contenedor_central = ctk.CTkFrame(self.frame_bienvenida, fg_color="transparent")
        self.contenedor_central.pack(expand=True)

    # --- AGREGAR IMAGEN (Logo) ---
        try:
        # Reemplaza "logo_medico.png" con el nombre de tu archivo de imagen
            img = ctk.CTkImage(light_image=Image.open("logo_medico.png"),
                           dark_image=Image.open("logo_medico.png"),
                           size=(160, 160))
            self.label_logo = ctk.CTkLabel(self.contenedor_central, image=img, text="")
            self.label_logo.pack(pady=20)
        except Exception as e:
        

    # Texto de Bienvenida centrado
            ctk.CTkLabel(self.contenedor_central, text="BIENVENIDO", 
                 font=("Roboto", 90, "bold"), text_color="#3b8ed0").pack(pady=10)
    
            ctk.CTkLabel(self.contenedor_central, 
                 text="Software de Evaluación Framingham\nPrecisión y Cuidado Cardiovascular", 
                 font=("Roboto", 25)).pack(pady=10)

    # Botón de entrada
            self.btn_entrar = ctk.CTkButton(self.contenedor_central, text="INICIAR", 
                                    width=250, height=60, font=("Roboto", 16, "bold"),
                                    command=self.entrar_a_calculadora)
            self.btn_entrar.pack(pady=40)
        
    def entrar_a_calculadora(self):
        self.frame_bienvenida.destroy()
        
    def crear_campo(self, parent, texto):
        ctk.CTkLabel(parent, text=texto, text_color="gray").pack(anchor="w", padx=25)
        entry = ctk.CTkEntry(parent, width=220, height=35, corner_radius=8, border_color="#3b8ed0")
        entry.pack(pady=(0, 10), padx=25)
        return entry
       
    def actualizar_proyeccion(self, valor):
    # 'valor' es el año seleccionado en el slider (1 al 10)
        año_actual = int(valor)
        self.label_tiempo.configure(text=f"Proyección temporal: Año {año_actual}")
        try:
        # 1. Obtenemos los datos actuales de los cuadros
           e, g, p, c, h = int(self.entry_edad.get()), self.entry_genero.get().lower(), int(self.entry_presion.get()), int(self.entry_colesterol.get()), int(self.entry_hdl.get())
           f = "si" if self.check_fumar.get() else "no"
           d = "si" if self.check_diabetico.get() else "no"
           f = "si" if self.check_fumar.get() else "no"
           l = "si" if self.check_antecedentesF.get() else "no"
           
          
        
        # 2. Calculamos el riesgo base (a 10 años)
           _, riesgo_10_años = calcular_puntos_edad(g, e, d, f, p, c, h, l)
        
        # 3. Lógica de simulación: Riesgo proporcional al año
        # Formula: (Riesgo total / 10) * año seleccionado
           riesgo_proyectado = round((riesgo_10_años / 10) * año_actual, 1)
        
        # 4. Actualizamos el círculo con el valor del año seleccionado
           self.label_porcentaje.configure(text=f"{riesgo_proyectado}%")
        
        except:
           self.label_status.configure(text="Calcula primero el riesgo para ver la línea de tiempo")

    def obtener_resultado(self):
        try:
            # Arreglado: ahora lee entry_genero para evitar el AttributeError
            e = int(self.entry_edad.get())
            g = self.entry_genero.get().lower().strip()
            p = int(self.entry_presion.get())
            c = int(self.entry_colesterol.get())
            h = int(self.entry_hdl.get())
            f = "si" if self.check_fumar.get() else "no"
            d = "si" if self.check_diabetico.get() else "no"
            l = "si" if self.check_antecedentesF.get() else "no"
            
            
            pts, riesgo = calcular_puntos_edad(g, e, d, f, p, c, h, l)

            self.label_porcentaje.configure(text=f"{riesgo}%")
            
            if riesgo > 30:
                color = "#8B0000" # Rojo oscuro
                status = "¡ALERTA!: Riesgo Crítico. Requiere atención inmediata."
            elif riesgo > 20:
                color = "#e74c3c" # Rojo normal
                status = "Riesgo Alto: Consulte a su cardiólogo"
            elif riesgo >= 10:
                color = "#f1c40f" # Amarillo
                status = "Riesgo Moderado: Se recomienda revisión médica"
            else:
                color = "#2ecc71" # Verde
                status = "Riesgo Bajo: Mantenga hábitos saludables"
                
            self.label_porcentaje.configure(text=f"{riesgo}%", text_color="white" if riesgo > 20 else "black")
            self.circulo_riesgo.configure(fg_color=color, border_color=color)
            self.label_status.configure(text=status, text_color=color)

        except Exception as err:
            self.label_status.configure(text="Error: Ingrese valores válidos", text_color="red")    
            
if __name__ == "__main__":
    app = AppCardio()  # Crea la aplicación
    app.mainloop()     # Mantiene la ventana abierta
       