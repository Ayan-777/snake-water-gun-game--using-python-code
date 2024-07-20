 #        <<<<<<<<<<<<<<< SNAKE  WATER  GUN  GAME >>>>>>>>>>>>>>>>



'''
(s) = Snake
(w) = Water
(G) = Gun

# '''


import random
randNo = random.randint(1,3)
def gamewin(comp,you,):
    if comp == you:
        return "GAME TIE"
    elif comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True
    elif comp == "w":
        if you == "s":
            return True
        elif you == "g":
            return False
    elif comp == "g":
        if you == "s":
            return False
        elif you == "w":
            return True    

print ("compter Turn : (s), (w), (g)")

if randNo == 1:
    comp = "s"
elif randNo == 2:
    comp = "w"
elif randNo == 3:
    comp = "g"   

you = input("you choose one = (S) (W) (G) : ")  
a = gamewin(comp, you)
print (f"Computer chose :{comp}")
print (f"You are chose : {you}")

if comp == you:
    print("<<< GAME IS TIE >>>")
   
elif False:
    print("<<< YOU WIN THIS GAME >>>")
else :
    print("<<< YOU LOOSE THIS GAME>>>") 
    

## Thank you for playing 😊


