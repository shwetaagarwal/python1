import random

class Die(object): #class inherits from object class
	def __init__(self,sides):
		self.sides = sides
	
	def roll(self):
		return random.randint(1,self.sides)

class Deck(object):
	def shuffle(self):
		suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
		ranks = ["1","2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
		
		#cards = []  #add self so that it can be used across the class
		self.cards = []
		for suit in suits:
			for rank in ranks:
				self.cards.append(rank + " of " + suit)
		
		random.shuffle(self.cards)
	
	def deal(self):
		return self.cards.pop()
	
d = Deck()
d.shuffle()
print(d.deal())
print(d.deal())
print(d.deal())
print(d.deal())
