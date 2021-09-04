#modules
import time
import random

#Functions
def verify_dare(dare):
    verification = input("Are you sure that you want to ask: {0}  [Please enter Yes or No] ".format(dare))
    if verification == "Yes":
        print("Ok, let's do this!")
    elif verification == "No":
        dare = input("What are you asking?")
        verify_dare(dare)
    else:
        print("Invalid response. Please enter Yes or No.")
        verify_dare(dare)
    return 

def verify_players(num_players):
    if num_players == 1:
        return
    elif num_players == 2:
        return
    else:
        print("Invalid response. Please enter 1 or 2.")
        num_players = input("How many players are there? [Please enter 1 or 2]")
        verify_players(num_players)
    return

def verify_range(selected_range):
    if selected_range in zero_range:
        print("You have selected the range 1 to {0}. Your guesses must be the same number.".format(selected_range))
    elif selected_range in one_range:
        print("You have selected the range 1 to {0}. Your guesses must be the same or within 1 of each other.".format(selected_range))
    elif selected_range in two_range:
        print("You have selected the range 1 to {0}. Your guesses must be the same or within 2 of each other.".format(selected_range))
    elif selected_range in three_range:
        print("You have selected the range 1 to {0}. Your guesses must be the same or within 3 of each other.".format(selected_range))
    elif selected_range in four_range:
        print("You have selected the range 1 to {0}. Your guesses must be the same or within 4 of each other.".format(selected_range))
    elif selected_range in five_range:
        print("You have selected the range 1 to {0}. Your guesses must be the same or within 5 of each other.".format(selected_range))
    else:
        print("Invalid selection. Please pick 2,3,4,5,10,15,20,25,30,35,40,45,50")
        selected_range = int(input("Please enter the end number for your range based on the instructions given at the start. \n[Remember, the range starts at 1]"))
    return

def number_test(num_players, selected_range):
    if num_players == 1:
        num_one = int(input("You're playing against the AI today. Which number from 1 to {0} are you picking?".format(selected_range)))
        num_two = random.randrange(1,selected_range)
        if selected_range in zero_range:
            if num_one == num_two:
                print("The AI got your number, looks like you have to do it! The numbers chosen were {0} and {1}.".format(num_one, num_two))
            else:
                print("Looks like you're safe today, the numbers chosen were {0} and {1}.".format(num_one, num_two))
        elif selected_range in one_range:
            possibilites = range((num_one - 1), (num_one + 1))
            if num_two in possibilites:
                print("The AI got your number, looks like you have to do it! The numbers chosen were {0} and {1}.".format(num_one, num_two))
            else:
                print("Looks like you're safe today, the numbers chosen were {0} and {1}.".format(num_one, num_two))
        elif selected_range in two_range:
            possibilites = range((num_one - 2), (num_one + 2))
            if num_two in possibilites:
                print("The AI got your number, looks like you have to do it! The numbers chosen were {0} and {1}.".format(num_one, num_two))
            else:
                print("Looks like you're safe today, the numbers chosen were {0} and {1}.".format(num_one, num_two))
        elif selected_range in three_range:
            possibilites = range((num_one - 3), (num_one + 3))
            if num_two in possibilites:
                print("The AI got your number, looks like you have to do it! The numbers chosen were {0} and {1}.".format(num_one, num_two))
            else:
                print("Looks like you're safe today, the numbers chosen were {0} and {1}.".format(num_one, num_two))
        elif selected_range in four_range:
            possibilites = range((num_one - 4), (num_one + 4))
            if num_two in possibilites:
                print("The AI got your number, looks like you have to do it! The numbers chosen were {0} and {1}.".format(num_one, num_two))
            else:
                print("Looks like you're safe today, the numbers chosen were {0} and {1}.".format(num_one, num_two))
        elif selected_range in five_range:
            possibilites = range((num_one - 5), (num_one + 5))
            if num_two in possibilites:
                print("The AI got your number, looks like you have to do it! The numbers chosen were {0} and {1}.".format(num_one, num_two))
            else:
                print("Looks like you're safe today, the numbers chosen were {0} and {1}.".format(num_one, num_two))
    elif num_players == 2:
        num_one = int(input("You're playing against someone else today. Which number from 1 to {0} are you picking?".format(selected_range)))
        num_two = int(input("You're being challenged. Which number from 1 to {0} are you picking?".format(selected_range)))
        if selected_range in zero_range:
            if num_one == num_two:
                print("You got their number, looks like they have to do it! The numbers chosen were {0} and {1}.".format(num_one, num_two))
            else:
                print("Looks like they're safe today, the numbers chosen were {0} and {1}.".format(num_one, num_two))
        elif selected_range in one_range:
            possibilites = range((num_one - 1), (num_one + 1))
            if num_two in possibilites:
                print("You got their number, looks like they have to do it! The numbers chosen were {0} and {1}.".format(num_one, num_two))
            else:
                print("Looks like they're safe today, the numbers chosen were {0} and {1}.".format(num_one, num_two))
        elif selected_range in two_range:
            possibilites = range((num_one - 2), (num_one + 2))
            if num_two in possibilites:
                print("You got their number, looks like they have to do it! The numbers chosen were {0} and {1}.".format(num_one, num_two))
            else:
                print("Looks like they're safe today, the numbers chosen were {0} and {1}.".format(num_one, num_two))
        elif selected_range in three_range:
            possibilites = range((num_one - 3), (num_one + 3))
            if num_two in possibilites:
                print("You got their number, looks like they have to do it! The numbers chosen were {0} and {1}.".format(num_one, num_two))
            else:
                print("Looks like they're safe today, the numbers chosen were {0} and {1}.".format(num_one, num_two))
        elif selected_range in four_range:
            possibilites = range((num_one - 4), (num_one + 4))
            if num_two in possibilites:
                print("You got their number, looks like they have to do it! The numbers chosen were {0} and {1}.".format(num_one, num_two))
            else:
                print("Looks like they're safe today, the numbers chosen were {0} and {1}.".format(num_one, num_two))
        elif selected_range in five_range:
            possibilites = range((num_one - 5), (num_one + 5))
            if num_two in possibilites:
                print("You got their number, looks like they have to do it! The numbers chosen were {0} and {1}.".format(num_one, num_two))
            else:
                print("Looks like they're safe today, the numbers chosen were {0} and {1}.".format(num_one, num_two))
    return

