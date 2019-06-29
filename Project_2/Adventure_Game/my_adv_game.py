import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("The doors of the castle close behind you.")
    print_pause("A blinding light fills the room as a hideous beast appears.")
    monster_list = ['Goblin King', 'Dragon', 'Horse Demon']
    monster = random.choice(monster_list)
    time.sleep(2)
    print("Oh no! It's a", monster)
    time.sleep(2)


def fight_or_flee():
    print_pause("You spot the treasure behind the beast.")
    print_pause("Your grip tightens on the Sword of Wrath,")
    print_pause("but the wound on your leg throbs with pain"
                " as blood pools around your feet.")
    print_pause("Enter 1 to fight the beast.")
    print_pause("Enter 2 to back away slowly.")
    choice = input("1. Fight\n"
                   "2. Flee\n")
    if choice == '1':
        print_pause("You lift the sword and plunge it into"
                    " the heart of the beast.")
        print_pause("The beast emits a piercing scream and turns to dust.")
        treasure()
        time.sleep(2)
        winner()
    elif choice == '2':
        print_pause("As you step backwards, you feel"
                    " a trap door open beneath you")
        print_pause("and you descend into a pit of snakes.")
        snake_pit()
        time.sleep(2)
        game_over()
    else:
        print_pause("Fool! Enter 1 or 2.")
        fight_or_flee()


def treasure():
    print_pause("You advance towards the glittering treasure.")
    loot_list = ['gold', 'rubies', 'chocolate bars', 'magical potions']
    loot = random.choice(loot_list)
    time.sleep(2)
    print("The chest is filled with", loot)
    time.sleep(2)


def snake_pit():
    print_pause("The snakes coil around you.")
    print_pause("You are now the King of the Snakes")
    print_pause("and are doomed to rule the snake pit for all eternity.")


def play_again():
    print_pause("Would you like to play again? y or n?")
    response = input("y\n"
                     "n\n")
    if response == "y":
        play_game()
    elif response == "n":
        quit()
    else:
        print_pause("Fool! Enter y or n")
        game_over()


def game_over():
    print_pause("GAME OVER")


def winner():
    print_pause("CONGRATULATIONS!")
    print_pause("You have saved the kingdom from the beast, ")
    print_pause("and restored the treasure to the people.")


def play_game():
    intro()
    fight_or_flee()
    play_again()


play_game()

