#
from random import randint

class Scene(object):
    def __init__(self, title, urlname, description, helptext):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.paths = {}
        self.help = helptext
        self.guesses = 6
        self.header= 'Roadtrip'

    def go(self, direction):
        default_direction = None
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')
        return self.paths.get(direction, default_direction)

    def add_paths(self, paths):
        self.paths.update(paths)

code = '%d%d%d' % (randint(1,9), randint(1,9), randint(1,9))
good_truck = randint(1,6)

# Create the scenes of the game
home = Scene("Your Home", "home",
 """
Finally you have time for a vacation.
But when you check your finances you realise that it might not happen at all.
You look around and spot your piggy bank.
 """,
 """
You could 'destroy the piggy bank', there might be some small change left.
Or 'go nonetheless' on a moneyfree journey.
 """)

piggy_death = Scene("Killing the Piggy Bank", "piggy_death",
"""
You take the next heavy item you can see and smash it on the poor piggy's head.
Karma must not be on your side. Due to your great determination, you used too much strength
and the piggy bank bursted, splitter flying everywhere. Eventually a piece lands in your eye.
Seems now you should use money on a oculist rather than going on vacation.
"""
)

hitchhiking = Scene("Road at Night", "hitchhiking",
"""
You’re on a road. Since you don’t have enough money left, there is only one solution.
You raise your hand and pull out your thumb. You have never done hitchhiking before,
but that should change now.
… You wait…
… And you wait…
There is no car in sight and it will only take a few minutes before you will give up and return home.
But hey! It seems you got lucky. The moment you want to move away, you see a car and a truck approaching.
""")

truck = Scene("Donny's Truck", "truck",
"""
You ask the truck driver for a drive. He seems nice and immediately agrees to take you a bit with him.
His name is Donny and he designed the interior of the truck himself in order to feel more at home. There is some soft fabric on the seats and the curtain is in a nice red color.
After you drove like one hour, the truck enters a remote area. You can see Donny sweating and getting more shaken and impatient. Something is wrong…
""")

reststop = Scene("Reststop 'Spacelounge'", "reststop",
"""
You ask him directly what’s up. He’s a nice guy and something is definitely wrong, you just can’t make out what it is.
He then tells you: “I was kinda ashamed to admit it in front of a stranger, but I really need to go to a restroom… And you know… The bigger one.”
You’re shocked by his confession, but then gladly help to look for a reststop.
At the reststop Donny excuses himself and you take a stroll. Too bad, you didn’t paid much attention.
When you come back all the trucks look so similar and you can’t spot Donny. You should just go to one of the 6 trucks.
""")

city = Scene("Big rustling City", "city",
"""
Great, you found Donny’s truck. How could you forget his red interior (He later told you, it was the favorite color of his dead wife).
Donny journey ends in the next biggest city and you decide to spend your night there.
""")

guessing = Scene("Keypad Lock", "guessing",
"""
BZZZZEDD!
The code must have been wrong, but you need the code to get the bomb
out. Remember, if you get the code wrong 10 times then the lock closes forever and you can't
get the bomb. The code is 3 digits.
""",
"""
The first digit is: %s
""" % code[0]

home.add_paths({
    'destroy the piggy bank': piggy_death,
    'go nonetheless': hitchhiking
})

guessing.add_paths({
    code: the_bridge,
    '*': code_death
})

hitchhiking.add_paths({
    'go to truck': truck,
    'go to car': accident_death
})

truck.add_paths({
    'ask him about it': reststop,
    'immediatly escape': escape_death
})

reststop.add_paths({
    good_truck: city,
    '*': reststop_death
})

city.add_paths({
    couchsurfing,
    under_bridge,
    dishes
})
# Make some useful variables to be used in the web application
SCENES = {
    home.urlname: home,
    piggy_death.urlname: piggy_death,
    hitchhiking.urlname: hitchhiking,
    truck.urlname: truck,
    escape_death.urlname: escape_death,
    accident_death.urlname: accident_name,
    dishes.urlname: dishes,
    city.urlname: city,
    reststop.urlname: reststop,
    reststop_death.urlname: reststop_death,
    couchsurfing.urlname: couchsurfing,
    house_death.urlname: house_death,
    under_bridge.urlname: under_bridge,
    escape_pod.urlname: escape_pod,
    the_end_winner.urlname: the_end_winner,
    guessing.urlname: guessing,
    space_winner.urlname: space_winner
}
START = home
