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
from kivy.uix.popup import Popup

# In this script we import a builder that will pull the kv file no matter the name



class MainWindow(Screen):
	def btn(self):
		show_popup()

class SecondWindow(Screen):
	pass 

class WindowManager(ScreenManager):
	pass 

class P(FloatLayout):
	pass

def show_popup():
	show = P()
	#Defualt is the middle
	popupWindow = Popup(title="Popup Window", content=show, size_hint=(None,None),size=(400,400)) 
	popupWindow.open()

kv = Builder.load_file("PopUp.kv")

class MyMainApp(App):
	def build(self):
		return kv


if __name__ == "__main__":
	MyMainApp().run()



