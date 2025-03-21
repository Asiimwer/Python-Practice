#Stores values to key(work like variables in a list)
prices = {'Bread':5000,'soda':4500, 'Choclate':8000, 'book':9000}
currency= "UGX"
total= prices['Bread'] + prices['Choclate'] + prices['soda']

for index, (items, price) in enumerate(prices.items(), start=1):
    print(f"{index} {items} {price}")

#This is how to add new items
prices['Water'] = 2000
# print(prices)

#This is how to overwrite another item
prices['Bread'] = 4500 
# print(prices)
# print(prices['Bread'],currency)
