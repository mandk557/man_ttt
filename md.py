start = print("Welcome to MID LAB GAME")
choose = input("We have 3 templates choose 1, 2, 3: ")

if choose == "":
    print("Error: input is empty. Please enter 1, 2, or 3. Exiting.")
    exit()
elif choose not in ["1", "2", "3"]:
    print("Invalid choice. Please enter 1, 2, or 3. Exiting.")
    exit()

start_2 = print("Now put random things what it will ask !")

if choose == "1" :


    Number = int(input("Number : "))
    Measure_of_time = input("Measure of time : ")
    Mode_of_Transportation = input("Mode of Transportation : ")
    Adjective = input("Adjective : ")
    Adjective2 = input("Adjective2 : ")
    Noun = input("Noun : ")
    Color = input("Color : ")
    Part_of_the_Body = input("Part of the Body : ")
    Verb = input("Verb : ")
    Number2 = int(input("Number2 : "))
    Noun2 = input("Noun2 : ")
    Noun3 = input("Noun3 : ")
    Part_of_the_Body2 = input("Part of the Body2 : ")
    Verb = input("Verb : ")
    Noun4 = input("Noun4 : ")
    Adjective3 = input("Adjective3 : ")
    Silly_Word = input("Silly Word : ")
    Noun = input("Noun : ")

    choose_1 = print(
        f"It was about {Number} {Measure_of_time} ago when I arrived at the hospital in a {Mode_of_Transportation}. "
        f"The hospital is a/an {Adjective} place, there are a lot of {Adjective2} {Noun} here. "
        f"There are nurses here who have {Color} {Part_of_the_Body}. "
        f"If someone wants to come into my room I told them that they have to {Verb} first. "
        f"I’ve decorated my room with {Number2} {Noun2}. Today I talked to a doctor and they were wearing a {Noun3} on their "
        f"{Part_of_the_Body2}. I heard that all doctors {Verb} {Noun4} every day for breakfast. "
        f"The most {Adjective3} thing about being in the hospital is the {Silly_Word} {Noun} !")

elif choose == "2" :

    Persons_Name = input("(Proper Noun (Person’s Name)) : ")
    Noun = input("Noun : ")
    Adjective = input("Adjective (Feeling) : ")
    Verb = input("Verb : ")
    Adjective2 = input("Adjective2 (Feeling) : ")
    Animal = input("Animal : ")
    Verb2 = input("Verb2 : ")
    Color = input("Color : ")
    Verb3 = input("Verb (ending in ing) : ")
    Adverb = input("Adverb (ending in ly) : ")
    Number = int(input("Number : "))
    Measure_of_Time = input("Measure of time : ")
    Color = input("Color : ")
    Animal = input("Animal : ")
    Number = int(input("Number : "))
    Silly_Word = input("Silly Word : ")
    Noun2 = input("Noun2 : ")

    choose_2 = print(f"This weekend I am going camping with {Persons_Name}."
                     f" I packed my lantern, sleeping bag, and {Noun}. "
                     f"I am so {Adjective} to {Verb} in a tent. "
                     f"I am {Adjective2}  we might see a(n) {Animal}, I hear they’re kind of dangerous. "
                     f"While we’re camping, we are going to hike, fish, and {Verb2}. I have heard that the {Color} lake is great for {Verb3}. "
                     f"Then we will {Adverb} hike through the forest for {Number} {Measure_of_Time}. "
                     f"If I see a {Color} {Animal} while hiking, I am going to bring it home as a pet! "
                     f"At night we will tell {Number} {Silly_Word} stories and roast {Noun2} around the campfire!!")

elif choose == "3" :

    Person_Name = input("Person Name : ")
    Adjective = input("Adjective : ")
    Color = input("Color : ")
    Animal = input("Animal : ")
    Place = input("Place : ")
    Adjective2 = input("Adjective2 : ")
    Magical_Creature = input("Magical Creature (Plural) : ")
    Adjective3 = input("Adjective3 : ")
    Magical_Creature2 = input("Magical Creature2 (Plural) : ")
    Room_in_a_House = input("Room in a House : ")
    Noun = input("Noun : ")
    Noun2 = input("Noun2 : ")
    Noun3 = input("Noun3 (Plural) : ")
    Adjective4 = input("Adjective4 : ")
    Noun4 = input("Noun4 (Plural) : ")
    Number = int(input("Number : "))
    Measure_of_time = input("Measure of time : ")
    Verb = input("Verb (ing) : ")
    Adjective5 = input("Adjective5 : ")
    Noun5 = input("Noun5 : ")

    choose_3 = print(f"Dear {Person_Name} , I am writing to you from a {Adjective} castle in an enchanted forest. "
                     f"I found myself here one day after going for a ride on a {Color} {Animal} in {Place}. "
                     f"There are {Adjective2} {Magical_Creature} and {Adjective3} {Magical_Creature2} here! "
                     f"In the {Room_in_a_House} there is a pool full of {Noun}. "
                     f"I fall asleep each night on a {Noun2} of {Noun3} and dream of {Adjective4} {Noun4}. "
                     f"It feels as though I have lived here for {Number} {Measure_of_time}. "
                     f"I hope one day you can visit, although the only way to get here now is {Verb} on a {Adjective5} {Noun5}!! ")


