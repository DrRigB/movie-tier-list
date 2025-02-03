import random

# Starting attributes
name = ""
weapon = ""
health = random.randint(7,10) * 10
gold = 0
strength = random.randint(12,17)
level = 1


'''
HELPER STRINGS -- Feel free to copy these lines to aid in your printouts:


A monster is attacking you!
Enter:  '1' to use your ___
        '2' to run away
Choice: ___
You defeated the monster and found ___!
That was rough! You lost ___ health.
Luckily you managed to get past the monster!
Press Enter to continue
___ gold
a health potion. You restored ___ health
Hello, ___
In this dungeon, you will fight three monsters.
If you survive to the end, treasure awaits!
You have your trusty ___, I see.
Good. You will need it.
Press Enter when you are ready to begin...
You made it to the treasure! You found ___ gold!
You didn't find the treasure, but you survived to fight again another day...
You fought as best you could, but didn't make it. 
The treasure waits for the next adventurer...
'''

# Write your functions here
def display_character():
   print(f"Character name: {name}, Level: {level}")
   print(f"Weapon: {weapon}, Gold: {gold}")
   print(f"Health: {health}, Strength: {strength}")


def found_loot():
    global health, gold
    random_loot = random.randint(1,100)
    gold_found = random.randint(25,150) #gold found for loot
    health_potion = random.randint(1,3)
    #healing potion
    potion = health_potion
    minor_healing = 10
    healing_potion = 20
    great_healing = 30
    restored_health = 0
    
    if health_potion == 1:
        potion = "minor healing"
        restored_health = minor_healing
        health += minor_healing
    
    elif health_potion == 2:
        potion = "healing"
        restored_health = healing_potion
        health += healing_potion
    
    else:
        potion = "greater"
        restored_health = great_healing
        health += great_healing
    
    if random_loot <= 70:
        print(f"You have found {gold_found} Gold")
        gold += gold_found
    else:
        print(f"You have found a {potion} potion")
        print(f"You've restored {restored_health} Health")
   

def encounter():
    
    global weapon, name, health, strength
    monster = random.randint(1,3)
    
    if monster == 1:
        mob = "Goblin"
    
    elif monster == 2:
        mob = "Skeleton"

    else: 
        mob = "Troll"
    while True: 
        print(f"A {mob} aproaches ")
        choice = int(input(f"""
                   1 to use your {weapon},
                   2 to run away"""))
    
        if choice == 1:
            monster_strength = random.randint(10,20)
            print(f"{name} Attacks!")
            if strength >= monster_strength:
                print(f"You've deafeated the {mob}!")
                found_loot()
            
            else:
                health -= monster_strength * 10
                print(f"You've lost {monster_strength * 10} Health")
                if health <= 0:
                    print("You died!")
                    break
            
                else:
                    print("somehow you managed to escape!")
                    input("Press Enter to continue")
            
        elif choice == 2:
            print(f"{name} Runs away to fight another day!")
            break
    
        else:
            print("Error Invalid request!")
        

    
        
        


    

def start_game():
    global name, weapon, health
    print("Welcome to the dungeon!")
    name = input("What is your name, adventurer? ")
    weapon = input("What is your weapon of choice? ")
    display_character()
    
    input(f"""Hello, {name}!
          In this dungeon, you will fight three monsters.
          If you survive to the end treasure awaits!
          You have your trusty {weapon}, I see.
          Good. You will need it.
          Press ENTER when you are ready to begin...""")
    
    for _ in range(3):
        encounter()
        if health <= 0:  # Check if the player is dead after each encounter
            print("You Died.")
            break  # Exit the loop if the player is dead
    



start_game()