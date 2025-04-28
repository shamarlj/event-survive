import random 
import time 
print("you have 5 items to surive in a desert for 14 days")
items = ["Water","Food","Med-Kit","Tent","Sword"]
print("here are your items",items)
def menuscreen():
    print("A. Drink from your water bottle.") # prached gose down by all and drinks go down by 1 
    print("B. eat food.")# if they dont eat let health go down by 15
    print("C. use the medkit.")#if they take damage and they use it let it go to 100
    print("D. go to sleep.")#
    print("E. walk around in the desert.")# they pick left or right up or down  and let there be a 1/10 chance they find water 
    print("F. fight")# they can only fight if tehy coyoe or javeline appear
    print("G. Status check")
    print("Q. Quit. \n")

water = 50 # water
food=10 #  if they eat food -1 
medkit = 5 # if the user health  gose down use this for it to go back to 100  and make medkit -1
sleep=0 # if the user fights the snake or coyote make them get tired if triedness = 100 make them go to the tent and sleep   
health=100 # if the player gets hit by the snake or coyote make them lose health coyote 30 snake 25
tent=0 #if the player gose to the tent and forget to close it make it 1 1/10 chance that  somthing will happen 
parched=0 # if they dont drink let this go up if 1/25 they dont drik they lose
movement=["left","right","forward","back",] # make this there a 1/25  chance to find somthing so if i 1/25 somthing will happen or make it where the map is complex 


sentences ={ # when they player is walking this will play out 
"you have ran into  a coyote"# player willl fight coyoe
"you have ran into a Javelina "#player will figth javelina
"there is a sandstorm runnnnnn!!!!"#will take plaer health  -3 every 4 secs
"there is a random un touched water bottle (will you pick it up??)"# add 1 to water 
"there is a random person will u help them (all they neeed is a shelter )"#ask a player for a name of a friend or anyone.#then that input is there name
"at night you see a huge cricle thing in the sky with a bring light (will  you go out)"#yes give user one water plus 4 food if no they get nothing 
"you trip over somthing in the snad (will it be food or water or even a exit)"#food or water let there be a 1/100 chance its a exit 
"a person walk up to you and ask (Which number would give you the victory in a contest of writing the largest number with the conventional rules of the Roman numeral system??.)"#answer MMMDCCCLXXXVIII  is  if they answer it fright they get + 10 food and water + 8          
""
}

import random
import time

print("you have 4 items to survive in a desert for 14 days")
items = ["Water", "Food", "Med-Kit", "Tent"]

def instructionsText():
    print("\n             Welcome to desert surviver!")
    time.sleep(.5)
    print("You have been trapped and need to survive for 14 days")
    time.sleep(.5)
    print("If you win, you will receive a cash prize of 25,000,000$")
    time.sleep(.5)
    print("Make sure to always check your stats.\n")

instructionsText()

print("here are your items food, water, Med-Kit, tent,")

def MenuScreen():
    print("A. Drink from your water bottle.") #
    print("B. Eat food.") #
    print("C. Use the medkit.") #
    print("D. Go to sleep.") #
    print("E. Walk around in the desert.") # if usr picks this, make an event system
    print("F. Fight")
    print("G. Status check")
    print("Q. Quit. \n")

# -------------------------------
# Variables
water = 50 # water
food = 10 # if they eat food, -1
medkit = 5 # if the user health goes down, use this to heal to 100 and subtract -1 medkit
sleep = 0 # if the user fights the snake or coyote, make them get tired. If tiredness = 100, make them go to the tent and sleep.
health = 100 # if the player gets hit by the snake or coyote, make them lose health (coyote: 30, snake: 25)
tent = 0 # if the player goes to the tent and forgets to close it, 1/10 chance something will happen
parched = 0 # if the user doesn't drink, make them thirsty
distance = 0
# -------------------------------

movement = ["left", "right", "forward", "back"]
sentences = {
    "you have ran into a coyote",  # player will fight coyote
    "you have ran into a Javelina",  # player will fight javelina
    "there is a sandstorm runnnnnn!!!!",  # will take player health
    "there is a random untouched water bottle (will you pick it up??)",  # add 1 to water
    "there is a random person. Will you help them (all they need is a shelter)",  # ask a player for a name of a friend or anyone.
    "at night you see a huge circle thing in the sky with a bright light (will you go out)", #
    "you trip over something in the sand (will it be food or water or even an exit)",  # food or water
    "a person walks up to you and asks (Which number would give you the victory in a contest of writing the largest number with the conventional rules of the Roman numeral system??)"  # answer MMMDCCCLXXXVIII; if they answer correctly, get +10 food and water +8
}

Done = False

while  Done == False:
    MenuScreen()
    if sleep >= 0 and sleep < 25:
        print(f"Your tiredness is at", sleep, "/100")
    elif sleep >= 35 and sleep < 50:
        print("You are getting tired???")
    elif sleep >= 55 and sleep <= 90:
        print("Get some sleep right now")
        break

    if sleep >= 100:
        Done = True
        print("You fell asleep in the middle of the desert")
        break

    if health > 50:
        print("There is no need for a med kit")
    elif health <= 50 and health > 25:
        print("You might want to use the med kit")
    elif health <= 25:
        print("Health is low, use a med kit")
       
    if health <= 0:
        print("Your health is 0, you have died")
        break

    choose = input("What will you do? ").strip().lower()
    if choose == "a":
        if water > 0:
            # If true, drink subtracts
            water -= 10
            parched = 0
            print("You drank from your water bottle.")
            print("But your water supply isn't infinite, so  be care full\n")
        elif water == 0:
            print("No more water to drink, you drank it all.")
   
    if choose == "b":
        if food > 0:
            food -= 1
            print(f"You had the best meal of your life! But you only have {food} food items left.")
        elif food <= 0:
            print("You ate all of the food.")
   
    if choose == "c":
        if health > 50:
            print("You don't need the med kit right now, focus!")
        elif health <= 50 and medkit > 0:
            medkit -= 1
            health = 100
            print(f"Health healed to 100. You have {medkit} medkits left.")
        elif medkit <= 0:
            print("No more medkits available.")
           
    if choose == "d":
        user_input = input("Do you want to sleep? (y/n) ").strip().lower()
        if user_input == "y":
            sleep = 0
            print("Good night...")
        elif user_input == "n":
            print("what will you do now?")
   
    if choose == "e":
        direction = input("Left or right? ").strip().lower()
        if direction == "left":
            distance += 25
        if distance == 75:
            choice = input("There is something hidden. Want to pick it? (y/n)").strip().lower()
            if choice == "y":
                water += 50
                print("You resupply your water!")
            elif choice == "n":
                print("You ignored it.")
        else:
            distance += 15
           
    if choose == "f":
        print("not done")
       
    if choose == "f":
        print("not done")
       
    if choose == "q":
        Done = True
        print("you didnt wanna do this anymore")
        time.sleep(.5)
        print("So because of that you went home and asked yourself")
        time.sleep(.5)
        print("")
    break


