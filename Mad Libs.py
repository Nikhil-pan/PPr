print(" ")
print("<||<||<|| MAD LIBS GENERATOR ||>||>||>")
print(" ")
print("Hey! Let's get started on your Mad Libs.")
print("Enter in words as specified below...")
print("")
print("")

name = input("Male name: ")
adj1 = input("Adjective 1: ")
adj2 = input("Adjective 2: ")
activity1 = input("Activity 1: ")
activity2 = input("Activity 2: ")
activity3 = input("Activity 3: ")
noun1 = input("Noun 1: ")
noun2 = input("Noun 2: ")
noun4 = input("Noun 4 (plural): ")
place1 = input("Place 1: ")
place2 = input("Place 2: ")

print("")

story_type=input("what story do you want the walmart one or the doctor one?(Wal/Doc):")

print("")

if (story_type=='Wal'):
    print(name, " is a ", adj1, noun1, " who lives in ", place1, " and is from a ", adj2, " family. He lives with his ", noun2, " who is the breadwinner of the family. She earns ", noun4, " by ", activity1, " at Walmart. When ", name, "'s ", noun2, " has free time they ", activity2, " together and have fun ", activity3, "in", place2, ".")


elif(story_type=='Doc'):
    print("most doctors agree that bicycle"+name+ "is a/an" + adj1 + "form of exercis"+adj2+"a bicycle enables"+ activity1+"and"+activity2+ "also" + activity3+ " around the world in" + place1+ "and" + place2+ noun1+noun2+noun4+"and hell is other people.")

print("")
print("The end!")
