# Import random module
import random
# Import time module
from time import sleep

# Variable for store Points
Machine_points = 0
user_points =0

# Game function for start the game
def start_game():

    # Global Variable for points 
    global Machine_points
    global user_points

    # For users game rules and instructions
    print("_"*60)
    print("="*19+"| Rock-Paper-Scissor |"+19*"=")
    print("-"*28+"GAME"+28*"-")
    print("Please Enter Your Choice:")
    print("Choice 1: Rock")
    print("Choice 2: Paper")
    print("Choice 3: Scissors")

    # Take user input for game
    try:
        user_choice = int(input("\nSelect any option from 1 to 3 :-> "))
        print("_"*60)

        if user_choice == 1:
            user_choice_str = "Rock"
        elif user_choice == 2:
            user_choice_str = "Paper"
        elif user_choice == 3:
            user_choice_str = "Scissor"
        else:
            print("\nSorry wrong option selected!\nPlease Enter right option and try again...\n")
            start_game()
    
    except Exception as e:
        print("\nSorry wrong option selected!\nPlease Enter right option and try again...\n")
        start_game()


    # Randint() function for generate random number
    machine_choice = random.randint(1,3)
    
    # Display machine choice
    print("\n[ Chooced by Machine :", end=" ")
    if machine_choice==1:
        print("Rock ]",end=" ")
    elif machine_choice==2:
        print("Paper ]",end=" ")
    else:
        print("Scissors ]",end=" ")

    print("[ Chooced by You :",user_choice_str,"]")

    # Declare who is the winner of the game and Add the points in the points variables
    if user_choice == machine_choice:
        print("+"+"-"*20+"( Ohh No, it's tie! )"+20*"-"+"+")
    elif user_choice == 1 and machine_choice==3:
        print("<"+"-"*15+"[ Congrats! You won the game! ]"+15*"-"+">")
        user_points += 1
    elif user_choice == 2 and machine_choice ==1:
        print("<"+"-"*15+"[ Congrats! You won the game! ]"+15*"-"+">")
        user_points += 1
    elif user_choice == 3 and machine_choice == 2:
        print("<"+"-"*15+"[ Congrats! You won the game! ]"+15*"-"+">")
        user_points += 1
    else:
        print("<"+"-"*15+"{ Sorry! Machine won the game! }"+15*"-"+">")
        Machine_points += 1

    # Points tracker for show the Machine and User points
    print("\n\t\t\t~POINTES~")
    print(f"\t\t[Machine : {Machine_points} | You : {user_points}]")
    print("_"*60)

    # Call play_again_game function
    play_again_game()

# play_again_game function for Play game again and again.
def play_again_game():
    # Ask user to play the game again
    play_again = input("\nDo you want to play again? (Yes/No) :-> ").lower()
    if play_again == "yes" or play_again == "y" or play_again == "ye" or play_again == "ya" or play_again =="yap":
        start_game()
    elif play_again == "no" or play_again == "n" or play_again == "nop" or play_again == "nah" or play_again =="noo":
        print("_"*60)
        print("\n","-"*14+": Thanks for playing the game! :"+14*"-")
        print(f"\n\t\t\tFinal Score\n\t\tMachine Score\t\t[ {Machine_points} ]\n\t\tYour Score\t\t[ {user_points} ]\n")
        if Machine_points > user_points:
            print(f"Final winner is Machine.\t With Score: [ {Machine_points} ]")
        elif Machine_points < user_points:
            print(f"Final winner is You.\t With Score: [ {user_points} ]")
        else:
            print("Ohh No! Match is TIE...")
        print("_"*60)
        sleep(5)
        exit()
    else :
        print("\nSorry wrong option selected!\nPlease Enter right option and try again...")
        print("_"*60)
        play_again_game()
        
# Start the Game 
start_game()