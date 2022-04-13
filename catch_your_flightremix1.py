import time
import random
import math


def reset_globals():
    global time_left
    global pocket_contents
    global weather
    global bag
    global is_sleepy
    global pass_hiding_spots
    global passport_location
    pocket_contents = random.choice(["nothing", "knife", "granola"])
    bag = [pocket_contents]
    weather = ""
    weather = random.choice(["raining", "sunny"])
    player_name = "Unknown Player"
    is_sleepy = True
    stay_awake = True
    pass_hiding_spots = ["drawer", "closet", "freezer"]
    passport_location = random.choice(pass_hiding_spots)
    time_left = 120


def pause(slow_message):
    print(slow_message)
    time.sleep(3)


def no_time():
    pause("There is no time for this!!!")


def valid_input(prompt, options):
    choice = input(prompt).lower()
    if choice in options:
        return choice
    else:
        pause("Sorry, I don't understand")
        valid_input(prompt, options)


def play_again():
    try_again = valid_input("Would you like to try again tomorrow?\n"
                            "Please select yes or no\n", ["yes", "no"])
    while try_again == "no":
        pause("Thank you for playing Catch Your Flight!")
        exit()
    else:
        pause("Safe Travels!")
        make_your_flight()


def missed_flight():
    pause("Unfortunately today is not your day")
    pause("You have missed your flight!")
    pause("Sorry! You ran out of time...")
    pause("Your flight left " + str(abs(time_left)) + " minutes ago")


def lost_minutes(reduce_time):
    global time_left
    time_left -= reduce_time
    if time_left < 0:
        missed_flight()
        play_again()
    else:
        pause("You have " + str(time_left) + " minutes to make your "
              "flight\n")
        return time_left


def good_weather():
    global weather
    weather = random.choice(["raining", "sunny"])
    if weather == "sunny":
        return True
    else:
        return False


def get_player_name():
    global player_name
    player_name = str(input("Please enter your name\n"))


def intro():
    pause("Welcome to Catch Your Flight! " + player_name + "!")
    pause("Please answer all questions with yes and no."
          " Unless otherwise indicated.")
    pause("Today you are taking the trip of a lifetime!")
    pause("It is currently " + weather + " outside")
    pause("You have " + str(time_left) + " minutes to make it to your flight")


def snooze():
    global is_sleepy
    pause("BEEP! BEEP!")
    pause("The loud alarm wakes up " + player_name)
    pause(player_name + " has plenty of time before the flight")
    hit_snooze = valid_input("Do you want to hit the snooze "
                             "button?\n", ["yes", "no"])
    if hit_snooze == "yes":
        pause(player_name + " hits the snooze button\n")
        time.sleep(4)
        pause(player_name + " wakes up")
        pause("That was refreshing")
        pause("Too refreshing...")
        pause(player_name + " checks the time")
        pause("OH NOOOOO! You overslept!!!!!!!")
        lost_minutes(45)
        is_sleepy = False
    else:
        pause("No time to waste")
        pause("Time to start the day")
        pause("You are still tired")
        is_sleepy = True


def coffee_pot():
    coffee_choice = valid_input("Would you like to make a cup of"
                                " coffee?\n", ["yes", "no"])
    if coffee_choice == "yes":
        pause("Oh yeah! That hit the spot! " + player_name + " feels more"
              " energized than ever!")
        lost_minutes(5)
        global is_sleepy
        is_sleepy = False
    elif coffee_choice == "no":
        no_time()
    else:
        pause("figure it out")


def pass_check():
    global passport_location
    pause("Where could the passport be?")
    pass_finder = valid_input("Where do you want to search?\n"
                              "1. Desk Drawer\n"
                              "2. Bottom of the Closet\n"
                              "3. Back of the Freezer\n", ["1", "2", "3"])

    pass_index = int(pass_finder) - 1
    if pass_hiding_spots[pass_index] == passport_location:
        pause("You found it!")
        bag.append("passport")
        pause("You have added your passport to your bag\n")
        lost_minutes(5)

    else:
        pause("It's not there! I have to keep looking")
        no_time()
        lost_minutes(5)
        pass_check()


