##Game by Julia Vollmer
from sys import exit
from random import randint, choice
from people import *

class User(object):
    ##User is-a object; has-a money, random strength, name; can-do speak to other people, get money

    def __init__(self):
        self.money = 0
        self.strength = randint(1,20)
        print "What is your name?"
        self.name = raw_input("> ")

    def speak(self, userinput, human):
        print "What do you say?"
        i = 0
        while i <= 1:
            userinput = raw_input ("> ")
            if "money" in userinput:
                human.money()
                i += 1 #you can only ask for money twice
            elif "name" in userinput:
                print human.voc_name[randint(0, len(human.voc_name)-1)]
            elif "murder" in userinput:
                print human.voc_murder[randint(0, len(human.voc_murder)-1)]
                human.murder()
            elif "Gibson" in userinput:
                human.gibson()
            elif "bye" in userinput:
                i = 2
            else:
                print human.voc_error[randint(0, len(human.voc_gibson)-1)]
        print "\nYou end the conversation.\n"

    def add_money(self, value):
        print "You get $%d." % value
        self.money += value
        print "\nYou now carry $%d with you." % self.money
        if self.money >= 5:
            a_game.booth = True
        elif self.money >= 20:
            a_game.ticket = True

class Item(object):
     ##Item is- object; has-a name, description, 'usefullness value', can-do 'look' give out information

    def __init__(self, name, description, val):
        self.name = name
        self.description = description
        self.status = val

    def look(self):
        print "\t\t#%s#" % self.name
        print self.description
        if self.status == 11:
            a_game.key = True
        else:
            a_game.gibsonval += self.status
            self.status = 0
        if a_game.gibsonval >= 10:
            a_game.gibson = True

class Scene(object):

    def items(self, item1, item2, item3): #Scene can have 3 items
        self.hints = [item1, item2, item3]
        print "You can spot these things around here:"
        for clue in self.hints:
            print clue.name, "\t",
        print "\nWhat do you want to examine further?"
        itemlook = raw_input("> ")
        while "no" not in itemlook:
            if itemlook == item1.name:
                item1.look()
            elif itemlook == item2.name:
                item2.look()
            elif itemlook == item3.name:
                item3.look()
            print "Something else?"
            itemlook = raw_input("> ")
        print "You stop the examination of items."

    def enter(self): #actual output
        print"enter()."
        exit(1)

    def next_places(self, directions, other_place1, other_place2, other_place3, other_place4):
        #choosing next place
        print "In which direction do you want to go?"
        print directions
        userinput = raw_input("> ")
        if 'forward' in userinput:
            return other_place1
        elif 'right' in userinput:
            return other_place2
        elif 'backwards' in userinput:
            return other_place3
        elif 'left' in userinput:
            return other_place4
        else:
            print "You seem to not know your way."

class Engine(object):

    def __init__(self, scene_map): #set start values
        self.scene_map = scene_map
        self.key = False
        self.number = "%d%d%d" % (randint(0,9), randint(0,9), randint(0,9))
        self.gibsonval = 0
        self.gibson = False
        self.witness = False
        self.user = User()
    def play(self):
        print "You wake up. Cold, confused and without memories about the day before."
        print "As you look down on yourself, you noticed that your hands are covered in blood."
        print "What happened yesterday?"
        print "On you left arm you see some numbers. Unfortunately you can only decipher two of the three digits."
        print "%s and %s" % (self.number[randint(0,1)], self.number[2])
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('wagon_final')
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene): ##just for people who want to go left/right when they shouldn't

    reason = [
        "You get lost and wander around the snowy landscape. You freeze to death",
        "You run into a gang member. Great, the hole in your head was a perfect shot.",
        "As you stumble over your one feet, you scream so loud, the police come and arrest you.",
    ]

    def enter(self):
        print Death.reason[randint(0, len(self.reason)-1)]
        exit(1)

class SnowLandscape(Scene):

    def enter(self):
        print "\n\n\t##The Snow Landscape##"
        print "The white snow is tainted in red... You know what it is."
        print "You standing in the middle of this wide white landscape."
        print "In front of you can spot a huge mansion in the distance."
        print "On your right is a dark forest and behind you is a path leading to a small village. "
        next_place = self.next_places("\t 'forward' \n'left' \t\t\t\t 'right' \n\t 'backwards'", 'villa', 'forest', 'village', 'death')
        return next_place

