# --------------------------------------------------
quantity = 100
itemPrice = 100
# --------------------------------------------------
def cantTotal_no():
	basePrice = quantity * itemPrice
	if (basePrice > 1000):
		return basePrice * 0.95
	else:
		return basePrice * 0.90
# ..................................................
def basePrice():
	return quantity * itemPrice

def cantTotal_si():
	if (basePrice() > 1000):
		return basePrice() * 0.95
	else:
		return basePrice() * 0.90
# --------------------------------------------------
print (cantTotal_no())
print ("..................................................")
print (cantTotal_si())
