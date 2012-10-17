# Rock-paper-scissors-lizard-Spock template

# Import random number module
import random

# Import math module might not be necessary here but cannot hurt
import math

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    # fill in your code below
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return ""
    # convert number to a name using if/elif/else
    # don't forget to return the result!

    
def name_to_number(name):
    # fill in your code below
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return ""
    # convert name to number using if/elif/else
    # don't forget to return the result!


    
def rpsls(name):
    # fill in your code below
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    name = player_number

    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    number = comp_number

    
    # compute difference of player_number and comp_number modulo five
    diff = (comp_number - player_number) % 5

    
    # use if/elif/else to determine winner
    if 0 < diff <= 2:
        print "Player Wins"
    elif diff >= 3:
        print "Computer Wins"
    elif diff == 0:
        print "Tie"
    else:
        print""
    
    # convert comp_number to name using number_to_name
    comp_number = number_to_name(name)

    # print results
    print 'Player Chooses', comp_number
    print 'Computer Chooses', number_to_name(number)
    print 

    
# test your code
print "These are test outputs"
print ""
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

print "to play simply enter rpsls('name') where name is the choice and press return"