class Forest(Scene):

    def enter(self):
        print "\n\n\t##The Forest##"
        print "The forest is dark. As you look for a path, you get frighten by the view in front of you."
        print "There is a corpse. Blood. And you have blood on your hand..."
        self.items(Item("Can", "This just seems to be trash thrown away in nature.", 0),
        Item("Key", "It is a small, fragile golden key. You can see some blood stains.\nYou take it.", 11),
        Item("Earring", "The earring looks really expensive.\nWait... it's only a single one.\nWhen you take a closer look at the body, you realise all the valuables are missing. ", 1))
        return 'snow_landscape'

class Villa(Scene):

    def enter(self):
        print "\n\n\t##The Huge Mansion##"
        print "You enter the huge mansion. Judging from the interior, the owner must be really rich."
        print "Oh... There is a blood trail going from the entrance to another room. You follow it."
        print "The blood trail stops in what seems to be the study. This must have been the crimescene."
        self.items(Item("Calendar", "The 9th December is marked with an heart on this calendar.", 0),
        Item("Safe", "The safe is still open, you can see the code '1209'.\nThe inside of the safe is completely empty except for two ring.\nThey have initials engraved on them: 'E.G. + M.R.H.'.", 2),
        Item("Note", "Note:\n\tMr Gardon called. You should immediatly called back.\n\t\t- C. Collins", 0))
        print "You go to the desk and try to open the drawers."
        if a_game.key == True:
            print "Oh, the key you found earlier fits into one of the drawers and you open it."
            self.items(Item("Book", "This seems to be an old copy of Hermann Hesse's 'Demian'", 1),
            Item("Postcard", "Some postcard from Hawaii.", 0),
            Item("Letter", "It seems to be a love letter:\n\tMy lovely Mathilda,\n\tyou're are my everything and I love you so much.\n\tThe time we spent apart, feels like forever.\n\tI received your gift. Thank you so much! I love you.\n\tTill death parts us I'm yours.\n\tYours forever, E.Gibson", 4))
        else:
            print "Every drawer is locked."
        print "You're done with investigating."
        next_place = self.next_places("\t 'forward' \n'left' \t\t\t\t 'right' \n\t 'backwards'", 'villa', 'forest', 'village', 'death')
        return next_place

class Village(Scene):
    def enter(self):
        print "\n\n\t##The Village##"
        print "The village is in an uproar. In the forest near the village someone found a corpse."
        print "Mathilda Rosa Hesse, a bestseller author was murdered and you're the prime suspect!"
        self.items(Item("Book", "Someone forgot it here. 'Demian' by Hermann Hesse. \nIt tells the story of Emil Sinclair, who is taught by Max Demian to look at things in a different way.", 4),
        Item("Teabox", "Mrs Hesse really like drinking tea.", 0),
        Item("Shoe", "Someone lost a really nice looking shoe. Seems the person was in a hurry.", 1))
        print "If you follow the main street, you would reach the Sunnyhill park."
        print "But maybe you would rather visit the bar on your left or the police station opposite of it?"
        next_place = self.next_places("\t 'forward' \n'left' \t\t\t\t 'right' \n\t 'backwards'", 'park', 'police_station', 'snow_landscape', 'bar')
        return next_place

class Bar(Scene):

    def enter(self):
        print "\n\n\t##The Bar [Karlsberger]##"
        people = [Police("Benton Jacobson"), Gangster("Tom Siddal"), Citizen("Demian Gardon"), Gangster("Emily Foster"), Gangster("Henning Rodd") ]
        human = choice(people)
        print "You see someone standing at the bar, do you want to talk to the person?"
        userinput = raw_input("(yes/no)> ")
        if userinput == "no":
            pass
        else:
            a_game.user.speak(userinput, human)
        value = randint(1, 5)
        print "As you leave the bar, you find a bit money: $%d." % value
        a_game.user.money += value
        print "\t You now carry $%d with you." % a_game.user.money
        if a_game.user.money >= 2:
            a_game.booth = True
        elif a_game.user.money >= 20:
            a_game.ticket = True
        return 'village'

