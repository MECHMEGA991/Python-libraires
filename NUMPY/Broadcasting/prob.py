prices = [100,200,300]

discount = 10 # 10%

final_prices=[]

for price in prices:

    final_price =price - (price * discount/100 ) 
    final_prices.append(final_price)

print(final_prices)

# To solve this problem we use numpy broadcasting without using loop
# Broadcasting allows Numpy to perform Operations on arrays of different shape