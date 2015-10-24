import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.core.window import Window

class ActivityInput(TextInput):
	pass

class DeleteButton(Button):
	# When pressed, this should delete and remove the activity layout it's in
	# Have image of a bin on it
	pass


class ActivityLayout(BoxLayout):
	# Contains a text input for the activity name, and a delete button
	# Will be horizontal
	pass


class ActivitiesLayout(BoxLayout):
	# Just a layout for all of the activity layouts to go
	# Will be vertical
	pass


class DecideBtn(Button):
	# When pressed, this should highlight a random activity in the list
	# for roughly 5 seconds?
	pass


class MainWidget(BoxLayout):
	'''Returned when the app is run'''
	pass


class MainApp(App):

	def build(self):
		#Window.size = (x, y)
		return MainWidget()

if __name__ == '__main__':
	MainApp().run()