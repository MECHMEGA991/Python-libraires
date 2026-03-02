# Temperature list
li=[25.2,56.9,44.2,12.0,78.9]

print(li)

# In list we use for loop to calculate avg
total=0
for i in li:
    total+=i

avg=total/len(li)

print(round(avg,2))

# So li is useful for small dataset  but in large dataset million of data analyze 
# To overcome this problem we use numerical python libraies called numpy 
