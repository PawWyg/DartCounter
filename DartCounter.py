# DartCouter

import time

print("### Welcome to DartCouter ###\n")

gameInProgress = True
gameChoice = True
gameOn = True

time.sleep(1)

while gameInProgress:

    print("Please choose: \n",
          "1 - Play with yourself\n",
          "2 - Two players game\n",
          "0 - Exit\n")
          
    choice = int(input("Your choice: \n"))
    print("--------------------------------------------")
    time.sleep(1)

    
    if choice == 2:

        print("Your choice is \"Two players game\" \n")
        count = int(input("Choose the numer of count: 501, 401, 301\n"))
        print(" ")

        if count == 501 or count == 401 or count == 301:

            print("Your choice is: ", int(count))
            print("Let\'s play dart\'s")
            print("--------------------------------------------\n")
            print("GAME ON!\n")

            
            p1turn = True
            p2turn = False
            counter_1 = count
            counter_2 = count
            turn = 1
            n1, n2 = 1 #throws
            average = 0 
            throws = 0
            left_1 = count
            left_2 = count

            while gameOn:

                    
                print("** TURN ", int(turn),"**\n")
                
                #PLAYER 1 TURN
                while p1turn:
                        
                    print("Player one turn\n")
                        
                    throw_1 = int(input("First throw: "))                              
                    throw_2 = int(input("Secord throw: "))
                    throw_3 = int(input("Third throw: "))
                   
                    print()
                    score_1 = throw_1 + throw_2 + throw_3
                    left_1 = counter_1 - score_1
                    throws = throws + score_1
                
                    if left_1 == 0:
                        
                        print("Player one WIN!\n")
                        average_1 = throws / n1
                        print("#" * 33)
                        print("#    END - NICE THROWS          #")
                        print("#    Your average: ", round(float(average_1), 3),"      #")
                        print("#    Numers of turns: ", int(turn),"       #")
                        print("#" * 33)
                        print()
                        p1turn = False
                        p2turn = False
                        gameOn = False
                            
                        
                    elif left_1 > 0:
                        
                        print("You threw: ", int(score_1))
                        counter_1 = counter_1 - score_1
                        average_1 = throws / n1
                        print("Your left score: ", int(counter_1),"\n")
                        print("Your average is: ", float(average_1),"\n")
                        print("--------------------------------------------")
                        n1 = n1 + 1
                        p1turn = False
                        p2turn = True
                    
                    elif left_1 < 0:
                        print("You threw to much! You have: ", int(counter_1)," to end\n")
                        p1turn = False
                        p2turn = True
                        
                #PLAYER 2 TURN
                while p2turn:

                    print("Player two turn\n")
                    
                    throw_1 = int(input("First throw: "))
                    throw_2 = int(input("Secord throw: "))
                    throw_3 = int(input("Third throw: "))
                    
                    score_2 = throw_1 + throw_2 + throw_3
                    left_2 = counter_2 - score_2
                    throws = throws + score_2
                    
                    if left_2 == 0:
                        print("Player two WIN!\n")
                        average_2 = throws / n2
                        print("#" * 33)
                        print("#    END - NICE THROWS          #")
                        print("#    Your average: ", round(float(average_2), 3),"      #")
                        print("#    Numers of turns: ", int(turn),"       #")
                        print("#" * 33)
                        print()
                        p1turn = False
                        p2turn = False
                        gameOn = False
                            
                        
                    elif left_2 > 0:
                        print("You threw: ", int(score_2))
                        counter_2 = counter_2 - score_2
                        average_2 = throws / n
                        print("Your left score: ", int(counter_2),"\n")
                        print("Your average is: ", float(average_2),"\n")
                        print("--------------------------------------------")
                        n2 = n2 + 1
                        p1turn = True
                        p2turn = False
                    
                    elif left_2 < 0:
                        print("You threw to much! You have: ", int(counter_2)," to end\n")
                        p1turn = True
                        p2turn = False

                turn = turn + 1
                print("--------------------------------------------\n")

        else:
            print("    !!!WRONG VALUE ENTERED !!!")
            print("!!! RE-ENTER THE CORRECT VALUE !!!")
            print("--------------------------------------------\n")
        
    elif choice == 1:
            
        print("Your choice is \"Play with yourself\" \n")
        counter = int(input("Enter your counter: \n"))
        print("--------------------------------------------")
        print("YOUR SCORE: ", int(counter),"\n")
        gameOn = True
        n = 1 #throws
        average = 0
        turn = 1
        throws = 0
        print("GAME ON!\n")
        print("--------------------------------------------")
            
        while gameOn:

            print("TURN: ", int(turn),"\n ")
            throw_1 = int(input("First throw: "))
            throw_2 = int(input("Secord throw: "))
            throw_3 = int(input("Third throw: "))
            print(" ")
            score = throw_1 + throw_2 + throw_3
            left = counter - score
            throws = throws + score
                
            if left > 0:
                    
                average = throws / n
                print("You threw: ", int(score),"\n")
                counter = counter - score
                print("Your left score: ", int(counter),"\n")
                print("Your average is: ", float(average),"\n")
                print("--------------------------------------------")
                turn = turn + 1
                n = n + 1
                    
            elif left == 0:

                average = throws / n
                print("#" * 33)
                print("#    END - NICE THROWS          #")
                print("#    Your average: ", round(float(average), 3),"      #")
                print("#    Numers of turns: ", int(turn),"       #")
                print("#" * 33)
                print()
                gameOn = False

            elif left < 0:

                print("You threw to much!")
                average = average
                turn = turn + 1
                
                
                
    elif choice == 0:
        print("GOOD BYE!")
        gameInProgress = False
            
            
    else:
        print("You can choose 0, 1 or 2!\n")
           

