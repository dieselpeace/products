#read
products = []
with open('products.txt', 'r') as f:
	for line in f:
		name, price = line.strip().split(',')
		products.append([name, price])

#input
products = []
while True:
	name = input('enter name: ')
	if name == 'q':
		break
	price = input('enter price: ')
	products.append([name, price])

#write
with open('products.txt', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
