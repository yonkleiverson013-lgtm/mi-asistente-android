import datetime
import json
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class AsistenteLayout(BoxLayout):

  def __init__(self, **kwargs):
    super().__init__(orientation="vertical", padding=15, spacing=10, **kwargs)

    # Titulo de la App
    self.label_status = Label(
        text="Asistente Tactico Listo",
        font_size="22sp",
        size_hint_y=0.15,
        color=(0, 1, 0.8, 1),
    )
    self.add_widget(self.label_status)

    # Buscador integrado
    self.input_text = TextInput(
        hint_text="Escribe aqui para buscar...",
        size_hint_y=0.12,
        multiline=False,
    )
    self.add_widget(self.input_text)

    # Botones tacticos
    btn_google = Button(
        text="Buscar en Google",
        size_hint_y=0.12,
        background_color=(0.2, 0.6, 1, 1),
    )
    btn_google.bind(on_press=self.buscar_google)
    self.add_widget(btn_google)

    btn_whatsapp = Button(
        text="Abrir WhatsApp",
        size_hint_y=0.12,
        background_color=(0.1, 0.8, 0.3, 1),
    )
    btn_whatsapp.bind(on_press=self.abrir_whatsapp)
    self.add_widget(btn_whatsapp)

    btn_freefire = Button(
        text="Abrir Free Fire",
        size_hint_y=0.12,
        background_color=(1, 0.3, 0, 1),
    )
    btn_freefire.bind(on_press=self.abrir_freefire)
    self.add_widget(btn_freefire)

    btn_namida = Button(
        text="Abrir Namida Music",
        size_hint_y=0.12,
        background_color=(0.6, 0.2, 0.8, 1),
    )
    btn_namida.bind(on_press=self.abrir_namida)
    self.add_widget(btn_namida)

    btn_bateria = Button(
        text="Estado de Bateria",
        size_hint_y=0.12,
        background_color=(0.8, 0.8, 0.1, 1),
    )
    btn_bateria.bind(on_press=self.consultar_bateria)
    self.add_widget(btn_bateria)

  def hablar(self, texto):
    texto_limpio = texto.replace('"', "")
    os.system(f'termux-tts-speak -l es "{texto_limpio}"')

  def buscar_google(self, instance):
    busqueda = self.input_text.text.strip()
    if busqueda:
      self.label_status.text = f"Buscando: {busqueda}"
      self.hablar(f"Buscando {busqueda} en Google")
      url = f"https://www.google.com/search?q={busqueda.replace(' ', '+')}"
      os.system(f"termux-open {url}")

  def abrir_whatsapp(self, instance):
    self.label_status.text = "Abriendo WhatsApp..."
    self.hablar("Abriendo WhatsApp")
    os.system("am start -n com.whatsapp/.HomeActivity")

  def abrir_freefire(self, instance):
    self.label_status.text = "Desplegando Free Fire..."
    self.hablar("Entrando al campo de batalla")
    os.system(
        "am start -n com.dts.freefireth/com.dts.freefireth.FFMainActivity"
    )

  def abrir_namida(self, instance):
    self.label_status.text = "Abriendo Namida..."
    self.hablar("Sincronizando frecuencias de audio")
    os.system("am start -a android.intent.action.MUSIC_PLAYER")

  def consultar_bateria(self, instance):
    resultado = os.popen("termux-battery-status").read()
    try:
      datos = json.loads(resultado)
      nivel = datos.get("percentage", 0)
      self.label_status.text = f"Bateria: {nivel}%"
      self.hablar(f"Tienes {nivel} por ciento de bateria")
    except Exception:
      self.label_status.text = "Bateria: Consultando..."


class MiAsistenteApp(App):

  def build(self):
    return AsistenteLayout()


if __name__ == "__main__":
  MiAsistenteApp().run()
    
