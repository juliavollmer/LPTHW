from random import randint, choice
from sys import exit, argv

class User(object):

    def __init__(self):
        self.bag = []
        self.money = 0
        self.strength = randint(1,20)

    def pick(self, item):
        self.bag.append(item)
        print "This is in your bag know: %s" % self.bag
        print "Want to examine something further?"
        userinput = raw_input("> ")

    def speak(self, userinput, human):

        while ("bye" or "no") not in userinput:
            print "What will you ask?"
            userinput = raw_input ("> ")
            if "money" in userinput:
                self.human.money()
            elif "name" in userinput:
                print self.human.voc_name[randint(0, len(self.human.voc_name)-1)]
            elif "murder" in userinput:
                print self.human.voc_murder[randint(0, len(self.human.voc_murder)-1)]
                self.human.murder()
            elif "Gibson" in userinput:
                self.human.gibson()
            else:
                print self.human.voc_error[randint(0, len(self.human.voc_gibson)-1)]



class Place(object):

    def go(self):
        print "enter()"
        return 'snow_landscape'

    def next_places(self, directions, other_place1, other_place2, other_place3, other_place4):
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



    # def init_person(self):
    #
    #     while ("bye" or "no") not in userinput:
    #         human.speak(userinput)
    #         userinput = raw_input("> ")

class Engine(object):

    def __init__(self, place_map):
        self.place_map = place_map
        self.booth = False
        self.ticket = False
        self.number = "%d%d%d%d" % (randint(0,9), randint(0,9), randint(0,9), randint(0,9))
        self.gibson = False
        self.witness = False
        self.user = User()

    def begin(self):
        current_place = self.place_map.opening_place()
        self.user = User()
        print "You wake up. Cold, confused and without memories about the day before."
        print "How are you doing?"
        while self.witness == False:
            next_place_name = current_place.go(self.user)
            current_place = self.place_map.next_place(next_place_name)

        current_place.go(self.user)

    # def decision(self):
    #     userinput = raw_input("> ")

