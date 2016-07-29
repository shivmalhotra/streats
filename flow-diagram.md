User: Alexa, ask streats to order
Alexa: Reoder last order?

User: 
	a) Yes 
	b) No (move to line 9) *
	c) Nevermind/Cancel (exit app)

Alexa: what would you like?

User: 
	a) I want to order X (X = food type, cuisine) (move to line 15)
	b) I want to order from X (X = restaurant) (move to line 27) *
	c) I want to order Y (Y = food) from X (X = restaurant) (if found move to line 30 else move to line 65)
	d) Nevermind/Cancel (Go to line 2)

Alexa: Do you want cheapest or fastest? (Handled by us in the backend)

User: (Can say either)

Alexa: would you like to order from X (X = restaurant)

User:
	a) Yes - move to branch b
	b) No - X++, back to line 19

Alexa: What Would you like to order from X?

User: 
	a) Y (Y = menu item) (Go to line 34) *
	b) Cancel/Nevermind (Go to line 9)

Alexa:
	a) Alright I found Y (Y = closest item on menu). Would you like to order this? (Go to line 37) *
	b) I couldn't find the item you specifed. (Go back to line 25)

User:
	a) Yes (Go to line 41) *
	b) No (Go to line 25)

Alexa: Alright, I've added Y to the cart. Would you like to order anything else?

User:
	a) Yes (Go to line 27)
	b) No (Go to line 48) *
	c) Nevermind/Cancel/Remove (Go to line 55)

Alexa: I've sent an order confirmation to your phone, should I place the order?

User:
	a) Yes (Go to line 56) *
	b) No (Go to line 54)

Alex: Order canceled (Go to line 2) 

Alexa: Alright I've placed your order. It should come in around (wait time). Would you like to order anything new?

User:
	a) Yes (Go to line 9)
	b) No (Exit app) *

Alexa:
	Alright I've removed Y.  (Go to line 27)

Alexa: I can't seem to find that restaurant (Go to line 9)