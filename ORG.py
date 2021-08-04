'''
This is a chose your adventure story in text form
Usage:
'''
import random
MONEY = 0
INVENTORY = []

def current_balance():
  global MONEY
  print("current balance ${}".format(MONEY))

def yes_no(question):
  '''for all your yes no needs'''
  print("{}\n\t".format(question))
  answer = input()
  return answer

def bal_verify(balance, cost):
  '''Validates the user can not over spend'''

  if balance - cost > 0:
    return True
  else:
    print("you do not have enough money\n{}".format(current_balance()))
    marketplace(balance)

def marketplace():
  '''items to sell'''
  global MONEY
  global INVENTORY


  print("\t\t\t1) Axe-$45\n \
         \t2) Sword-$32\n \
         \t3) Bow-$78\n \
         \t4) Arrowsx10-$20\n \
         \t5) List Inventory\n \
         \t6) Use Inventory\n \
         \t7) Leave Game!\n")
  item = input("Please select an item from the list:\n\t")
  item = int(item)
  if item == 1:
    bal_verify(MONEY,45)
    MONEY-=45
    print("You now have an Axe and your balance is ${}".format(MONEY))
    INVENTORY.append("AXE")
    axe()
  elif item == 2:
    bal_verify(MONEY,32)
    MONEY-=32
    print("You now have a Sword and your balance is ${}".format(MONEY))
    INVENTORY.append("SWORD")
    sword()
  elif item == 3:
    bal_verify(MONEY,78)
    MONEY-=78
    print("You now have a Bow and your balance is ${}".format(MONEY))
    INVENTORY.append("BOW")
    bow()
  elif item == 4:
    bal_verify(MONEY,20)
    MONEY-=20
    print("You now have Arrows and your balance is ${}".format(MONEY))
    for i in range(10):
      INVENTORY.append("ARROWS")
    marketplace()
  elif item == 5:
    print("Number of items in inventory {}\n\t{}".format(len(INVENTORY), INVENTORY))
    marketplace()
  elif item == 6:
    print("Number of items in inventory {}\n\t{}".format(len(INVENTORY), INVENTORY))
    sel_item = input("Which item do you want to use:\n\t")
    if sel_item.upper() == "AXE":
      if ("AXE" in INVENTORY):
        axe()
    if sel_item.upper() == "SWORD":
      sword()
    if sel_item.upper() == "BOW":
      bow()
    else:
      print("unable to use item")
      marketplace()
  elif item == 7:
    exit
  else:
    marketplace()

  return item
def goon_walk(item):
  '''GO ON A WALK OPTIONS'''

  if ("DOG" in INVENTORY):
    marketplace()

  if item.upper() == "AXE":
    walk = input("Would you like to go on a walk?\n\t")
    if ("YES" in walk.upper()):
      walk = input("You found a dog would you like to be friends with it\n\t")
      if ("YES" in walk.upper()):
        mylist =["You Died", "You now have a Dog"]
        pick = (random.choice(mylist))
        if ("DIED" in pick.upper()):
          print("BAD LUCK; YOU DIED!!!")
          exit
        else:
          print("Want to use your axe or go back to the market? (axe/market)\n\t")
          axe_market = input()
          print("Going to {}".format(axe_market))
          if ("AXE" in axe_market.upper()):
            axe()
          else:
            marketplace()

def axe():
  '''all the adventures with an axe'''
  global INVENTORY
  global MONEY
  cut = input("Would you like to cut down a tree?\n\t")
  if ("YES" in cut.upper()):
    print ("You cut down 10 trees")
  sell_house = input("You can either sell your lumber or build a wall for a house (sell/house)\n\t")
  if ("SELL" in sell_house.upper()):
    wood = input("Where do you want to sell your wood\n\
    1) Jeff's Lumber -- $2 a tree\n\
    2) George's Saw Mill -- $5 a tree minus 10 dollars for gas if you have a car\n\t")
    if (wood == "1"):
      MONEY+=20
      print("Jeff gave you $20; Current Balance ${}".format(MONEY))
      goon_walk("axe")
    elif (wood == "2"):
      if "CAR" in INVENTORY:
        print('Selling wood to George')
        MONEY+=50
        print('Buying Gas')
        MONEY-=10
        print('Current Balance: ${}'.format(MONEY))
        goon_walk("axe")
      else:
        print("You do not have a car and must go to Jeff's")
        MONEY+=20
        print("You got $20 from Jeff\nCurrent Balance: ${}".format(MONEY))
        goon_walk("axe")
    else:
      print("Invalid selection\nkeep wood")
      axe()
  elif ("HOUSE" in sell_house.upper()):
    print ("You now have one house wall")
    INVENTORY.append("HOUSE")
    goon_walk("axe")
  print("You found a peice of clothing")
  Bob = input("Would you like your dog to sniff out the person\n\t")
  if ("YES" == Bob.upper()):
    print("Your dog found Bob")
    print("Hello welcome to Bob's Dealership")
    Bob_Dealership = input("Would you like to buy a car for $45\n\t")
    if ("YES" == Bob_Dealership.upper()):
        MONEY-=45
        INVENTORY.append("CAR")
        current_balance()
        marketplace()
    else:
      marketplace()

