def square(n):
  """Returns the square of a number."""
  squared = n ** 2
  print(f"{n} squared is {squared}")
  return squared
  
square(10)

""""""
#using python modules this is convenient and clear 
# no confusion
import math
print(math.sqrt(36))


""""""
#for analytical input and results use *args

#print() in a function only prints the data doesnt return it 
#so use return() to enable the using of it in another line of code

def biggest_number(*args):
  print(max(args))
  return (max(args))
    
def smallest_number(*args):
  print (min(args))
  return (min(args))

def distance_from_zero(arg):
  print (abs(arg))
  return (abs(arg))

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)


""""""
# defining parameters and conditions for a function
def shut_down(s):
  if s.lower()=="yes":
    return "shutting down"
  elif s.lower()=="no":
    return "Shutdown aborted"
  else:
    return "Sorry"
comm= input("shutdown?:")
print(shut_down(comm))



def distance_from_zero(dist):
  if type(dist)==int or type(dist)==float:
    return abs(dist)
  else:
    return "Nope"

num= int(input("enter a point: "))
print(distance_from_zero(num))


""""""
#trip cost calculations
def hotel_cost(nights):
  return 140*nights


def plane_ride_cost(city):
  if city.lower()=="charlotte":
    return 183
  elif city.lower()=="tampa":
    return 220
  elif city.lower()=="pittsburgh":
    return 222
  elif city.lower()=="los angeles":
    return 475
  


def rental_car_cost(days):
  if days>=7:
    return (40*days) - 50
  elif days>=3 and days<7:
    return (40*days) - 20
  elif days==1 or days==2:
    return 40*days
  else:
    return 0

def trip_cost(city,days,spending_money):
  nights=days - 1
  return rental_car_cost(days) + hotel_cost(nights) + plane_ride_cost(city) + spending_money

city=input("City? :")
"""recursion to make sure the city name is entered properly"""

def city_correct(city):
  if(city.lower()== 'los angeles' or city.lower()=="charlotte" or city.lower()=="tampa" or city.lower()=="pittsburgh"):
    days=int(input("no. of Days? :"))
    spending_money=int(input("Extra Money :"))

    print(trip_cost(city,days,spending_money))
  else:
    city=input("re-enter the city name properly:")
    city_correct(city)


city_correct(city)


#function arguments can be of any datatype,
#no need to mention it !

n = [3, 5, 7]
def print_list(x):
  for i in range(0, len(x)):
    print(x[i])
    
print_list(n)

#range can be passed as an argument to a list 
def my_function(x):
  for i in range(0, len(x)):
    x[i] = x[i]
  return x
print(my_function(range(3))) # Add your range between the parentheses!

#concatenating two strings
def join_strings(lst):
  result=""
  for i in range(len(lst)):
    result+=lst[i]
  return result

#list of lists in a function
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
def flatten(lst):
  results=[]
  for i in lst:
    for j in i:
      results.append(j)
  return results

print(flatten(n))