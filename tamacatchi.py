print("Welcome to the Tamacatchi Game!")
print("")

pet = {"name": "", "type": "", "age": 0, "hunger": 0, "sleepiness": 0, "attributes": []}

petAttributes = {"banana cat": ["crying", "love", "friends"],
           "huh cat": ["confusion", "weird hairline", "chunkiness"],
           "happy cat": ["dancing", "happiness", "friends"],
           "sad cat": ["tears", "loneliness", "crying"],
           "crunchy cat": ["rocks", "nomnoms", "weirdness"]}

def cat():
    petType = ""
    
    petOptions = list(petAttributes.keys())

    while petType not in petOptions:
        print("Select the cat you want to raise! ")
        print("")
        for option in petOptions:
            print(option)
        print("")
        petType = input("Pick a cat: ")

    pet["type"] = petType
    print("")
    pet["name"] = input("Name your " + pet["type"] + "! ")
    print("")

def printMenu(menuOptions):
    optionKeys = list(menuOptions.keys())

    print("Options to choose from:")
    print("")
    for key in optionKeys:
        print(key + ":\t" + menuOptions[key]["text"])

def petCat():
    print(pet["name"] + " loved getting pets!")

def feedCat():
    hungerStat = pet["hunger"] - 20
    if hungerStat < 0:
        hungerStat = -10
    pet["hunger"] = hungerStat
    print(pet["name"] + " has eaten, hunger decreased by 10!")

def playCat():
    print(pet["name"] + " had a lot of fun playing with you!")

def sleepCat():
    sleepinessStat = pet["sleepiness"] - 20
    if sleepinessStat < 0:
        sleepinessStat = -10
    pet["sleepiness"] = sleepinessStat
    print(pet["name"] + " went nightnight, sleepiness decreased by 10!")

def getAttributes():
    print("Unlock cat attributes:")
    print("")
    attributeOptions = petAttributes[pet["type"]]

    attributeNum = -1

    while attributeNum < 0 or attributeNum > len(attributeOptions) - 1:
        for i in range(len(attributeOptions)):
            print(str(i) + ": " + attributeOptions[i])
        print("")
        attributeNum = int(input("Select an attribute: "))
        print("")

    chosenAttribute = attributeOptions[attributeNum]
    pet["attributes"].append(chosenAttribute)
    print(pet["name"] + " has unlocked " + chosenAttribute + "!")

def quitSimulator():
    print("Thanks for playing Tamacatchi, see you soon!")
    print(pet["name"] + " will miss you very much!")

def printStats():
    print(pet["type"] + ", " + pet["name"] + ", is growing!")
    print(pet["name"] + " is " + str(pet["age"]) + " day(s) old.")
    print(pet["name"] + " currently has " + str(len(pet["attributes"])) + " attribute(s): ")
    for attribute in pet["attributes"]:
        print(attribute)
    print(pet["name"] + "'s hunger level is " + str(pet["hunger"]) + "/100.")
    print(pet["name"] + "'s sleepiness level is " + str(pet["sleepiness"]) + "/100.")

def main():
    cat()

    menuOptions = {"A": {"function": petCat, "text": "Give " + pet["name"] + " some nice pets"},
                   "F": {"function": feedCat, "text": "Feed " + pet["name"] + " a yummy treat"},
                   "P": {"function": playCat, "text": "Play with " + pet["name"]},
                   "S": {"function": sleepCat, "text": "Tell " + pet["name"] + " to sleep"},
                   "G": {"function": getAttributes, "text": "Unlock new attributes for " + pet["name"]},
                   "Q": {"function": quitSimulator, "text": "Quit Tamacatchi"}}

    keepPlaying = True
    while keepPlaying:
        menuSelection = ""
        while menuSelection not in menuOptions.keys():
            printMenu(menuOptions)
            print("")
            menuSelection = input("Select option: ").upper()
            print("")

        if menuSelection == "Q":
            keepPlaying = False

        menuOptions[menuSelection]["function"]()

        pet["hunger"] += 10
        pet["sleepiness"] += 10
        pet["age"] += 1

        printStats()

        print()
        
main()
