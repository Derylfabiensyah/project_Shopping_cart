print('='*20)
print('KERANJANG BELANJA')
print('='*20)

foods = []
prices = []
total = 0

while True:
    food = input('Masukan nama barang (k untuk keluar): ')
    if food.lower() == 'k':
        break
    else :
       price = float(input(f'Masukan harga {food}: Rp.'))
       foods.append(food)
       prices.append(price)
       
print('----- BELANJAAN MU-----')

for food in foods:
    print(food,end=' ')
    
for price in prices:
    total += price
    
print ()
print(f'Total belanjaan: Rp.{total}')      