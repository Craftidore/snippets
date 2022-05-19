play = "yes"
pa = 0
number_of_deaths = 1
name = input("what is your name? ")
while True:
    play == "yes"
    print("------------start------------")
    if pa == 1:
        if number_of_deaths == 2:
            A = 0
        elif number_of_deaths == 3:
            A = 1
        else:
            A = 2
    inventory = ["torch", "sword", "whip", "shield"]
    import time
    import random
    b = False
    machete = 1
    where = 0
    q = 0
    p = 0
    money = 0
    hp = 60
    direction1 = 0
    to_kill_a_king = 0
    win = 0
    th = 0
    _2 = "0"
    a = 0# for while true
    c = 0
    #
    #
    #
    #
    #
    if name == "cheating is what I do":
        hp = 640
    if name == "quit":
        break
    print("please keep words in lowercase and do not put spaces before or after the word.")
    print('you are on a circular island, on which a lion, who lives in the jungle, is king. you want to become king. (after leaving the jungle type lion to visit him). type info instead of right or left for "how to win," you may also do "hints/tips" for exactly that')
    print("you can go right and go to the cave or go left to the beach")
    time.sleep(3)
    _1 = 1
    while True:
        a == 0
        if name == "idiot":
            print("you are to stupid to survive on this island") 
            break
        if _1 == 1:
            while True:
                _1 == 1
                direction1 = input("right or left? ")
                if direction1 == "right":
                    where = where + 1
                    a = 0
                    break
                elif direction1 == "left":
                    where = where + 2
                    a = 0
                    break
                elif (direction1 == "lion" and where == 3):
                    where = "3.5"
                    a = 0
                    break
                elif direction1 == "info":
                    print("to win, visit the lion five(5)(V) times in one life (and survive) to win")
                elif direction1 == "hints/tips":
                    print("    you need a machete to go into the jungle")
                    print("    you can get it if you choose to stay in the cave")
                    print("    use anything but the torch when facing the gorilla")
                    print("    the lion normally deals you 200 damage")
                    print("    you may immedietly quit by puting quit instead of your name")
                elif direction1 == "secret info":
                    print('if you anger the doc, the lion deals you half the damage. the cheating name is "cheating is what I do"')
                else:
                    if pa == 0:
                        print(name, "thinks for a while")
                    elif A == 0:
                        print(name, " the ", number_of_deaths, "nd, thinks for a while")
                    elif A == 1:
                        print(name, " the ", number_of_deaths, "rd, thinks for a while")
                    else:
                        print(name, " the ", number_of_deaths, "th, thinks for a while")
                    time.sleep(1)
        if where == 1:
            print ("you walk into the cave and a snake bites you lose 20 hp")
            hp = hp - 20
            time.sleep(0.5)
            if hp <= 0:
                break
            if machete == 1:
                while True:
                    a == 0
                    cave = input ("do you want to continue in the cave or leave (cave, leave) ")
                    if cave == "leave":
                        break
                    elif cave == "cave":
                        print ("you find some ore and make a machete")
                        machete = 0
                        break
                    else:
                        if pa == 0:
                            print(name, "thinks for a while")
                        elif A == 0:
                            print(name, " the ", number_of_deaths, "nd, thinks for a while")
                        elif A == 1:
                            print(name, " the ", number_of_deaths, "rd, thinks for a while")
                        else:
                            print(name, " the ", number_of_deaths, "th, thinks for a while")
                        time.sleep(1)
            print ("you find the exit and leave the cave")
            time.sleep(0.5)
            print ("your health is ", hp)
            print ("you have $", money)
            print ("you can turn right and go to the beach or go left to the jungle")
        if where == 2:
            print ("you go to the beach")
            time.sleep(0.5)
            money = money + 50
            print ("you find 50 dollars")
            if hp <= 0:
                break
            time.sleep(0.5)
            print ("your health is ", hp)
            print ("you have $", money)
            print ("you can turn right and go to the jungle or go left to the desert")
        if where == 3:
            print ("you reach the jungle")
            if machete == 1:
                print ("you have no machete")
                print ("you leave the jungle and go to the desert")
                where = 4
            else:
                print ("you use your machete to hack through the jungle")
                time.sleep(0.5)
                print ("you search for somthing in your backpack.")
                time.sleep(0.5)
                
                hand1 = "0"
                hand1 = random.choice(inventory)
                time.sleep(0.5)
                print ("a", hand1, "is in your hand")
                while True:
                    a == 0
                    redo_search = input("would you like to search for something else instead? (yes, no) ")
                    if redo_search == "yes":
                        hand1 = random.choice(inventory)
                        time.sleep(0.5)
                        print ("a", hand1, "is in your hand")
                        break
                    elif redo_search == "no":
                        break
                    else:
                        if pa == 0:
                            print(name, "thinks for a while")
                        elif A == 0:
                            print(name, " the ", number_of_deaths, "nd, thinks for a while")
                        elif A == 1:
                            print(name, " the ", number_of_deaths, "rd, thinks for a while")
                        else:
                            print(name, " the ", number_of_deaths, "th, thinks for a while")
                        time.sleep(1)
                time.sleep(0.5)
                print ("you get in a fight with a gorilla")
                while True:
                    a == 0
                    print ("do you want to use what is in your hand")
                    _2 = input ("yes or no ")
                    if _2 == "yes":
                        if hand1 == "sword":
                            print ("you kill it with your sword")
                            print ("you find $25")
                            money = money + 25
                        elif hand1 == "torch":
                            print ("you scorch him, and he gets angrier, he beats you up really bad")
                            print ("lose 150 hp")
                            hp = hp - 150
                        else:  
                            if hand1 == "whip":
                                print ("you whip him and he runs away")
                            else:
                                print ("the shield absorbs most of the damage")
                                print ("lose 40 hp")
                                hp = hp - 40
                        break
                    elif _2 == "no":
                        print ("you get beat up pretty bad")
                        print ("lose 90 hp")
                        hp = hp - 90
                        break
                    else:
                        if pa == 0:
                            print(name, "thinks for a while")
                        elif A == 0:
                            print(name, " the ", number_of_deaths, "nd, thinks for a while")
                        elif A == 1:
                            print(name, " the ", number_of_deaths, "rd, thinks for a while")
                        else:
                            print(name, " the ", number_of_deaths, "th, thinks for a while")
                        time.sleep(1)

                time.sleep(0.5)
                if hp <= 0:
                    break
                print("you find your way out of the jungle")
                print ("your health is ", hp)
                print ("you have $", money)
                print ("do you want to go right to the desert or left to the doctors hut")
        if where == "3.5":
            print("you find the king")
            if b == True:
                #you have angered his doctor and he likes it
                print("you attack him and he deals you 100 damage")
                hp += -100
            else:
                print("you attack him and he deals you 200 damage")
                hp += -200
            if (not hp <= 0):
                to_kill_a_king += 1
                if to_kill_a_king == 5:
                    win = 1
                    break
                print("you find your way out of the jungle")
                print ("your health is ", hp)
                print ("you have $", money)
            else:
                break
            where = 3
            print ("do you want to go right to the desert or left to the doctors hut")
        if where == 4:
            # desert enter + low chance of death of thirst
            print ("you go to the desert")
            c = 0
            while True:
                a == 0
                time.sleep(0.5)
                dc = random.randint(0, 10)
                if dc == 0:
                    th = 1
                    break
                else:
                    print ("you find an oasis")
                    d = random.randint(1, 10)
                    d = d + c
                    c = c + 1
                    if d > 7:
                        print ("you find your way out of the desert")
                        break
                    else:
                        time.sleep(0.5)
                        print ("you wander around the desert trying to find a way out")
            if th == 1:
                break
            time.sleep(0.5)
            print ("your health is ", hp)
            print ("you have $", money)
            print ("you can turn right and go to the doctors hut or go left to the cave")
        if where == 5:
            if b == False:
                print ("the doctor will heal 20 health for $25")
                while True:
                    a == 0
                    _2 = input ("do you want to be healed?  (yes, no) ")
                    if _2 == "yes":
                        if money == 25:
                            print ("you pay him $", money)
                            _3 = money / 25
                            money = 0
                            _3 = _3 * 20
                            print ("you are healed ", _3, " health")
                            hp += _3
                            break
                        elif money > 25:
                            print ("you pay him $", money)
                            _3 = money / 25
                            money = 0
                            _3 = _3 * 20
                            print ("you are healed ", _3, " health")
                            hp += _3
                            break
                        else:
                            print ("you have no money")
                            print ("the doc says he'll never doctor you again. then he beat you up")
                            print ("lose 40 hp")
                            hp = hp - 20
                            b = True
                            break
                    elif _2 == "no":
                        print ("the doc says he'll never doctor you again. then he beats you up")
                        print ("lose 20 hp")
                        if hp <= 0:
                            q = 1
                        hp = hp - 20
                        b = True
                        break
                    else:
                        if pa == 0:
                            print(name, "thinks for a while")
                        elif A == 0:
                            print(name, " the ", number_of_deaths, "nd, thinks for a while")
                        elif A == 1:
                            print(name, " the ", number_of_deaths, "rd, thinks for a while")
                        else:
                            print(name, " the ", number_of_deaths, "th, thinks for a while")
                        time.sleep(1)
                    if hp <= 0:
                        break
                    print ("your health is ", hp)
                    print ("you have $", money)
            else:
                print ('the doctor says "I told you I will never heal you again" the docter beats you up, lose 40 hp')
                hp = hp - 40
            if hp <= 0:
                break
            print ("your health is ", hp)
            print ("you have $", money)
            print ("you can go right to the cave or left to the beach")
        if _1 == 0:
            _1 = 1
        if where > 5:
            where = where - 5
            _1 = 0
    if th == 1:
        print("you died of thirst, game over")
    elif win == 1:
        print("the lion dies")
        print("you claim the crown and claim the island your domain")
        print("you win, game over")
    else:
        print ("you died, game over")

    pa = 1
    number_of_deaths += 1
    print ("would you like to play again")
    while True:
        a == 0
        p = input("yes, no ")
        if p == "yes":
            break
        elif p == "no":
            break
        elif win == 0:
            print("You cant think for a while! Your dead!")
        else:
            print("our new hero thinks for a while")
    play = p
    if play == "no":
        break
print("what is wrong with you?!!! DO YOU NOT LIKE MY GAME?")
print("end of session")
