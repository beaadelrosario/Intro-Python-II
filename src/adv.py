from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together using dot notation

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

### Notes - to make the game run ###
# My game starts with a welcome message, and explanation of the scenario, and asks what their player name is. 
# Then, It will run the functions I've written. 
# After the game, it will ask if you want to play again. If yes, run the functions again. If no, it will exit the game.

### Defining my functions ###

# Make a new player object that is currently in the 'outside' room.
# def start_game():
#     player_name = input("Choose your username: \n")
#     greet_user(player_name)
#     player = Player(player_name, room["outside"])

def greet_user(name):
    while True:
        if len(name) >0:
            greeting = f"\n Hello {name}! Let's begin the adventure. Navigate to different rooms to find the hidden treasure. Good luck!\n"
            print(greeting)
        else:
            print("Please provide a username.")
            name = input("Type your name: \n")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
