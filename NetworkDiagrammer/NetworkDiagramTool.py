import kivy
import scannerScript
import os
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.image import Image
from kivy.core.window import Window


Window.size = (1920,1080)


class MainWindow(Screen):
	
	ipToScan = ObjectProperty(None)

	def executeScan(self):
		ipToScan = self.ids.inputIpField.text
		print("Executing scan of:  " + ipToScan)
		os.system('python scannerScript.py ' + ipToScan)
		print("-------DONE-----")
	 

class SecondWindow(Screen):
	pass 

class WindowManager(ScreenManager):
	pass 


kv = Builder.load_file("DiagramWindow.kv")

class MyMainApp(App):
	def build(self):
		return kv

if __name__ == "__main__":
	MyMainApp().run()
	
