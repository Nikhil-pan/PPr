
print("""This is the Tip Calculator for your convenience.""")


bill_cost=int(input("How much was the bill?: $"))

tip_cost=int(input("How much do you want to tip the waiter?: $"))

bill_cost += tip_cost

num_people=int(input("How many people do you want to split the bill between ?: "))

tip_per_person = bill_cost/num_people


tip_per_person= "{:.2f}".format(tip_per_person)
''' round() method can also be used to round a float value to two decimal places
when the float has decimal values other than 0, if the decimal values are zero ex:86.00
it rounds off to 86.0

so we generally use format method'''

#tip_per_person =round(tip_per_person, 2)

print("Each person has to pay: $", tip_per_person)