#Variables
possible_ranges = [2,3,4,5,10,15,20,25,30,35,40,45,50]
zero_range = [2,3,4,5]
one_range = [10,15]
two_range = [20,25]
three_range = [30,35]
four_range = [40,45]
five_range = [50]



#Program

##Introduction 
print("Welcome to the Python version of the infamous 'What are the odds?' game! \n Normally this game is sporadically played amongst friends in public, but in this program I will make it possible to play this game against an AI, or by using hidden inputs from two separate players.")
print("Overview and Rules:")
print("The point of this game is to introduce a risk factor to whether or not yourself, or someone else will have to do a proposed task.")
print("Examples: Taking a shot, doing something embarassing in public, eating that dessert, buying that plane ticket, etc.")
print("The game starts whenever an individual proposes a task. After that, the person who this is directed toward has to pick a range of numbers depending on how willing they are to do it.")
print("After they pick a range, two numbers must be picked (if playing against an AI, it will be random on their part). The goal if you're the one asking, is to guess the same number as the person you're asking.")
print("Note: These numbers are to be kept secret.")
print("Also, depending on the range, there is a certain error range allowed between the guesses.")
print("You must pick a range from 1 to 2, 3, 4, 5, or any multiple of 5 after that up to 50.")
print("Any range from 1 up to 5, the numbers guessed have to be exactly the same.")
print("From 1-10 or 1-15, the error range is ±1")
print("From 1-20 or 1-25, the error range is ±2")
print("From 1-30 or 1-35, the error range is ±3")
print("From 1-40 or 1-45, the error range is ±4")
print("From 1-50 the error range is ±5.")
print("After the range is set, and each player has secretly selected a number, both numbers will be displayed along with a message stating whether or not the person has to do the proposed task. ")

##Execution
time.sleep(5)
num_players = int(input("How many players are there? [Please enter 1 or 2]"))


verify_players(num_players)

dare = input("What are you asking? [Tip: Use the format 'What are the odds that ________?'")
verify_dare(dare)

selected_range = int(input("Please enter the end number for your range based on the instructions given at the start. \n[Remember, the range starts at 1]"))
verify_range(selected_range)

number_test(num_players,selected_range)


