# My game
from sys import argv, exit
script, name = argv #Player's name
# Theme: deserted island / plane crash
inventar = []
stuff = ["signal light", "coconut", "canned food", "lighter", "rope"]
survivor = 1
last_words = " "
raft = False
fire = False
def survivors(number):
    global survivor
    print "Do you want to ask them to join you?"
    choice_survivors = raw_input("> ")
    if "yes" == choice_survivors:
        survivor += number
        print "You are now a group of %d." % survivor
    elif "no" == choice_survivors:
        print "Shame on you. But maybe you have better survival chances alone."
    else:
        faint()
    return survivor

def inventar1(pick):
    inventar.append(pick)
    print "This is in your inventar now:", inventar

def jungle():
    # traps, tools,... leaves logs
    print "The jungle is a ocean of greens with a bit of color here and there. You spot hidden paths in all of this."
    print "\t 'straight' \n'left' \t\t\t\t 'right' \n\t 'back'"
    choice_jungle = raw_input("> ")
    if "right" in choice_jungle:
        print "There are some fallen trees lying around."
        print "You pick up the logs. Who knows, they might help somehow?"
        inventar1("logs")
        global raft
        if not raft and "rope" in inventar:
            raft = True
            print "You use the logs and the rope to build a raft!"
            print "Genius."
        print "Let's go back."
        jungle()
    elif "left" in choice_jungle:
        print "You encounter a village hidden inside the woods. Do you want take a look?"
        choice_village = raw_input("> ")
        if "yes" == choice_village:
            village()
        else:
            print "Watching from the distance might be the best. You return."
            jungle()
    elif "back" in choice_jungle:
        print "You go back to the beach."
        beach_beginning()
    elif "straight" in choice_jungle:
        junglepath()
    else:
        dead("You stepped on a snake. A poisonous snake.")

def junglepath():
    print "You pass some stones and all these green plants."
    print "Want to pick up some sticks or leaves?"
    choice_junglepath = raw_input("> ")
    if "stick" in choice_junglepath:
        inventar1("stick")
        tool = "a stick"
    elif "leaves" in choice_junglepath:
        inventar1("leaves")
    elif "yes" == choice_junglepath:
        inventar1("stick")
        inventar1("leaves")
    else:
        print "You leave the stuff there and go on."
    print "\t 'straight' \n'left \t\t\t\t 'right' \n\t 'back'"
    choice_furtherway = raw_input("> ")
    if "straight" in choice_furtherway:
        hill()
    elif "left" in choice_furtherway:
        print "You're making your way through the thicket."
        print "Damn it! You fall down a trap. Who build this?"
        dead("There seems to be cannibals living in this jungle and you just went straight in their trap.")
    elif "right" in choice_furtherway:
        print "You stumble on some roots and when you look up, you can see smoke coming from a bonfire."
        print "You get closer to the bonfire and spot three other survivors!"
        survivors(3)
        junglepath()
    elif "back" in choice_furtherway:
        jungle()
    else:
        faint()

def village(): #cannibal village
    print "Oh no, it seems the people are cannibals."
    if "blanket" in inventar and "coconut" in inventar:
        print "You have a blanket and a coconut in your inventar"
        print "Are you insane enough for this idea?"
        choice_king = raw_input("> ")
        if "yes" in choice_king or "hell yeah" in choice_king:
            print """
            You take the blanket, wrap it around yourself like a cape and put the coconut on your head.
            As you slowly enter the village, you walk around majestically and wave your hands at the cannibals.
            What seems to be the village eldress approaches you and falls down on his feet.
            Then you realise, your cool king costume worked.
            Congratulations Royal Highness %s II. from Up The Air.
            In celebration of your coronation, another survivor is sacrificed.
            Good job! Staying here forever seems like a great idea!
            """ % name
            exit(0)
        else:
            print "%s, you are a sissy. Okay then." % name
    else:
        print "Oh wait, they even captured another survivor!"
    print "Do you wish to rescue him?"
    choice_cannibals = raw_input("> ")
    global survivor
    if "yes" == choice_cannibals and "stick" in inventar:
        print "You fought against the cannibals with a stick and rescued Bob, a truck driver from Texas."
        survivor += 1
        print "He joins your group. You are now %d people." % survivor
        jungle()
    elif "yes" == choice_cannibals and "coconut" in inventar:
        print "You throw the coconut at the head of a cannibal and rescue Bob, a truck driver from Texas."
        survivor += 1
        print "He joins your group. You are now %d people." % survivor
        jungle()
    elif "yes" == choice_cannibals:
        print "The cannibals spot you and immediatly attack you."
        dead("You don't have anything to defend yourself. What a tasty dinner you are.")
    else:
        print "Okay. You really don't have to rescue this poor little guy over there."
        jungle()
    return survivor

def boat(): #picking up other survivors
    print "You get close to the deflated rescue boat."
    print "Oh! You can spot other survivors!"
    print "There is a flight attentant, a nosy passenger and a mother with a child."
    survivors(4)
    print "Lets go back to the beach."
    beach()

def hill():    #where the signal is best seen
    print "You reach a hill"
    print "The view from here is stunning. You can oversee the whole island."
    while "signal light" in inventar or fire:
        print "This gives you and idea. This might be the best spot for..."
        choice_hill = raw_input("> ")
        if "signal" in choice_hill and "signal light" in inventar:
            print "So you want to %r?" % choice_hill
            print "You use the signal as a beacon and a rescue team gets your location."
            print "Everyone is rescued and back home! %s, you're the best!" % name
            exit(0)
        elif "smoke" in choice_hill:
            print "You use the flammable things to make a smoke signal."
            print "Maybe you're lucky and someone will see it?"
            print "Yes! The fire attracts the attention of a ship in the distance."
            print "%s, you can finally return home!" % name
            exit(0)
        else:
            faint()
    print "Let's go down again."
    junglepath()