class PoliceStation(Scene):

    def enter(self):
        print "\n\n\t##The Police Station##"
        people = [Police("Benton Jacobson"), Police("Gideon Landen"), Citizen("Emilia Gibson"), Police("Christie Denmann"), Police("Tina Meyer") ]
        human = choice(people)
        print "You're are in front of the police station."
        print "You hear people talking about the recent murder that took place here."
        while a_game.gibson == True:
            print "You go inside the police station and tell everyone that you know the culprit. It is:"
            guess = raw_input("(full name)> ")
            if guess == "Emil Gibson":
                print "During the questioning, you could prove your innocence with all the evidence you found."
                print "Emil Gibson, the secret lover of Mathilda Rosa Hesse could be arrested"
                print "thanks to you. He had ties with the local gang and was a gold digger."
                print "When Mathilda Rosa Hesse didn't want to give him any money,"
                print "he killed her in his rage. Thanks to your hard work, this case is now closed."
            else:
                print "You thought you could leave the station, after telling them the wrong culprit?"
                print "You could neither provide an alibi nor the name of the murderer. You are arrested and sentenced to life in prison."
                print "While you rot in prison, you think about the murderer, who's still on the loose."
                print "Too bad, that you had enough hints. It was so close."
            print "Good job, %s" % a_game.user.name
            exit(0)
        print "Want to talk to someone?"
        userinput = raw_input("(yes|no)> ")
        if userinput == "no":
            pass
        else:
            a_game.user.speak(userinput, human)
        value = randint(1, 10)
        print "You go back to the main street."
        return 'village'

class Park(Scene):

    def enter(self):
        print "\n\n\t##Park Sunnyhill##"
        print "The park is peaceful. When you go straight, you would arrive at the train station. "
        people = [Police("Alexandra Phelps"), Gangster("Marie Smith"), Citizen("Elaine Foster"), Citizen("Dave Flanders"), Citizen("Walter Demian") ]
        human = choice(people)
        print "Someone is sitting on a bench. Do you want to talk to the person?"
        userinput = raw_input("(yes/no)> ")
        if userinput == "no":
            pass
        else:
            a_game.user.speak(userinput, human)
        print "There is also a phone booth next to this bench."
        print "Do you want to call someone?"
        userinput = raw_input("> ")
        if 'yes' in userinput:
            if a_game.user.money >= 5:
                print "Please dial the 3-digit phone number."
                guess = raw_input("> ")
                while guess != a_game.number and a_game.user.money >= 1:
                    print "This number does not exit. Please try again."
                    a_game.user.money = a_game.user.money - 1
                    guess = raw_input("> ")
                if guess == a_game.number:
                    a_game.witness = True
                    print "'Hello? Is it you, %s?'" % a_game.user.name
                    print "'It's me Cailyn Collins. Good that you remembered my phone number."
                    print "'I heard you're the prime suspect for the murder on Mrs Hesse?"
                    print "'We should meet up! I definetly know, you aren't the perpretator."
                    print "'Because of the local gang I'm afraid to set a foot in our village."
                    print "'Let's meet in a train. Bye!''"
                else:
                    print "You have not enough money. You used it all up."
            else:
                print "You have not enough money."
        else:
            print "You skip phoning someone."

        next_place = self.next_places("\t 'forward' \n\t 'backwards'", 'train_station', 'death', 'village', 'death')
        return next_place

class TrainStation(Scene):

    def enter(self):
        print "\n\n\t##The Train Station##"
        print "Do you want to buy a $20 train ticket?"
        userinput = raw_input("(yes|no)> ")
        if a_game.user.money >= 20 and userinput == 'yes':
            print "You get yourself a ticket and enter the next train."
            return 'wagon_final'
        elif userinput == 'yes':
            print "Your $%d are not enough for this purchase." % a_game.user.money
            return 'park'
        else:
            return 'park'

