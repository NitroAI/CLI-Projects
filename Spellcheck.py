import textblob#pip install textblob in cmd
from textblob import TextBlob#Importing the function
while True: 
    spelling = input("Ener Spelling Here: ")
    print("Spelling:",spelling)
    check = TextBlob(spelling)
    correct = str(check.correct())
    print("Correct Spelling is:",correct)
    if spelling==correct:
        print("Your spelling is correct:",spelling)
        print()
    elif spelling=="qqq":
        break
    else:
        print("Your Spellig is wrong!")
        print()


