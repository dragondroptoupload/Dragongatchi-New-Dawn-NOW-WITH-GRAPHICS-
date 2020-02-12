import time
import math
import random
import sys
import pygame


RESOURCES =sd12.ext.resources(__file__, "resources")
#import pickle

#by: Lodelcorp


#the item area. stores the funtions for the items
def DragonTreat():
  global PetMood
  global PetName
  print ((str(PetName) + " devours the treat happily, improving their mood!"))
  PetMood += 5
  Inventory.remove("Dragon Treat")

def ScalePolish():
  global PetMood
  global PetName
  print ("working on this atm")
  Inventory.remove("Scale Polish")
#what should this do?


def CoolSunglasses():
  print ("this should do something, eventually.")
  Inventory.remove("Cool Sunglasses")
#equippable? idk.

#the Data area (Stores species info, etc)
SpeciesArt = ["You have chosen the noble Western dragon. This breed is the most well known dragon breed. Its four-legged, winged figure is instantly recognizable to all.", "You Chose to go with the Eastern Dragon. This particular breed of dragon dates back to the ancient days of asia, usually depicted as being a god, or an extremely wise being.", "You picked a Wyvern! This breed of dragon can be tempermental, so watch out! Walking on two legs and sporting two powerful wings, along with a poisonous tail barb like a scorpion, this breed is definitely imposing to look at!", "You Chose a Drake! this breed may look similar to a western dragon, but their main difference is that they lack wings. to compensate, Drakes have a much stronger body build. Dragons may be fearsome in the air, but a Drake on the ground is a speedy sight to behold!"]
#random events for area 1, plus the EvntPetName variable

EvntPetName =["first"]

RandEventA1 = ["You run into another Dragon Tamer at the park. He mentions that his Western Dragon has an odd taste in food for its breed, regarding its love for seafood", "You run about for a while with your dragon, before getting tired and heading home","You play catch with your dragon for a while, before heading home. your dragon thanks you for taking them to the park", "Its raining outside, so you and your dragon spend the day inside watching TV. a sitcom comes on, called ""Drake and Josh, about a teenager getting into wacky situations with his pet Drake, aptly named ""Drake"" Josh is holding a spherical device, and going on about it. Drake just seems confused.", "you find a small obelisk in the bushes after chasing a wayward ball into them. brushing leaves off of it, you find a plaque with an engraving of an upside down finger circle, under it, it reads ''Gotcha''. you arent sure what this means, but feel like youve just been got good.", "You chill at the park for a while with your dragon, before heading home"]
#change the drake and josh one. dead meme you idiot.

#battle arena opponents
class Foe():
  def __init__(self,fl,ll,name):
    self.FoeLevel = fl
    self.FoeLeagueLevel = ll
    self.FoeName = name
FirstFoe = Foe(1,1,"Red")
SecondFoe = Foe(2,2,"edward")


#the pet area (stores/will store all the info on the pet) (except name and species, as those are chosen by the player.)
PetNameSav = "buggy"
PetSpec = "If you're seeing this, its a bug"
PetGender = "should be either male or female, if this prints, its a bug."
Hungry = True
PetLevel = 1
PetAge = 0
LeagueLevel = 1
Money = 50
Inventory = []
PetMood = 10

#the function area. stores functions.
def RandEncounterA1():
  EncNum = random.randint(0,5)
  #print (str(EncNum))
  print (RandEventA1[EncNum])

def FightScript():
  #gonna use a simple rock paper scissors script for now
  global LeagueLevel
  from random import randint
  Strats = ["Attack","Defend","Magic"]
  FoeMove = Strats[randint(0,2)]
  Player = False
  
  while Player == False:
    Player = input("Attack, Defend, or Magic?")
    if Player == FoeMove:
      print ("Your dragon's attacks negate each other. try again.")
      Player = False
    elif Player == "Attack":
      if FoeMove == "Defend":
        print ("Your foe's dragon blocks the attack, before delivering a devastating counter attack. your dragon is knocked out.")
        Player = True
      else:
        print ("your dragon deftly dodges the opponent's magical blast, and lands its attack, knocking their opponent out.")
        LeagueLevel = LeagueLevel + 1
        Player = True
    elif Player == "Defend":
        if FoeMove == "Magic":
          print ("your dragon prepares to block a physical attack, only to be met by a magical blast, and is knocked out.")
          Player = True
        else:
          print ("Your dragon blocks the foe's physical assault, before countering with their own while their opponent is off balance, knocking them out")
          LeagueLevel = LeagueLevel + 1
          Player = True
    elif Player == "Magic":
        if FoeMove == "Defend":
          print ("the opponent blocks, prompting your dragon to break through with a magical blast. the foe does not expect this, and is knocked out")
          LeagueLevel = LeagueLevel + 1
          Player = True
        else:
            print ("your dragon casts a magical blast, but their opponent dodges it, and connects a physical attack, knocking your dragon out.")
            Player = True
    else:
        print ("thats not a valid strat! retype!")
        Player = False