def beach(): #picking up things
    print "You are at the beach. You can spot several things around here:"
    print "A deflated rescue boat in the distance"
    for things in stuff:
        print things
    print "What are you going to do?"
    print "Remember. You're not a superhuman and not capable for multitasking."
    choice_things = raw_input("> ")
    if "lighter" in choice_things:
        print "You went to the lighter and picked it up."
        global fire
        inventar1("lighter")
        if (not fire and "magazine" in inventar) or (not fire and "leaves" in inventar):
            fire = True
        else:
            print "Maybe you could use this lighter..."
        stuff.remove("lighter")
    elif "signal light" in choice_things:
        print "How handy. You picked up the signal light. What could you do with this?"
        stuff.remove("signal light")
        inventar1("signal light")
    elif "coconut" in choice_things:
        print "You're going to the coconut. Do you want to eat it? Yes or No?"
        choice_coconut = raw_input("> ")
        if "Yes" == choice_coconut:
            print "You try to open the coconut with your head and feel dizzy."
            faint()
        else:
            print "You don't know what to do with the coconut, so you just put it in your bag."
            stuff.remove("coconut")
            inventar1("coconut")
    elif "canned food" in choice_things:
        print "You pick up the canned food and suddenly feel really hungry."
        dead("You devour the food, but do not realize it is spoiled.")
    elif "rope" in choice_things:
        print "You take the rope."
        global raft
        inventar1("rope")
        if not raft and "logs" in inventar:
            print "Wait... You have enough materials for a raft!"
            raft = True
            print "You know have a raft. Your escape is so close."
        else:
            print "This rope could be useful in the future."
        stuff.remove("rope")
    else:
        print "You're not picking anything up."

    if "boat" in choice_things:
        boat()
    else:
        print "Anything else? 'Yes' \t'No'"
        choice_pick = raw_input("> ")
        if "yes" in choice_pick:
            beach()
        else:
            print "Let's go back to the front beach."
            beach_beginning()
    return fire, raft

def faint(): #can't make a valid decision
    print "You're exhausted and while the sun steadily hits you, you faint."
    print "You must have lost your memories and somehow ended back at the beach."
    beach_beginning()

def ocean(): #escape spot
    print "You are at the ocean. What do you want to do?"
    print "Swim back? Or do you have a raft?"
    choice_ocean = raw_input("> ")
    if "swim" in choice_ocean:
        dead("You do not have the strength for this. You drown.")
    elif "raft" in choice_ocean and raft:
        print "You take your selfmade raft. It needs to fit %d people." % survivor
        print "How many people including will you let on your raft?"
        choice_raft = raw_input("> ")
        people = int(choice_raft)
        if people > 6 and people == survivor:
            dead("Your intentions were good, but the raft can't withhold the weight.\nEveryone including you drowns on the open sea and dies. ")
        elif people < 6 and people < survivor:
            print "You successful escaped, but you left other people on the island behind."
            print "Your guilty conscience will forever haunt you. Great!"
            exit(0)
        elif people < 6 and people == survivor:
            print "Great! Thanks to you, the escape from the island was succesfull! Be happy back at home."
            print "%s ,good job on staying alive." % name
            exit(0)
        else:
            print "You seem undecided and take a long while thinking."
            faint()
    else:
        print "You don't want to swim and don't even have a raft! Maybe you could build one?"
        print "Right now this is in your inventar:", inventar
        print "Let's go back to the beach!"
        beach_beginning()

def beach_beginning():
    print """In front of you is a white beach.
While you look around you see the wide ocean, a jungle and the endless beach. What will you do?
\t1 I will try my luck with the ocean!
\t2 I will explore this island more and go to the jungle.
\t3 Maybe I find usefull stuff from the plane crash at the beach. I will take a look."""
    choice_beach = raw_input("> ")
    if choice_beach == '1':
        ocean()
    elif choice_beach == '2':
        print 'You are brave enough to go inside the jungle.'
        jungle()
    elif choice_beach == '3':
        print "You look around the beach a bit more."
        beach()
    else:
        print"Just standing there in the sun, won't do anything good!"
        faint()

def dead(why):
    print why, "\nGreat job %s, you're dead. Your relatives are devasted. But somehow your last words reached them. \nMaybe that will make them feel better:" % name
    print last_words
    print "Or not."
    exit(0)

def start():
    print "'%s, welcome at board on our airplane 'Straight to Heaven'. We wish you a pleasant journey.'" % name
    print "'Do you wish to browse through our duty-free magazine or want to have a blanket?'"
    choice_plane = raw_input("> ")
    if "magazine" in choice_plane and "blanket" in choice_plane:
        inventar.append('magazine')
        inventar.append('blanket')
    elif "magazine" in choice_plane:
        inventar.append('magazine')
    elif "blanket" in choice_plane:
        inventar.append('blanket')
    else:
        print "'I'm sorry, we don't offer this.'"
    print "'Now lay back and relax.'"
    print "...\n..\n."
    print "\n'Dear passengers, there are some turbulences. Please do not pa--'"
    print "Any last words, %s?" % name
    global last_words
    last_words = raw_input("> ")
    print "Hey %s, your last words were really nice, but you might be still alive." % name
    print "You slowly open your eyes."
    print "You must have survived the plane crash, but now you are stranded on an unkown island in the middle of nowhere."
    beach_beginning()
    return inventar
    return last_words

start()