class Death(Place):
    quips = [
        "You died. You kinda suck at this.",
        "You mom would be proud... if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class SnowLandscape(Place):

    def go(self, user):
        print "The white snow is tainted in red."
        next_dir = self.next_places(self, "\t 'forward' \n'left' \t\t\t\t 'right' \n\t 'backwards'", 'villa', 'forest', 'village', 'death')
        return next_dir

class Forest(Place):

    def go(self, user):
        return 'snow_landscape'

class Villa(Place):

    def go(self, user):
        next_dir = self.next_places(self, "\t 'forward' \n'left' \t\t\t\t 'right' \n\t 'backwards'", 'villa', 'forest', 'village', 'death')
        return next_dir

class Village(Place):
    # while ("bye" or "no") not in userinput:
    #     human.speak(userinput)
    #     userinput = raw_input("> ")
    def go(self, user):
        next_dir = self.next_places(self, "\t 'forward' \n'left' \t\t\t\t 'right' \n\t 'backwards'", 'park', 'police_station', 'bar', 'snow_landscape')
        return next_dir

class Bar(Place):

    def go(self, user):
        people = [Police("Benton Jacobson"), Gangster("Tom Siddal"), Citizen("Elaine Foster"), Gangster("Em Gardon"), Gangster("Henning Rodd") ]
        human = choice(people)
        print "You see someone standing at the bar, do you want to talk to the person?"
        userinput = raw_input("(yes/no)>")
        user.human.speak(userinput, human)
        print "As you leave the bar, you find a bit money: %d $." % value
        user.money += value
        print "\t You now carry %d $ with you." % user.money
        if user.money >= 2:
            engine.booth = True
        elif user.money >= 20:
            engine.ticket = True
        return 'village'

class PoliceStation(Place):

    def go(self, user):
        people = [Police("Benton Jacobson"), Police("Gideon Landen"), Citizen("Emilia Gibson"), Police("Christie Denmann"), Police("Tina Meyer") ]
        human = choice(people)
        print "You're are in front of the police station."
        print "You hear people talking about the recent murder that took place here."
        while engine.gibson == True:
            print "You go inside the police station and tell everyone about your evidence."
            print "Emil Gibson, the secret lover of Mathilda Rosa Hesse can be arrested"
            print "thanks to you. He had ties with the local gang and was a gold digger."
            print "When Mathilda Rosa Hesse didn't want to give him any money,"
            print "he killed her in his rage. Thanks to your hard work, this case is now closed."
            print "Good job, %s." % user.name
            exit(0)
        print "Want to talk to someone?"
        userinput = raw_input("(yes|no)>")
        user.human.speak(userinput, human)
        value = randint(1, 10)
        print "You go back to the main street."
        return 'village'

class Park(Place):

    def go(self, user):

        next_dir = self.next_places(self, "\t 'forward' \n\t 'backwards'", 'train_station', None, 'village', None)
        return next_dir

class TrainStation(Place):

    def go(self, user):
        return 'park'

class Train(object):
    pass

class Wagon(Train):
    pass

class WagonFinal(Train):
    pass

class Person(object):

    def __init__(self, name):
        self.name = name
        self.voc_money = "Reaction to money question."
        self.voc_name = "Reaction to name question."
        self.voc_murder = "Reaction to question about the murder."
        self.voc_gibson = "Reaction to question about Gibson."
        self.voc_error = "Reaction to unclear answer."

    # def speak(self, userinput):
    #     while ("bye" or "no") not in userinput:
    #         print "What will you ask?"
    #         userinput = raw_input ("> ")
    #         if "money" in userinput:
    #             self.money()
    #         elif "name" in userinput:
    #             print self.voc_name[randint(0, len(self.voc_name)-1)]
    #         elif "murder" in userinput:
    #             print self.voc_murder[randint(0, len(self.voc_murder)-1)]
    #             self.murder()
    #         elif "Gibson" in userinput:
    #             self.gibson()
    #         else:
    #             print self.voc_error[randint(0, len(self.voc_gibson)-1)]

    def money():
        print self.voc_money[randint(0, len(self.voc_money)-1)]

    def murder():
        pass

    def gibson():
        print self.voc_gibson[randint(0, len(self.voc_gibson)-1)]

class Police(Person):

    def __init__(self, name):
        super(Police, self).__init__(name)
        self.voc_money = [
            "Actually, I'm a undercover police officer. \nSince police officers are the role models, I will give a good example\n and give you some.",
            "Yes, I have a bit change left, that I could give you.",
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
            "Who is this? Is he connected to the murder case?"
        ]
        self.voc_error = [
            "Sorry, I couldn't hear you",
            "What did you say?",
            "What was the question again?",
            "Even though I'm a police officer I do not have superhuman hearing."
        ]

    def money():
        print self.voc_money[randint(0, len(self.voc_money)-1)]
        value = randint(1, 10)
        print "'I will give you %d $.'" % value
        User.money += value
        print "\t You now carry %d $ with you." % User.money
        if User.money >= 2:
            engine.booth = True
        elif User.money >= 20:
            engine.ticket = True

    def murder():
        print """'%sI'm taking you in for questioning as an suspect of the murder on Mathilda Rosa Hesse.
        You have the right to remain silent. If you choose to give up that right,
        anything you say can and will be used against you in a court of law.
        You have the right to speak to an attorney, and to have an attorney present during any questioning.
        If you cannot afford a lawyer, one will be provided for you at government expense.'  """ % user_name
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
        print "Good job, %s" % user_name
        exit(0)

class Gangster(Person):

    def __init__(self, name):
        super(Gangster, self).__init__(name)
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

    def money():
        print self.voc_money[randint(0, len(self.voc_money)-1)]
        print "'If you can guess correct, I will give you money.'"
        print "'We're going to do arm wrestling. Do you think you will 'win', 'lose' or play 'even'?'"
        wrestling = raw_input("> ")
        if self.strength < User.strength and wrestling == "win":
            value = randint(1, 5)
            print "'I will give you %d $. Your strength was %d and mine %d. You win.'" % (value, User.strength, self.strength)
            User.money += value
            print "\t You now carry %d $ with you." % User.money
        elif self.strength == User.strength and wrestling == "even":
            value = randint(1, 5)
            print "'Yes, we played even. I will give you %d $.'" % value
            User.money += value
            print "\t You now carry %d $ with you." % User.money
        elif self.strength > User.strength and wrestling == "lose":
            value = randint(1, 5)
            print "'I lose with %d to %d. I will give you %d $.'" % (User.strength, self.strength, value)
            User.money += value
            print "\t You now carry %d $ with you." % User.money
        else:
            print "'HAHAHA! Wrong. You get nothing!'"
        if User.money >= 2:
            engine.booth = True
        elif User.money >= 20:
            engine.ticket = True

    def gibson():
        print self.voc_gibson[randint(0, len(self.voc_gibson)-1)]
        print "You're so lucky! You ran into a gangster. He saw no other way then to keep you silent forever."
        print "%s, hurrah! You're dead, not knowing how the case will be solved." % user_name
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
            Let me guess, your name is %s. I'm %s.""" % (user_name, self.name)
        ]
        self.voc_murder = [
            "'The victim really liked reading. Her favorite book was 'Demian' by Herman Hesse'.",
            """'Everyone thought Mathilda Rosa Hesse was crazy for her obsession with this one book.
            According to rumors, even the name of her secret lover was similar to the main character.'""",
            "'I wonder what Cailyn, the assistant of Mathilda Rosa is doing. She seems to have left the village yesterday.'",
            "'If you want to know more about the victim, you should ask Cailyn. Her phone numbered ended with %s.'" % engine.number,
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
            "'What did you say?'"
        ]

class Map(object):

    places = {
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
        self.start_place = SnowLandscape()

    def next_place(self, place_name):
        val = Map.places.get(place_name)
        return val

    def opening_place(self):
        return self.next_place(self.start_place)

a_map = Map()
a_game = Engine(a_map)
a_game.begin()
