print """
You are in front of an dark house. What are you going to do?
\n \t 1. Go inside the house.
\n \t 2. Walk through the garden.
\n \t 3. Run away as fast as you can. The house seems creepy.
"""
firstd = raw_input("> ")

if firstd == "1":
    print """You slowly open the door.\nAfter the door stops squeaking you notice the stifling atmosphere.
    \n \t 1. Go up the stairs.
    \n \t 2. Exit the house immediatly.
    """
    secondd = raw_input("> ")
    if secondd == "1":
        print "While you go up the stairs, you're too carefree and don't notice the missing step. \n...\n..\n. \nThat hurt. \nAfter the fall, you just want to go and never come back."
    elif secondd == "2":
        print "You're a scaredycat, but as you stumble out of the house, you don't care."
    else:
        print "While you can't decide to do, some taps on your shoulder. \nYou faint."
elif firstd == "2":
    print "The garden is covered with mist. You can't see anything.\n Suddenly you fall."
    print "\n \t 1. Look down to see what you just hit."
    print "\n \t 2. Close you eyes and just return home."
    thirdd = raw_input("> ")
    if thirdd == "1":
        print "As you see the gravestone you pass out."
    elif thirdd == "2":
        print "Good decision. Your knees hurt from the fall, but apart from that you're doing fine."
        print "Who knows what could have happened to you at this creepy house?"
    else:
        print "You lying there on the wet ground and feel the coldnees creeping in your bones."
elif firstd == "3":
    print "You don't waste another thought on this house and just go back to your normal stuff."
else:
    print "Just standing there won't make a difference. Make clear decision."
