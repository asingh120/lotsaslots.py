'''
Progam: lotsaslots.py
Author: Amit
Date: 9/23/19

Program imitates a slot machine which randomly generates three numbers
between 0 - 9.  If all three numbers match, player gets JACKPOT. If two numbers
match, player gets TWO OF A KIND.  If none match, player gets a LOSS.  Program 
adds or deducts points from player total until player wins or loses all.
'''

from breezypythongui import EasyFrame
import random

class Slots(EasyFrame):

	def __init__(self):
		''' sets up the window and the widgets'''
		EasyFrame.__init__(self, "Lotsa Slots", width = 470, height = 355, background = 'powderblue')

		# sets up the labels and widgets
		self.title = self.addLabel(text = "Ready to Play?", row = 0, column = 0, columnspan = 3, sticky = "NSEW" ,background = 'powderblue', font = ("Helvetica", 20, 'italic'))
		self.first = self.addIntegerField(value = 0, row = 1, column = 0, rowspan = 2, width = 100)
		self.second = self.addIntegerField(value = 0, row = 1, column = 1, rowspan = 2, width = 100)
		self.third = self.addIntegerField(value = 0, row = 1, column = 2, rowspan = 2, width = 100)

		self.main = self.addLabel(text = "Let's Make Some Magic Baby", row = 3, column = 0, columnspan = 3, sticky = "NSEW", background = 'powderblue', font = ("Arial Black", 20))
		self.button = self.addButton(text = "Spin It", row = 4, column = 0, columnspan = 4, command = self.spin)
		self.lose = self.addLabel(text = "Total Points", row = 5, column = 0, columnspan = 2, sticky = "NSEW", background = 'powderblue', font = ("Helvetica", 14, 'bold'))
		self.fourth = self.addIntegerField(value = 100, row = 5, column = 1, columnspan = 2)
		self.addLabel(text = "", row = 6, column =0, columnspan = 4, sticky = "NSEW", background = 'powderblue')
		
		self.button["background"] = 'red'
		self.button["foreground"] = 'white'
		self.button["font"] = "Times+New+Roman"

	# Event Handler Method
	def spin(self):

		# Generates random numbers
		one = random.randint(0, 9)
		two = random.randint(0, 9)
		three = random.randint(0, 9)

		self.first.setValue(one)
		self.second.setValue(two)
		self.third.setValue(three)

		# Points Accumulator
		points = self.fourth.getNumber()

		# Game mechanics for deciding if there is a winner or not
		if one == two == three:	
			self.fourth.getNumber()
			points += 50
			self.fourth.setNumber(points)
			self.win = self.addLabel(text = "JACKPOT!!", row = 6, column = 0, columnspan = 4, sticky = "NSEW", background = 'yellow', font = ("Arial+Bold", 22, 'italic'))			
		elif one == two or one == three or two == three:
			self.fourth.getNumber()
			points += 30
			self.fourth.setNumber(points)
			self.runner = self.addLabel(text = "TWO OF A KIND!", row = 6, column = 0, columnspan = 4, sticky = "NSEW", background = 'lawngreen', font = ("Verdana", 18))
		else:
			self.fourth.getNumber()
			points -= 10
			self.fourth.setNumber(points)
			self.nowin = self.addLabel(text = "LOSS!", row = 6, column =0, columnspan = 4, sticky = "NSEW", background = 'powderblue', font = ("Helvetica", 14, 'bold'))
		if points == 0:
			self.lose = self.addLabel(text = "YOU'RE BROKE! GAME OVER!!", row = 6, column = 0, columnspan = 4, sticky = "NSEW", background = 'powderblue', font = ("Verdana", 18, 'bold'))

def main():
	Slots().mainloop()

main()