def sword():
  '''Playing with swords'''
  global MONEY
  sword = input("A person is being attacked would you like to help\n\t")
  if ("YES" in sword.upper()):
    mylist =["You Failed", "You Succeed"]
    pick = (random.choice(mylist))
    if ("FAILED" in pick.upper()):
        print("BAD LUCK; YOU Failed!!!")
        exit
    if ("SUCCEED" in pick.upper()):
        print("The person gives you $10 for your heroic service")
        MONEY+=10
        print("Your current balance is {}".format(MONEY))
  store = input("Would you like to go back to the store\n\t")
  if ("YES" in store.upper()):
    marketplace()
  else:
      quest_pick = input("Do you want to go on a quest\n\t")
      if ("YES" in quest_pick.upper()):
        print("\t 1)The Great Dragon\n\t 2)Gem Theif\n\t 3)Robin Hood Time\n\t")
        quest_pick = input("What is your quest\n\t")
        quest_pick = int(quest_pick)
      if quest_pick == 1:
        print("The book O'l quests reads to findth the Drangon that is Great thy shall first findth a Volcano")
        print("They be two ways to get to the nearest Volcano 1)Do the Dangerous path on a horse which cost $5 to rent 2)Go in a car on the highway which cost $3 for gas\n\t")
        quest = input("Which way\n\t")
        quest = int(quest)
        if (quest == 1):
          MONEY-=5
          print("You rented a horse")
          current_balance()
          print("You found Mark on your trail")
          print("You have two options\n\t 1) You can try to talk to him\n\t 2) you can keep going\n\t")
          quest = input("Choose one\n\t")
          quest = int(quest)
        if (quest == 1):
          mylist =["Mark killed you", "He tells you where Bob's dealership is"]
          pick = (random.choice(mylist))
          if ("MARK KILLED YOU" == pick.upper()):
              print("Bad Luck, Your Dead")
              exit
          if ("HE TELLS YOU WHERE BOB'S DEALERSHIP IS" == pick.upper()):
              print("To find where Bob is you must find a dog")
        if (quest == 2):
          print("You keep going on the trail")
          print("There is a fork in the road\n\t 1) You go straight\n\t 2) You go left\n\t 3) You go right\n\t")
          quest_fork = input("Choose which way to go\n\t")
          quest_fork = int(quest_fork)
          if (quest_fork == 1):
            print("There is a Knight in your way\n\t")
            print("Would you like to 1) try to kill him\n\t or 2) return to the marketplace\n\t")
            quest_fork = input("Choose your fate\n\t")
            quest_fork = int(quest_fork)

            if (quest_fork == 1):
              mylist =["He killed you", "You killed him you can now face the dragon","You killed him you can now face the dragon"]
              pick = (random.choice(mylist))
              if ("HE KILLED YOU" == pick.upper()):
                print("He killed you")
                exit
              if ("YOU KILLED HIM YOU CAN NOW FACE THE DRAGON" == pick.upper()):
                print("You killed the Knight")
                mylist =["You died", "You have killed the dragon and claimed the $100 bounty","You have killed the dragon and claimed the $100 bounty"]
                pick = (random.choice(mylist))
                if ("YOU DIED" == pick.upper()):
                    print("You Died")
                    exit
                if ("YOU HAVE KILLED THE DRAGON AND CLAIMED THE $100 BOUNTY" == pick.upper()):
                    MONEY+=100
            if (quest_fork == 2):
                marketplace()

          elif (quest_fork == 2):
              print("You are going left")
              print("There is a block in your way")
              quest_fork = input("Would you like to try to move it\n\t")
              if ("YES" in quest_fork.upper()):
                  mylist =["The block crushes you", "You found the dragon","You found the dragon"]
                  pick = (random.choice(mylist))
                  if ("THE BLOCK CRUSHES" == pick.upper()):
                      print("RIP")
                      exit
                  if ("YOU FOUND THE DRAGON" == pick.upper()):
                      quest_fork = input("Would you like to kill the Dragon\n\t")
                      if ("YES" == quest_fork.upper()):
                          mylist =["You killed the dragon", "You Died", "You killed the dragon"]
                          pick = (random.choice(mylist))
                          if ("YOU DIED" == pick.upper()):
                              print("You Died")
                              exit
                          if ("YOU KILLED THE DRAGON" == pick.upper()):
                              print("You Beat The Quest")
                              MONEY+=100
                              current_balance()


          elif (quest_fork == 3):
              print("You're going right")
              print("Your horse is scared by an earthquake and runs wild")
              quest_fork = input("Whould you like to try to calm it\n\t")
              if ("YES" in quest_fork.upper()):
                  print("He flinged you off and you fell of a cliff")
                  exit
              else:
                    print("He took you back to the marketplace")
                    marketplace()

      if quest_pick == 2:
         print("Mr.Robert Her of Her Jewels is losing money buying the Jewels to make Jewelery so he wants you to go steal them from Hanks Jewels and People's homes")
         quest_2 = input("1) Hanks Jewels\n\t 2) Random People\n\t")
         quest_2 = int(quest_2)
         if (quest_2 == 1):
             print("To get to Hanks Jewels undetected you need to take a taxi")
             MONEY-=7
             current_balance()
             print("Hank is leaving the store now is the time to rob him")
             Hank_quest = int(input("1) Break the window\n\t 2) Buy picklock supplies(minus $20)\n\t"))
             if (Hank_quest == 1):
                 print("You broke the window")
                 mylist = ["The alarm goes off you're arrested", "THe alarm doesn't go off"]
                 pick = (random.choice(mylist))
                 if ("THE ALARM GOES OFF YOU'RE ARRESTED" == pick.upper()):
                      print("Jail Time")
                      exit
                 if ("THE ALARM DOESN'T GO OFF" == pick.upper()):
                      print("You got gems for Robert Her")
                      print("You take a taxi back")
                      MONEY-=7
                      current_balance()
                      print("Thank You for the Gems")
                      print("You Beat the Quest")
                      MONEY+=200
                      current_balance()
                      marketplace()
             if (Hank_quest == 2):
              MONEY-=20
              current_balance()
              print("You got the gems")
              print("Robert Gives you Money")
              MONEY+=155
              current_balance()
              marketplace()
         if (quest_2 == 2):
            print("At night you sneak into Mark's house")
            mylist=["Mark kills you","Mark's dog kills you"]
            pick =(random.choice(mylist))
            if ("MARK KILLS YOU" == pick.upper()):
              print("You Dead")
              exit
            if ("MARK'S DOG KILLS YOU" == pick.upper()):
              print("You Dead")
              exit
      if (quest_pick == 3):
            print("The Rich are to Rich and the Poor are to Poor you need to even it out")
            print("1) Rob king Matthew\n\t 2) Rob king Dude\n\t")
            robin_hood = input("Who do you want to rob\n\t")
            robin_hood = int(robin_hood)
            if (robin_hood == 1):
                print("You hire a taxi")
                MONEY-=8
                current_balance()
                print("You are heading to Castle Matthew")
                print ("You have two options 1) Rob things from his room\n\t 2) Buy a bomb and blow up his safe")
                matthew = input("Choose your robber tactic\n\t")
                matthew = int(matthew)
                if (matthew == 1):
                    print("King Matthew is sleeping in there, you have to be very quiet")
                    mylist =["Matthew wakes up and calls security","You steal all of his valuable items"]
                    pick = (random.choice(mylist))
                    if ("MATTHEW WAKES UP AND CALLS SECURITY" == pick):
                        print("King Matthew Called the Police on You")
                        exit
                    if ("YOU STEAL ALL OF HIS VALUABLE ITEMS" == pick):
                        print("You stole everythinig and returned to the poor people")
                        MONEY+=75
                        current_balance()
                if (matthew == 2):
                    MONEY-=7
                    current_balance()
                    print("You blew up his safe and stole all the money")
                    print("1) Do the noble thing and give the money to the poor people\n\t 2) KEEP THE MONEY\n\t")
                    quest_3 = input("Choose Wisely\n\t")
                    quest_3 = int(quest_3)
                    if (quest_3 == 1):
                        print("You beat the quest")
                        MONEY+=90
                        current_balance()
                        marketplace()
                    if (quest_3 == 2):
                        print("You Suck")
                        exit
            if (robin_hood == 2):
                print("You take a horse to King Dude's Castle")
                MONEY-=5
                current_balance()
                print("King Dude is drunk and will let you take anything")
                print("You take everything back to the poor people, like the good soul you are")
                MONEY+=25
                current_balance()
                marketplace()


