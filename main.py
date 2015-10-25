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
		ActivitiesLayout.al.delactivity(toremove=self.parent)


class ActivityLayout(BoxLayout):

	def __init__(self, **kwargs):
		super(ActivityLayout, self).__init__(**kwargs)
		ActivitiesLayout.childlist.append(self)
	

class ActivitiesLayout(GridLayout):

	childlist = [] # To keep a reference of all children

	def addactivity(self):
		self.add_widget(ActivityLayout())

	def delactivity(self, toremove):
		self.remove_widget(toremove)
		ActivitiesLayout.childlist.remove(toremove)


class MyScrollView(ScrollView):
	pass


class AddBtn(Button):

	def callback(self):
		ActivitiesLayout.al.addactivity()


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
		# Creates a reference to the activitieslayout within ActivitiesLayout
		# So we can access it from anywhere
		mainwig = MainWidget()
		ActivitiesLayout.al = mainwig.ids.myscrollview.ids.activitieslayout

		#Window.size = (x, y)
		return mainwig

if __name__ == '__main__':
	MainApp().run()