def LeagueStart(Foe,Player):
  global LeagueLevel
  if LeagueLevel == FirstFoe.FoeLeagueLevel:
    print ("Your first foe is Red! This mysterious tamer never speaks, only seems to gaze into your soul. He gestures twoards the field and his dragon runs onto it. His dragon is an orange Western Dragon, atttuned to fire. Sending " + (str(PetName)) + " onto the field, you prepare to battle!")
    FightScript()
  elif LeagueLevel == SecondFoe.FoeLeagueLevel:
    print ("works!")
    FightScript()

#this is where all the running code is.
#gonna just pad this out with this, so its easier for me to Find 
#        . 
#   .>   )\;`a__
#  (  _ _)/ /-." ~~
#  `( )_ )/
#   <_  <_ 

#cool little opening
print ("intinalizing")
print ("Loading...")

time.sleep(1)

print ("Loading....")

time.sleep(1)

print ("done")

time.sleep(1)

print ("welcome to Dragongatchi! please choose a species to raise! Dont worry, dragons here only grow to be around the height of an average human, at most!")
time.sleep(1)
print ("            ")
print ("            ")
#these print blank spaces so that it looks a bit nicer, more spaced out so it isnt a wall of text.
DragonSpeciesCorrect = False

if DragonSpeciesCorrect == False:
  print ("The possible species are: Western Dragon, Eastern Dragon, Wyvern or Drake! Selections are case sensitive")
  time.sleep(.5)
  print ("please type your selection!")
#Dragon's species is stored here.

PetSpecies = input()
if PetSpecies == "Western Dragon":
  print (SpeciesArt[0])
  PetSpec = "Western Dragon"
  DragonSpeciesCorrect = True
elif PetSpecies == "Eastern Dragon":
  PetSpec = "Eastern Dragon"
  print (SpeciesArt[1])
  DragonSpeciesCorrect = True
elif PetSpecies == "Wyvern":
  PetSpec = "Wyvern "
  print (SpeciesArt[2])
  DragonSpeciesCorrect = True
elif PetSpecies == "Drake":
  PetSpec = "Drake"
  print (SpeciesArt[3])
  DragonSpeciesCorrect = True
else:
  print ("Thats not a valid selection, try again!")  
#make it so that any other choices cause a message to appear and it to loop 

OpeningContinue = False
PetGenderSelection = "placeholder"

if DragonSpeciesCorrect == True:
  print ("please name your Dragon!")
  PetName = input()
  PetNameSav = PetName
  OpeningContinue = True

if OpeningContinue:
  print("OK, is " + (str(PetNameSav)) + " Male, or Female?")
  PetGenderSelection = input()
  PetGender = PetGenderSelection

ans = True