def bow():
  '''Lets Shoot Stuff'''
  global MONEY
  if ("ARROWS" in INVENTORY):
    Bow = input("Would you like to go hunting\n\t")
    if ("YES" == Bow.upper()):
      print("You find a deer")
      hunt = input("Would you like to shoot the deer\n\t")
      if ("YES" == hunt.upper()):
          INVENTORY.remove("ARROWS")
          mylist =["You got Deer meat and Deer hide","You Missed"]
          pick =(random.choice(mylist))
          if ("YOU GOT DEER MEAT AND DEER HIDE" == pick):
              print("YOU KILLED A DEER!")
              meat = input("Would you like to sell the meat")
              if ("YES" == meat.upper()):
                  mylist("You got $10", "You got $5","You got $15")
                  pick_2 = (random.choice(mylist))
                  if ("YOU GOT $10" == pick_2):
                      print("You Got $10 For The Meat")
                      MONEY+=10
                      current_balance()
                      cabin = input("You found a cabin in the woods would you like to enter\n\t")
                      if ("YES" == cabin.upper()):
                          print("Hello i'm Joe")
                          cabin = input("Would you like to see me your Deer hide")
                          if ("YES" == cabin.upper()):
                              print("He bought the deer hide for $6")
                              MONEY+=6
                              current_balance()
                          else:
                            marketplace()
                  if ("YOU GOT $5" == pick_2):
                      print("You Got $5 For The Meat")
                      MONEY+=5
                      current_balance()
                      cabin = input("You found a cabin in the woods would you like to enter\n\t")
                      if ("YES" == cabin.upper()):
                          print("Hello i'm Joe")
                          cabin = input("Would you like to see me your Deer hide")
                          if ("YES" == cabin.upper()):
                              print("He bought the deer hide for $6")
                              MONEY+=6
                              current_balance()
                          else:
                            marketplace()
                  if ("YOU GOT $15" == pick_2):
                      print("You Got $15 For The Meat")
                      MONEY+=15
                      current_balance()
                      cabin = input("You found a cabin in the woods would you like to enter\n\t")
                      if ("YES" == cabin.upper()):
                          print("Hello i'm Joe")
                          cabin = input("Would you like to see me your Deer hide")
                          if ("YES" == cabin.upper()):
                              print("He bought the deer hide for $6")
                              MONEY+=6
                              current_balance()
                          else:
                            marketplace()

print("Hello Person")
name = yes_no("WHAT IS NAME")
if (name == "Kegan"):
    print("Cool")
if (name == "Keagan"):
    print("Stupid")
if (name == "Matthew"):
    print("Go away")
if (name == "Matthew"):
  print("HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAAAAAAAAAAAAAAAAAAAAAAA")
while (name == "Kegan"):
    print("Awesome")
    name = input("WHAT IS Question ")
    if (name == "Is Matthew Cool"):
        print("No")
    if (name == "2+2"):
        print("54363564634643616136")

variable1=True
while variable1==True:
  play = input ("WOULD YOU LIKE TO PLAY A GAME????\n\t")
  if ("YES" in play.upper()):
    print("You Got Mail")
    variable1=False

mail = input("Open OR not Open\n\t")
if ("OPEN" in mail.upper()):
  MONEY+=50
  print("You got ${} and a branch".format(MONEY))
else:
   marketplace()
market = input("Would you like to buy something\n\t")
if ("YES" in market.upper()):
  item = marketplace()
