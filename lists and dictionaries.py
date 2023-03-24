#0 indexing for lists in python
#empty list
list=[]
list.insert(1,"apple")
print(list[0])

#to remove an element from the list remove method to be used
list.remove('apple')
print(list)


#for loop for operations on elements of the list
my_list = [1,9,3,8,5,7]
lst=[]
for number in my_list:
  lst.append(2*number)
print(*lst)


#to define a dictionary
dict={'alpharomeo':43,
      'betaromeo':44}

print(dict['alpharomeo'])

#delete from dictionary
del dict['betaromeo']

#if dict={key:list_value}
#we have direct access to the elements inside the list using dict['key][index]

inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'],
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']


inventory['pouch'].sort() 

inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] = inventory['gold'] + 50

print(inventory['pouch'][0])
print(inventory['gold'])


#for loops to print lists and dictionaries
names = ["Adam","Alex","Mariah","Martine","Columbus"]
webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}
#print the list
for i in names:
  print(i)

#print the dictionary
for i in webster:
  print(webster[i])
#here i iterates every key of webster but no order is guaranteed 
#every key is printed but no order is defined



def count_small(numbers):
  total = 0
  for n in numbers:
    if n < 10:
      total = total + 1
  return total
 
lotto = [4, 8, 15, 16, 23, 42]
small = count_small(lotto)
print(small)


#Write a function that counts how many times the string "fizz" appears in a list.

def fizz_count(x):
  count=0
  for i in x:
    if i=='fizz':
      count+=1
  return count

print(fizz_count(["fizz","cat","fizz"]))

lst=[]
print_letter="codecademy"
for i in print_letter:
  lst.append(i)
print(*lst)


