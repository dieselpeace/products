products = []
while True:
	name = input('product name: ')
	if name == 'q':
		break
	price = input('product price: ')
	if price == 'q':
		break
	p = [name, price]
	products = [p]
print(products)
