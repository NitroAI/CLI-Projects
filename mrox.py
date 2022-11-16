##Luck Store
import random
a = ["Rock","Paper","Scisor"]
x = 0
y = 0
while True:
    b = int(input('''
 Sellect Now Lets See Who will win (Computer or You)! :) 
        1 Rock
        2 Paper
        3 Scesor

>> '''))
    print()
    if b == 1:
       print("You Sellected: Rock")
    elif b == 2:
        print("Your Sellected: Paper")
    elif b == 3:
        print("You Sellected: Scesor")
    else:
        print("Hey Man :( Out Of Box!!!")
        break
    rd = random.choice(a)
    print("Computer Sellected: ",rd)
    if b == 1 and rd == "Rock":
        print(">> Draw")
    elif b == 2 and rd == "Paper":
        print(">> Draw")
    elif b == 3 and rd == "Scisor":
        print(">> Draw")
    elif (b == 1 and rd == "Paper") or (b == 2 and rd == "Scisor") or (b == 3 and rd == "Rock"):
        print("<< Computer Win!")
        x+=1
        print("<< Computer Score:",x)
    else:
        print(">> You Win")
        y+=1
        print("Your Score:",y)
    if x == 10:
        print("Finished","Computer Won!!!")
        break
    elif y == 10:
        print("Finished! You Won!!!")
        break
    else:
        pass

    
