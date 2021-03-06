
import os # operating system

products = []

# 檢察檔案在不在
if os.path.isfile('products2.csv'):
	# 讀取檔案
	with open('products2.csv', 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('找不到檔案')



# 讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
print(products)

# 印出所有購買紀錄
for p in products:
	print('The price of ', p[0], 'is ', p[1])

# 寫入檔案
with open('products2.csv', 'w', encoding = 'utf-8-sig') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

