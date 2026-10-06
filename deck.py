import random
suits=['HEART', 'DIAMONDS','CLUB','SPADE']
ranks=['2','3','4','5','6','7','8','9','10','Jack','Queen','King']
deck=[rank + " of " + suit for suit in suits for rank in ranks]

random.shuffle(deck)
print("shuffled deck of cards: ")
for card in deck:
	print(card)
