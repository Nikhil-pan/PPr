# Keeping Track of the Produce

prices={
  "banana":4,
  "apple":2,
  "orange":1.5,
  "pear":3
}
stock={
  "banana":6,
  "apple":0,
  "orange":32,
  "pear":15
}

for key in stock:
  print(key)
  print(f"price: {prices[key]}")
  print("stock: %s" % stock[key])
total=0
#to check total and print it
for key in prices:
  tota=(prices[key]*stock[key])
  print(tota)
  total=total+tota
print(total)

# a function to add the total amount and deduce the stock as per requirement
shopping_list = ["banana", "banana","orange", "apple"]

def compute_bill(food):
  total=0
  for item in food:
    if stock[item]>0:
      total+=prices[item]
      stock[item]-=1
  return total

print("bill for shopping list: ",compute_bill(shopping_list))

print("stock left:")
for key in stock:
  print(key)
  print("stock: %s" % stock[key])