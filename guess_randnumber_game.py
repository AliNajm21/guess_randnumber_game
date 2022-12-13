import random
score = 0
Quit = False
while Quit != True:
    namber = random.randint(1,20)
    for i in range(1,4):
        try:
            player_namber = int(input("guess the number between 1 ... 20 :"))
        except:
            print("please enter a vaild number")
        if player_namber == namber:
            print("you win")
            score += 1
            break
        elif player_namber < namber :
            print("the namber is > form yours")
        elif player_namber > namber :
            print("the namber is < from yours")
    print("score is: {}".format(score))
    if score == 5:
        Quit = True
        
    