class WagonFinal(Scene):

    def enter(self):
        print "\n\n\t##Train-Last Wagon##"
        if a_game.witness == True:
            print "You meet Caily Collins. She is a key witness to this case and provides you with an alibi."
            print "Caily Collins was the assistant of Mathilda Rosa Hesse and noticed that things were off."
            print "On the day of the crime, Emil Gibson, the secret lover of Mrs Hesse seemed really furios."
            print "Caily was actually the person, who called you in order to check on Mrs Hesse, since she had to leave."
            print "Before she got on the train, she was talking to you all the time, explaining details,\n when the connection was suddenly cut."
            print "You must have arrived during the time Emil Gibson was trying to hide the corpse."
            print "As he was surprised by your visit, he attacked you and tried to make it look like you're culprit."
            print "Good job, %s. You proved your innocene and can enjoy your freedom." % a_game.user.name
        else:
            print "You flee from the village, without being able to prove you innocence."
            print "Now you're forever on the run. So nice..."
        exit(0)

# class Person(object):
#
#     def __init__(self, name):
#         self.name = name
#         self.voc_money = "Reaction to money question."
#         self.voc_name = "Reaction to name question."
#         self.voc_murder = "Reaction to question about the murder."
#         self.voc_gibson = "Reaction to question about Gibson."
#         self.voc_error = "Reaction to unclear answer."
#
#     def money(self):
#         print self.voc_money[randint(0, len(self.voc_money)-1)]
#
#     def murder(self):
#         pass
#
#     def gibson(self):
#         print self.voc_gibson[randint(0, len(self.voc_gibson)-1)]

class Police(Person):

    def __init__(self, name):
        super(Police, self).__init__(name)
        self.voc_money = [
            "Actually, I'm a undercover police officer.\nSince police officers should be role models, I will give a good example\n and give you some.",
            "Yes, I have a bit change left, I could give you.",
            "I'm glad, if I can help others.",
            "You seem to need it."
        ]
        self.voc_name = [
            "I'm %s. If you ever need help, I'm actually a police officer." % self.name,
            "Hello. I'm police officer %s, nice to meet you!" % self.name
        ]
        self.voc_murder = [
            "Why are you asking? You seem a bit suspicious.",
            "I'm police officer %s. Your interest in this case is shady." % self.name
        ]
        self.voc_gibson = [
            "I have no idea, who this is. I'm sorry.",
            "Who is this? Is he connected to the murder case?",
            "Gibson, never heard of him."
        ]
        self.voc_error = [
            "Sorry, I couldn't hear you.",
            "What did you say?",
            "What was the question again?",
            "Even though I'm a police officer I do not have superhuman hearing."
        ]

    def money(self):
        print self.voc_money[randint(0, len(self.voc_money)-1)]
        value = randint(1, 10)
        a_game.user.add_money(value)


    def murder(self):
        print """'%s I'm taking you in for questioning as an suspect of the murder on Mathilda Rosa Hesse.
You have the right to remain silent. If you choose to give up that right,
anything you say can and will be used against you in a court of law.
You have the right to speak to an attorney, and to have an attorney present during any questioning.
If you cannot afford a lawyer, one will be provided for you at government expense.'  """ % a_game.user.name
        print "Do you know, who the real murderer is?"
        guess = raw_input("(full name)> ")
        if guess == "Emil Gibson":
            print "During the questioning, you could prove your innocence with all the evidence you found."
            print "Emil Gibson, the secret lover of Mathilda Rosa Hesse could be arrested"
            print "thanks to you. He had ties with the local gang and was a gold digger."
            print "When Mathilda Rosa Hesse didn't want to give him any money,"
            print "he killed her in his rage. Thanks to your hard work, this case is now closed."
        else:
            print "You couldn't provide neither alibi nor the murderer. You are arrested and sentenced to life in prison."
            print "While you rot in prison, you think about the murderer, who's still on the loose."
        print "Good job, %s" % a_game.user.name
        exit(0)

