
import json                                   
import os
from kivy.lang import Builder                 
from kivymd.app import MDApp                 
from plyer import notification                

KV = """
MDBoxLayout:
    orientation: "vertical"
    padding: "20dp"
    spacing: "20dp"
    md_bg_color: app.theme_cls.backgroundColor
    MDTextField:
        id: campo
    MDButton:
        on_release: app.guardar(campo.text)
        MDButtonText:
            text: "Guardar"
"""

class App(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def guardar(self, texto):
        if not texto:
            return
        ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "datos.json")
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump({"texto": texto}, f, ensure_ascii=False)
        notification.notify(
            title="Guardado",
            message=f'El texto "{texto}" ha sido guardado exitosamente')

App().run()
