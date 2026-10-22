import json                                   # librería para escribir/leer archivos JSON
from kivy.lang import Builder                 # permite cargar el diseño escrito en lenguaje KV
from kivymd.app import MDApp                  # clase base de toda aplicación KivyMD
from plyer import notification                # librería que lanza la notificación del sistema

KV = """
MDBoxLayout:                                  # contenedor que apila los widgets
    orientation: "vertical"                   # los apila de arriba hacia abajo
    padding: "20dp"                           # margen interior
    spacing: "20dp"                           # espacio entre widgets
    md_bg_color: app.theme_cls.backgroundColor  # color de fondo (si no, queda negro)
    MDTextField:                              # campo para escribir el texto
        id: campo                             # nombre para referenciarlo desde el botón
    MDButton:                                 # botón
        on_release: app.guardar(campo.text)   # al soltarlo, llama a guardar() pasándole el texto del campo
        MDButtonText:                         # texto dentro del botón (obligatorio en KivyMD 2.0)
            text: "Guardar"                   # lo que dice el botón
"""

class App(MDApp):                             # nuestra app hereda de MDApp
    def build(self):                          # método que construye la interfaz
        return Builder.load_string(KV)        # convierte el KV en widgets y los devuelve como pantalla

    def guardar(self, texto):                 # función del botón; recibe el texto escrito
        if not texto:                         # si el campo está vacío...
            return                            # ...no hace nada
        ruta = self.user_data_dir + "/datos.json"   # carpeta privada y escribible de la app + nombre del archivo
        with open(ruta, "w") as f:            # abre el archivo en modo escritura (si existe, lo sobrescribe)
            json.dump({"texto": texto}, f)    # escribe un JSON válido: {"texto": "hola"}
        notification.notify(                  # lanza la notificación del sistema
            title="Guardado",                 # título de la notificación
            message=f'El texto "{texto}" ha sido guardado exitosamente')  # mensaje con el texto dentro

App().run()                                   # crea la app y la ejecuta