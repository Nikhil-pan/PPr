pig='ay'
print("Welcome to the Pig Latin Translator !")
word=input("Enter a Word: ")

if(len(word)>0 and word.isalpha()):
    print("Valid Word")
else:
    print("Invalid word, try again;")
    word=input("Enter a Word: ")
    if(len(word)>0 and word.isalpha()):
        print("Valid Word")

print(f"In Pig Latin {word} would be:",word[1:len(word)] + word[0] + pig)


