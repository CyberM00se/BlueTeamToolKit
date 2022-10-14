import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


class MainWindow(Screen):
	pass 

class SecondWindow(Screen):
	pass 

class WindowManager(ScreenManager):
	pass 

kv = Builder.load_file("NetDiagram.kv")

class MyMainApp(App):
	def build(self):
		return kv


if __name__ == "__main__":
	MyMainApp().run()