while ans:
          print ("make a selection! use the numbers to choose an option.")
          print("""
          1. feed
          2. train
          3. """ + (str(PetName)) + 
          """
          4. Inventory
          5. Check stats
          6. battle (WIP)
          7. Head out!
          """)
          Selection = input()
         
          #this is the feed option
          if Selection == "1":
            if Hungry == True:
              Hungry = False
              print(str(PetName) + " is fed!")
            elif Hungry == False:
              print (str(PetName) + " isnt Hungry!")
         
          #this is the train option
          elif Selection == "2":
              PetLevel = PetLevel + 1
              print (str(PetName) + " trains really hard!")
              print (PetLevel)
         
          #this is the dragon option
          elif Selection == "3": 
               print("What would you like to do with " + (str(PetName)) + "?")
               print ("""
               1. Pet
               2. Talk
               3. Play""")
               DragonMenuSelect = input()
               if DragonMenuSelect == "1":
                 print ("You pet " + (str(PetName) + " for a while, they love it!"))
               if DragonMenuSelect ==  "2":
                 print ("add a random dialouge function later.")
               if DragonMenuSelect == "3":
                 print ("add play dialouge later")
         
         #this is the Inventory option
          elif Selection == "4":
                print("what would you like to use?")
                print (Inventory)
                InventorySelection = input()
                for InventorySelection in Inventory:
                  if InventorySelection == "Dragon Treat":
                    DragonTreat()
                  if InventorySelection == "Scale Polish":
                    ScalePolish()
                  if InventorySelection == "Cool Sunglasses":
                    CoolSunglasses()
          
          
          #check stats option.
          elif Selection == "5":
            print ("Name: " + (str(PetNameSav)))
            print ("Species: " + (str(PetSpec)))
            print ("Gender: " + (str(PetGender)))
            print ("Pet Level: " + (str(PetLevel)))
            print ("Age: " + (str(PetAge)))
            print ("League level: " + (str(LeagueLevel)))
            #print ("Inventory: " + (Inventory))
            print ("Money: " + (str(Money)))
            print ()
            

          #this leads to the battle menu. may be constituted into a "head out" menu later.
          elif Selection == "6":
            print ("welcome to the battle arena! here you can pit your Dragon against other Dragons! its a morally grey area, but dont worry, your Dragon wont die!")
            print ("battle arena is a work in progress. please pardon the dust.")
            print ("""so, what would you like to do?
            1. find opponent
            2. check Dragon stats
            3. how to fight
            4. return to main menu""")
            BattleSelection = input()
            if BattleSelection == "1":
              print ("WIP, may break.")
              print ("would you like to start a league battle? Y/N")
              BattleYN = input()
              if BattleYN == "Y":
                  LeagueStart(FirstFoe.FoeLeagueLevel,LeagueLevel)
                  print ("this should quit back to menu.")
            if BattleSelection == "2":
              print ("this is not fully implemented.")
              print ("League Level: " + (str(LeagueLevel)))
            if BattleSelection == "3":
              print ("welcome to the battle tutorial. this is subject to change, but as it is right now, the battle system is just rock paper scissors. attack is rock, defend is paper, and magic is scissors! good luck!")
            if BattleSelection == "4":
              print ("returning to main menu.")
          
          
          
          
          #this is the "head out" option. 

          elif Selection == "7":
            print ("""where would you like to go?
            1. the park
            2. under construction
            3. the mall
            4. Testing zone""")
            OutSelection = input()
            
            if OutSelection == "1":
              RandEncounterA1()
              time.sleep(1)
            if OutSelection == "2":
              print ("A guard stops you as you try to walk by. ""halt! this section is under construction!"" he says. you look at " + (str(PetName)) + ", who shrugs. you head back home." )
            if OutSelection =="3":
              print ("you decide to do some shopping, and approach a store, noticing a sign saying the area is zoned for a new mall to be built.")
              print ("you enter, and the shopkeeper greets you. ""hello there! care to browse my wares?""" "he says.")
              print ("your money: " + (str(Money)))
              print ("""Shopkeeper's wares:
              1. Dragon Treat - 10 
              2. Scale Polish - 10
              3. Cool Sunglasses - 20
              4. Leave""")
              ShopSelection = input()
              if ShopSelection == "1":
               Inventory.append ("Dragon Treat")
               print ("you exchange 10 gold for the Dragon Treat")
               Money -= 10
              if ShopSelection == "2":
                Inventory.append ("Scale Polish")
                print ("you exchange 10 gold for the Scale Polish")
                Money -= 10
              if ShopSelection == "3": 
                Inventory.append ("Cool Sunglasses")
                print ("you exchange 20 gold for the Cool Sunglasses")
                Money -= 20
              if ShopSelection == "4":
                print ("the shopkeeper bids you farwell")
              else:
                print ("not valid.")

            if OutSelection =="3":
              print ("You step into the testing zone, welcome. what would you like to test?")
              print("""1.graphics test
              2.
              3.""")
              TestAreaSelect = input()
              if TestAreaSelect == "1":
