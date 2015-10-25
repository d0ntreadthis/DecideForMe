import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.core.window import Window

class ActivityInput(TextInput):
	# Should have a method that will change the color of the background
	# for 10 secs, then go back to default
	pass


class DeleteBtn(Button):
	# Should have an image of a bin on it, rather than the word del
	
	def callback(self):
		self.parent.deleteactivity()


class ActivityLayout(BoxLayout):

	childlist = [] # To keep a reference of all instances

	def __init__(self, **kwargs):
		super(ActivityLayout, self).__init__(**kwargs)
		ActivityLayout.childlist.append(self)
	
	def deleteactivity(self):
		self.parent.remove_widget(self)
		ActivityLayout.childlist.remove(self)


class ActivitiesLayout(GridLayout):
	# A layout for all of the activity layouts to go
	# Will be vertical
	pass


class MyScrollView(ScrollView):
	pass


class AddBtn(Button):
	# When pressed, will add an activity layout to the bottom of the
	# activities layout
	pass


class DecideBtn(Button):
	# When pressed, this should highlight a random activity in the list
	# for roughly 5 seconds?
	pass


class MenuLayout(BoxLayout):
	# A layout for the menu buttons
	# Will be horizontal
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