import random

# Global variables
name = ""
medical_supplies = random.randint(50, 100)
energy = random.randint(70, 100)
ewoks_treated = 0

def display_status():
    print(f"Medic: {name}")
    print(f"Medical Supplies: {medical_supplies}")
    print(f"Energy: {energy}")
    print(f"Ewoks Treated: {ewoks_treated}")

def treat_ewok():
    global medical_supplies, energy, ewoks_treated
    injuries = {
        "Minor": {"supplies": 10, "energy": 5},
        "Moderate": {"supplies": 20, "energy": 0},
        "Severe": {"supplies": 30, "energy": -10}
    }
    severity = random.choice(list(injuries.keys()))
    cost = injuries[severity]

    print(f"Ewok has a {severity} injury.")
    if medical_supplies >= cost["supplies"]:
        medical_supplies -= cost["supplies"]
        energy += cost["energy"]
        ewoks_treated += 1
        print(f"Treated successfully! Supplies left: {medical_supplies}, Energy: {energy}")
    else:
        print(f"Not enough supplies to treat a {severity} injury.")

def treat_ewok():
    global medical_supplies, energy, ewoks_treated

    injuries = {
        "Minor": {"supplies": 10, "energy": -5},
        "Moderate": {"supplies": 20, "energy": 0},
        "Severe": {"supplies": 30, "energy": -10}
    }

    severity = random.choice(list(injuries.keys()))
    cost = injuries[severity]

    print(f"Ewok has a {severity} injury.")
    
    # Step 1: Player's Choice to Treat or Not
    choice = input("Do you want to treat this Ewok? (yes/no): ").strip().lower()
    
    if choice == "yes":
        # Step 2: Check Resources and Proceed
        if medical_supplies >= cost["supplies"]:
            medical_supplies -= cost["supplies"]
            energy += cost["energy"]
            ewoks_treated += 1
            print(f"Treated successfully! Supplies left: {medical_supplies}, Energy: {energy}")
        else:
            print(f"Not enough supplies to treat a {severity} injury.")
    elif choice == "no":
        print("You decided not to treat the Ewok.")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

def start_shift():
    global name
    print("Welcome to the forest moon of Endor!")
    name = input("Enter your name, Medic: ")
    print(f"Welcome, Medic {name}. Ewoks are depending on you.")
    input("Press Enter to begin your shift...")

    for _ in range(3):
        if medical_supplies <= 0 or energy <= 0:
            print("You're out of resources! Ending shift early.")
            break
        treat_ewok()
        display_status()
    
    end_shift()

def end_shift():
    print("\nShift Complete!")
    print(f"Ewoks Treated: {ewoks_treated}")
    if medical_supplies > 20:
        print("Great job! You managed your resources well.")
    elif ewoks_treated < 3:
        print("You ran out of resources. Better luck next time!")
    else:
        print("Mission accomplished, but supplies ran low.")
    display_status()

start_shift()
