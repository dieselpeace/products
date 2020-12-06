import os

def read_file(filename):
	products = []
	with open(filename, 'r') as f: #read
		for line in f:
			if 'products, price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

def user_input(products):
	while True:
		name = input('enter name: ')
		if name == 'q':
			break
		price = input('enter price: ')
		price = int(price)
		products.append([name, price])
	return products
	
def write_file(filename, products):
	with open(filename, 'w') as f: 
		f.write('products, price\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	filename = 'products.txt'
	if os.path.isfile(filename): #chech if file is there
		products = read_file(filename)
	else: 
		print('file not found')

	products = user_input(products)
	write_file('products.txt', products)

main()

