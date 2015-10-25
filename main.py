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
			Color(0.529,0.792,0.435, 0.3)
			Rectangle(pos=self.pos, size=self.size)

	def unhighlight(self, *ignore):
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

	def __init__(self, **kwargs):
		super(ActivitiesLayout, self).__init__(**kwargs)
		self.lastselection = 0

	def addactivity(self):
		self.add_widget(ActivityLayout())

	def delactivity(self, toremove):
		self.remove_widget(toremove)
		ActivitiesLayout.childlist.remove(toremove)

	def pickchild(self):
		# Choose a random child from the childlist
		selection = 0

		# Let the same answer be selected more than once
		if self.randomness() == False:
			selection = random.choice(ActivitiesLayout.childlist)
			selection.getactinput()
			self.lastselection = selection

		while self.randomness() == True:
			selection = random.choice(ActivitiesLayout.childlist)
			if selection != self.lastselection:
				selection.getactinput()
				self.lastselection = selection
				break

		return selection

	def randomness(self):
		return len(ActivitiesLayout.childlist) > 3


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
		#self.pressed = False
		self.lastselection = 0
	
	def callback(self):
		try: self.lastselection.children[1].unhighlight()
		except AttributeError: pass
		self.lastselection = ActivitiesLayout.al.pickchild()


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