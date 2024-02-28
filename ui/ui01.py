# Librerías
#import tkinter
import customtkinter

class App(customtkinter.CTk):

    nums = [
        [ 1,  2,  3,  4,  5,  6],
        [ 7,  8,  9, 10, 11, 12],
        [13, 14, 15, 16, 17, 18]
    ]

    # Función para inicializar
    def __init__(self):
        super().__init__() #qué signigica?

        # configure window
        self.title("Tirolesa")
        #self.geometry(f"{1100}x{580}") #tamaño de la ventana

        # configure grid layout
        # son 4 filas
        # la fila 0 tiene tamaño predefinido
        # estas ocupan el mínimo espacio
        self.grid_rowconfigure((0, 1, 2, 4), weight=0)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # agregar frame a la primera fila
        self.frame_top = customtkinter.CTkFrame(self, height=100) #corner_radius
        self.frame_top.grid(row=0, column=0, sticky="nsew")

        # agregar progress bar y slider
        self.bar = customtkinter.CTkProgressBar(self, height=16)
        self.bar.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="ew")
        self.slider = customtkinter.CTkSlider(self, height=24)
        self.slider.grid(row=2, column=0, padx=20, pady=(10, 20), sticky="ew")

        # frame para botones
        self.frame_buttons = customtkinter.CTkFrame(self, fg_color="transparent")
        self.frame_buttons.grid(row=3, column=0, sticky="nsew")
        self.frame_buttons.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.frame_buttons.grid_rowconfigure((0, 1, 2), weight=1)
        # Crear y colocar los botones en la rejilla
        for j in range(3):  # Filas
            for i in range(6):  # Columnas
                val = self.nums[j][i] #Obtener valor para este botón
                self.boton = customtkinter.CTkButton(self.frame_buttons, text=f"Botón {val}", command=lambda v=val: self.boton_clicado(v))
                self.boton.grid(row=j, column=i, padx=5, pady=5, sticky="nsew")  # Colocar el botón en la fila i y columna j

        # frame inferior
        #self.frame_bottom = customtkinter.CTkFrame(self) #corner_radius
        #self.frame_bottom.grid(row=4, column=0, sticky="ew")
        self.label1 = customtkinter.CTkLabel(self, text="hola")
        self.label1.grid(row=4, column=0, sticky="ew")

    # Acción cuando se presionan los botones de la rejilla
    def boton_clicado(event, val):
        #print("¡Botón clicado!")
        #print(event)
        print(val)

if __name__ == "__main__":
    app = App()
    app.mainloop()