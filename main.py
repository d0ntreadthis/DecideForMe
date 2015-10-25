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
from kivy.graphics import Color, Rectangle
from kivy.graphics.instructions import InstructionGroup
from kivy.clock import Clock
import random


class ActivityInput(TextInput):
	# Should have a method that will change the color of the background
	# for 10 secs, then go back to default
	
	def highlight(self):
		# highlight an instance of ActivityInput

		with self.canvas.after:
			Color(0, 1, 0, 0.2)
			Rectangle(pos=self.pos, size=self.size)

		# Trigger the unhighlight function after 3.5secs
		Clock.schedule_once(self.unhighlight, 3.5)

	def unhighlight(self, dt):
		with self.canvas.after:
			self.canvas.after.clear()



class DeleteBtn(Button):
	# Should have an image of a bin on it, rather than the word del
	
	def callback(self):
		ActivitiesLayout.al.delactivity(toremove=self.parent)


class ActivityLayout(BoxLayout):

	def __init__(self, **kwargs):
		super(ActivityLayout, self).__init__(**kwargs)
		ActivitiesLayout.childlist.append(self)

	def getactinput(self):
		# Highlight the ActivityInput of the ActivityLayout
		self.children[1].highlight()
	

class ActivitiesLayout(GridLayout):

	childlist = [] # To keep a reference of all children

	def addactivity(self):
		self.add_widget(ActivityLayout())

	def delactivity(self, toremove):
		self.remove_widget(toremove)
		ActivitiesLayout.childlist.remove(toremove)

	def pickchild(self):
		# Choose a random child from the childlist
		selection = random.choice(ActivitiesLayout.childlist)
		selection.getactinput()


class MyScrollView(ScrollView):
	pass


class AddBtn(Button):

	def callback(self):
		ActivitiesLayout.al.addactivity()


class DecideBtn(Button):
	# When pressed, this should highlight a random activity in the list
	# for roughly 5 seconds?

	def __init__(self, **kwargs):
		super(DecideBtn, self).__init__(**kwargs)
		self.pressed = False
	
	def callback(self):
		# To prevent the callback from running when an activity is
		# already highlighted

		if self.pressed == True:
			pass

		elif self.pressed == False:
			self.pressed = True
			ActivitiesLayout.al.pickchild()
			Clock.schedule_once(self.pressedfunc, 3.5)

	def pressedfunc(self, dt):
		self.pressed = False


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