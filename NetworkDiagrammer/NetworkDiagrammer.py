import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

kivy.require("1.24.2")

class DashboardPage(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		self.cols = 2

		self.add_widget(Label(text="BTTK"))
		self.ip = TextInput(multiline=False)
		self.add_widget(self.ip)

		self.add_widget(Label(text="Page 1"))

		self.Page1info = TextInput(multiline=False)
		self.add_widget(self.Page1info)

		#Adding a component	
		self.join = Button(text="Join")
		self.add_widget(self.join)
		#Getting Buttons to run -- create a method join_button
		self.join.bind(on_press=self.join_button)

	def join_button(self, instance):
		ip = self.ip.text

		print(f"Attemptying to join {ip} as ASAAA")
		info = f"Attemptying to join {ip} as ASAAA"
		NetDiag_app.info_page.udpate_info(info)
		NetDiag_app.screen_manager.current = "Info"

class InfoPage(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.cols = 1
		self.message = Label(halign="center", valign="middle", font_size= 30)
		self.message.bind(width=self.update_text_width)
		self.add_widget(self.message)

	def udpate_info(self, message):
		self.message.text = message

	def update_text_width(self, *_):
		self.message.text_size = (self.message.width*0.9, None)


class myApp(App):
	#initalization Method (run through App)
	def build(self):
		self.screen_manager = ScreenManager()


		self.dashboard_page = DashboardPage()
		screen = Screen(name="Connect")
		screen.add_widget(self.dashboard_page)
		self.screen_manager.add_widget(screen)

		self.info_page = InfoPage()
		screen = Screen(name="Info")
		screen.add_widget(self.info_page)
		self.screen_manager.add_widget(screen)

		return self.screen_manager


if __name__ == "__main__":
	NetDiag_app = myApp()
	NetDiag_app.run()

#Next Step: Start formatting page
#https://www.youtube.com/watch?v=62LSK62Gudc&list=PLQVvvaa0QuDfwnDTZWw8H3hN_VRQfq8rF&index=5&ab_channel=sentdex

