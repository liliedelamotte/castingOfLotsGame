# imports random module
import random

# create and initialize constants
# menu choice constants
FIELD_BET = "1"
PASS_BET = "2"
QUIT = "3"
MENU_CHOICES = (FIELD_BET, PASS_BET, QUIT)
DEFAULT_TALENTS = 100

# field bet constants
FIELD_BET_WIN_DOUBLE = (2, 12)
FIELD_BET_WIN_EVEN = (3, 4, 9, 10, 11)
FIELD_BET_LOSE = (5, 6, 7, 8)

# pass bet constants
PASS_BET_WIN_EVEN = (7, 11)
PASS_BET_LOSE = (2, 12)
PASS_BET_LOSE_POINT = (7, 11)


# MODULE: main
# DEF: main algorithm to run casting of lots game
def main():

    displayWelcomeMessage()

    talents = retrieveNumberOfTalentsFromFile()

    menuChoice = receiveMenuChoice(talents)

    while menuChoice != QUIT and talents > 0:

        talents = playGame(talents, menuChoice)

        menuChoice = receiveMenuChoice(talents)

    writeLeftoverTalentsToFile(talents)

    displayExitMessage()


# MODULE: displayWelcomeMessage
# INPUTS: none
# OUTPUTS: none
# DEF: display a welcome message
def displayWelcomeMessage():
    print("Welcome to the Casting of Lots Game!")


# MODULE: receiveMenuChoice
# INPUTS: none
# OUTPUTS: menuChoice
# DEF: ask user if they would like to play a field bet, a pass bet, or quit
def receiveMenuChoice(talents):
    if talents > 0:
        print()
        print("Would you like to make a field bet, a pass bet, or quit?")
        print("Enter '1' for a Field Bet.")
        print("Enter '2' for a Pass Bet.")
        print("Enter '3' to quit.")
        menuChoice = input("What would you like to do? ")
        print()
        while menuChoice not in MENU_CHOICES:
            print("ERROR: That is an invalid input.")
            menuChoice = input("Please enter a '1', a '2', or a '3'. ")
            print()
    else:
        menuChoice = '3'
    return menuChoice


# MODULE: retrieveNumberOfTalentsFromFile
# INPUTS: none
# OUTPUTS: talents
# DEF: open talents.txt file and retrieves number of talents written on file
def retrieveNumberOfTalentsFromFile():
    try:
        file = open("talents.txt", "r")
        talents = int(file.read())
        file.close()
    except:
        talents = DEFAULT_TALENTS
    return talents


# MODULE: castLots
# INPUTS: none
# OUTPUTS: lotsCast
# DEF: two dice are rolled using the random module
def castLots():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print("The lots cast is ", (die1 + die2), ".", sep="")
    return die1 + die2


# MODULE: playGame
# INPUTS: talents, menuChoice
# OUTPUTS: talents
# DEF: main game module, calls both pass bet and field bet functions
def playGame(talents, menuChoice):
    wager = getWager(talents)
    # print("The lots cast is ", lotsCast, ".", sep='')
    if menuChoice == '1':
        talents = playFieldBet(talents, wager)
    else:
        talents = playPassBet(talents, wager)
    return talents


# MODULE: getWager
# INPUTS: talents
# OUTPUTS: wager
# DEF: gets wager from user
def getWager(talents):
    print("You currently have ", talents, " talents.", sep='')
    try:
        wager = int(input("How many talents would you like to wager? "))
        print()
        while wager > talents or wager <= 0:
            print("ERROR: That is an invalid input.")
            wager = int(input("How many talents would you like to wager? "))
            print()
    except ValueError:
        wager = 0
        while wager > talents or wager <= 0:
            try:
                print("ERROR: That is an invalid input.")
                wager = int(input("How many talents would you like to wager? "))
                print()
            except ValueError:
                wager = 0
    return wager


# MODULE: playFieldBet
# INPUTS: lotsCast, talents, wager
# OUTPUTS: talents
# DEF: plays a field bet based off lots cast and talents wagered
def playFieldBet(talents, wager):
    lotsCast = castLots()
    if lotsCast in FIELD_BET_WIN_DOUBLE:
        talents += (wager * 2)
        print("You won double the talents you wagered!")
        printTotalNumberOfTalents(talents)
    elif lotsCast in FIELD_BET_WIN_EVEN:
        talents += wager
        print("You won even the talents you wagered!")
        printTotalNumberOfTalents(talents)
    else:
        talents -= wager
        print("You lost the number of talents you wagered!")
        printTotalNumberOfTalents(talents)
    return talents


# MODULE: playPassBet
# INPUTS: lotsCast, talents, wager
# OUTPUTS: talents
# DEF: plays a pass bet based off lots cast and talents wagered
def playPassBet(talents, wager):
    lotsCast = castLots()
    if lotsCast in PASS_BET_WIN_EVEN:
        talents += wager
        print("You won even talents you wagered!")
        printTotalNumberOfTalents(talents)
    elif lotsCast in PASS_BET_LOSE:
        talents -= wager
        print("You lost the number of talents you wagered!")
        printTotalNumberOfTalents(talents)
    else:
        talents = playPassBetPoint(lotsCast, talents, wager)
    return talents


# MODULE: playPassBetPoint
# INPUTS: lotsCast, talents, wager
# OUTPUTS: talents
# DEF: plays a pass bet when a point number is rolled
def playPassBetPoint(lotsCast, talents, wager):
    point = lotsCast
    print(point, " has become a POINT.", sep="")
    lotsCast = castLots()
    while lotsCast not in PASS_BET_LOSE_POINT and lotsCast != point:
        lotsCast = castLots()
    if lotsCast in PASS_BET_LOSE_POINT:
        talents -= wager
        print("You lost the number of talents you wagered!")
        printTotalNumberOfTalents(talents)
    else:
        talents += wager
        print("You won even the talents you wagered!")
        printTotalNumberOfTalents(talents)
    return talents


# MODULE: printTotalNumberOfTalents
# INPUTS: talents
# OUTPUTS: none
# DEF: prints number of talents and never prints negative talents
def printTotalNumberOfTalents(talents):
    if talents > 0:
        print("You currently have ", talents, " talents.", sep='')
    else:
        print("You currently have 0 talents.")


# MODULE: writeLeftoverTalentsToFile
# INPUTS: talents
# OUTPUTS: none
# DEF: writes number of leftover talents to talents.txt file
def writeLeftoverTalentsToFile(talents):
    if talents <= 0:
        talents = DEFAULT_TALENTS
    file = open("talents.txt", "w")
    file.write(str(talents))
    file.close()


# MODULE: displayExitMessage
# INPUTS: none
# OUTPUTS: none
# DEF: displays an exit message
def displayExitMessage():
    print()
    print("Thank you for playing the Casting of Lots game!")


# call main function
main()