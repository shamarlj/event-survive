import random 
print("you have 5 items to surive in a desert for 14 days")
items = ["Water","Food","Med-Kit","Tent","Sword"]
print("here are your items",items)
def menuscreen():
    print("A. Drink from your water bottle.") #
    print("B. eat food.")#
    print("C. use the medkit.")#
    print("D. go to sleep.")#
    print("E. walk around in the desert.")# if usr picks this make a  map system 
    print("F. fight")
    print("G. Status check")
    print("Q. Quit. \n")

refill=15 # if the user drinks a  water bottle make this go down 1
water = 50 # water
food=10 #  if they eat food -1 
medkit = 5 # if the user health  gose down use this for it to go back to 100  and make medkit -1
sleep=0 # if the user fights the snake or coyote make them get tired if triedness = 100 make them go to the tent and sleep   
health=100 # if the player gets hit by the snake or coyote make them lose health coyote 30 snake 25
tent=0 #if the player gose to the tent and forget to close it make it 1 1/10 chance that  somthing will happen 

movement=["left","right","forward","back",]
sentences ={
"you have ran into  a coyote"# plaer willl fight coyoe
"you have ran into a Javelina "#player will figth snake
"there is a sandstorm runnnnnn!!!!"#will take plaer health 
"there is a random un touched water bottle (will you pick it up??)"# add 1 to water 
"there is a random person will u help them (all they neeed is a shelter )"#ask a player for a name of a friend or anyone.
"at night you see a huge cricle thing in the sky with a bring light (will  you go out)"#
"you trip over somthing in the snad (will it be food or water or even a exit)"#food or water 
"a person walk up to you and ask (Which number would give you the victory in a contest of writing the largest number with the conventional rules of the Roman numeral system??.)"#answer MMMDCCCLXXXVIII  is  if they answer it fright they get + 10 food and water + 8          
""
};

sentenctent=[

              ];