class Gangster(Person):

    def __init__(self, name):
        super(Gangster, self).__init__(name, )
        self.strength = randint(0, 20)
        self.voc_money = [
            "'So you wanna get some money from me?'",
            "'I don't give money to weaklings!'",
            "'You idiot think, I will give you money?'",
            "'You need to be worthy of my money!'"
        ]
        self.voc_name = [
            "'What the heck do you want?'",
            "'Tell me f***ing reason, why I should?!'",
            "'Get lost!'",
            "'F*** off!'",
            "'You would faint hearing my name. Be glad, you're in the dark.'",
            "'My name? You're biggest nightmare''"
        ]
        self.voc_murder = [
            "'You mean the murder on this bestseller author? She was an old hag.'",
            "'Mrs Hesse had this young lady, who would assist her from time to time. \nShe was quite hot.'",
            "'The victim deserved it.'",
            "'I wonder who's going to inherit all the money?! I better find out...'"
        ]
        self.voc_gibson = [
            "'Who are you, asking about Gibson?'",
            "'It seems, you wanna die today?'",
            "'Silence is the best way to stay alive here. Bad you didn't know.'",
            "'Look at me! DO I SEEM LIKE A TRAITOR?!!!'",
            "'Did you write your last will yet?'"
        ]
        self.voc_error = [
            "'I don't waste my time on people that can't talk properly!'",
            "'Don't was my time!'",
            "'Was this supposed to be English?'"
        ]

    def money(self):
        print self.voc_money[randint(0, len(self.voc_money)-1)]
        print "'If you can guess correct, I will give you money.'"
        print "'We're going to do arm wrestling. Do you think you will 'win', 'lose' or play 'even'?'"
        wrestling = raw_input("> ")
        if self.strength < a_game.user.strength and wrestling == "win":
            value = randint(1, 5)
            print "'I will give you $%d. Your strength was %d and mine %d. You win.'" % (value, a_game.user.strength, self.strength)
            a_game.user.add_money(value)
        elif self.strength == a_game.user.strength and wrestling == "even":
            value = randint(1, 5)
            print "'Yes, we played even. I will give you $%d.'" % value
            a_game.user.add_money(value)
        elif self.strength > a_game.user.strength and wrestling == "lose":
            value = randint(1, 5)
            print "'I lose with %d to %d. I will give you $%d.'" % (a_game.user.strength, self.strength, value)
            a_game.user.add_money(value)
        else:
            print "'HAHAHA! Wrong. You get nothing!'"

    def gibson(self):
        print self.voc_gibson[randint(0, len(self.voc_gibson)-1)]
        print "You're so lucky! You ran into a gangster. He saw no other way then to keep you silent forever."
        print "%s, hurrah! You're dead, not knowing how the case will be solved." % a_game.user.name
        exit(0)

class Citizen(Person):

    def __init__(self, name):
        super(Citizen, self).__init__(name)
        self.voc_money = [
            "'I don't have money on me.'",
            "'As a general rule I don't give money to strangers. I would rather give food.'",
            "'I'm sorry, I don't have cash on me.'",
            "'I'm a poor student. Where should I get the money from?'",
            "'If I had, I would.'"
        ]
        self.voc_name = [
            "'My name is %s.'" % self.name,
            "'People call me %s. Don't know what my parents thought, when they named me.'" % self.name,
            """'Names are so irrelevant. So many people have the same name.
            Let me guess, your name is %s. I'm %s.""" % (a_game.user.name, self.name)
        ]
        self.voc_murder = [
            "'The victim really liked reading. Her favorite book was 'Demian' by Herman Hesse'.",
            """'Everyone thought Mathilda Rosa Hesse was crazy for her obsession with this one book.
            According to rumors, even the name of her secret lover was similar to the main character.'""",
            "'I wonder what Cailyn, the assistant of Mathilda Rosa is doing. She seems to have left the village yesterday.'",
            "'If you want to know more about the victim, you should ask Cailyn. Her phone numbered ended with %s.'" % a_game.number,
            "'Mathilda Rosa Hesse was a bestseller author. She was filthy rich and lived in this huge villa outside the village.'"
        ]
        self.voc_gibson = [
            "'Gibson? I think he was involved in some kind of gang activity.'",
            "'Oh, you mean this gold digger? No idea where he is.'",
            "'This young guy is quite popular with women.'",
            "'I didn't see him today.",
            "'I heard through the grapevine that he was the secret lover of Mrs Hesse. He must be devastated.'"
        ]
        self.voc_error = [
            "'What did you say?'",
            "Could you repeat this?"
        ]

class Map(object):

    scenes = {
        'death': Death(),
        'snow_landscape': SnowLandscape(),
        'forest': Forest(),
        'villa': Villa(),
        'village': Village(),
        'police_station': PoliceStation(),
        'bar': Bar(),
        'park': Park(),
        'train_station': TrainStation(),
        'wagon_final': WagonFinal(),
    }

    def __init__(self):
        self.start_scene = 'snow_landscape'

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map()
a_game = Engine(a_map)
a_game.play()
