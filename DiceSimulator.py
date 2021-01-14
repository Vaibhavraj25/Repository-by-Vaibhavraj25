#importing Modules
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import random
#setting list for dice faces
a =  [".",":",".:","::",".::",":::"]
#defining command of dice button
def Command1(self):
#Getting random out of a
    Dice.text = (str(random.choice(a)))
#setting Dice color for different phases
    if Dice.text == "." :
    	Dice.color = (1,0,0,1)
    if Dice.text == ":::" :
    	Dice.color = (1,0,0,1)
    if Dice.text == ":" :
    	Dice.color = (0,0,1,1)
    if Dice.text == ".:" :
    	Dice.color = (0,0,1,1)
    if Dice.text == ".::" :
    	Dice.color = (0,0,1,1)
    if Dice.text == "::" :
    	Dice.color = (0,0,1,1)

#Making Dice button	
Dice = Button(text = "", color = (0,0,0,1),background_color = (3,3,3,1), font_size = 300, on_press = Command1)
#(3,3,3,1) = white as buttons have a dark shade
#creating class of layout and adding multiple kwargs in it as I use pure python	
class MyLayout(GridLayout):
	def __init__(self, **kwargs):
		super(MyLayout, self).__init__(**kwargs)
                #No of coloumns
                self.cols = 1
                # adding dice to layout
		self.add_widget(Dice)
		
#class for myapp	
class MyApp(App):
	def build(self):
		return MyLayout()
#running my app
MyApp().run()