def double_check():
    pause(player_name + " feels like they are still missing something\n")
    pocket_check = valid_input("Would you like to check your bag"
                               " one more time?\n", ["yes", "no"])
    if pocket_check == "yes":
        pause("You have found " + pocket_contents + " in your bag's pockets")
        empty_pockets = input("Would you like to empty your bag's pockets?\n")
        if empty_pockets == "yes":
            bag.remove(pocket_contents)
            lost_minutes(3)
        else:
            no_time()
            pause("You keep everything in your pockets")
    else:
        no_time()
    pause("Okay its time to go")


def check_bag():
    bag_check = valid_input("Would you like to double check your"
                            " bag?\n", ["yes", "no"])
    if bag_check == "yes":
        pause("Oh no! Your passport is missing!")
        lost_minutes(5)
        pass_check()
        double_check()
    else:
        no_time()


def check_in(bag):
    global fail_check_in
    pause("It takes 25 minutes to get to the airport")
    lost_minutes(25)
    pause("You have finally reached check-in!")
    pause("The agent looks at you")
    pause("Passport please")
    pause(player_name + " checks their bag...")
    if "passport" in bag:
        pause("Got it!")
        pause("You eagerly hand over your passport")
        pause("Thank you!")
        time.sleep(3)
        pause("Check-in complete! Next stop...")
        pause("Security!")
        lost_minutes(15)
        fail_check_in = False
    else:
        time.sleep(3)
        pause("No way!")
        lost_minutes(2)
        pause("It has to be here somewhere")
        lost_minutes(5)
        pause("Unbelievable!")
        pause(player_name + " forgot their passport at home!")
        fail_check_in = True


def security_check(bag):
    global fail_tsa
    pause(player_name + " arrives at security")
    pause("The carry-on bag is placed on the belt")
    pause("The TSA agent's eyes widen")
    pause("He yells...")
    pause("I need some help over here!!!!")
    pause("The agent pulls the bag from the belt")
    pause("He looks in the pockets...")
    time.sleep(2)
    if "knife" in bag:
        pause("The TSA agent pulls out a large pocket knife with"
              " the name: " + player_name + " etched on the side!")
        pause(player_name + " is tackled to the floor")
        pause("As " + player_name + " is dragged away. It is clear"
              " no flight is being made today...  ")
        fail_tsa = True

    else:
        pause("False alarm")
        pause(player_name + " has made it past security!")
        lost_minutes(10)
        fail_tsa = False


def coffee_shop():
    pause("The most wonderful nutty aroma fills your nostrils.")
    drink_shop = valid_input("Grab a cup?\n"
                             "yes or no\n", ["yes", "no"])
    if drink_shop == "yes":
        global is_sleepy
        pause("That may be the best cup of coffee " + player_name + " has "
              "ever had!")
        is_sleepy = False
        lost_minutes(12)
    else:
        no_time()


def asleep(bag):
    global is_sleepy
    global stay_awake
    pause("This is it! Almost there!")
    if is_sleepy is True:
        pause("Suddenly your eyes get start getting heavy")
        pause("Too tired. Let's check the bag to see "
              "if you have anything to help")
        if "granola" in bag:
            pause("Woohoo there is an granola bar in the bag's pocket!")
            pause("Just enough for a quick burst of energy")
            is_sleepy is False
            stay_awake = True
            lost_minutes(2)
        else:
            pause("Nothing here")
            pause(player_name + " falls asleep at the gate!")
            stay_awake = False
    else:
        pause("You have arrived at the gate!!!!!!")
        made_flight()


def made_flight():
    if time_left > 0:
        pause("Congratulations!!!!")
        pause("You made your flight!!!")
        play_again()
    else:
        missed_flight()
        play_again()


def make_your_flight():
    reset_globals()
    global time_left
    global stay_awake
    good_weather()
    while time_left > 0:
        while True:
            reset_globals()
            get_player_name()
            intro()
            snooze()
            coffee_pot()
            check_bag()
            check_in(bag)
            if fail_check_in is True:
                play_again()
                break
            security_check(bag)
            if fail_tsa is True:
                play_again()
                break
            else:
                coffee_shop()
                asleep(bag)
                if stay_awake is True:
                    made_flight()
                else:
                    missed_flight()
                    play_again()
        break
    else:
        missed_flight()
        play_again()


make_your_flight()
