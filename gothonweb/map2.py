#
from random import randint
import time

class Scene(object):
    def __init__(self, title, urlname, description, helptext=None, amount=0):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.paths = {}
        self.help = helptext
        self.guesses = 5
        self.header= 'Roadtrip'
        self.amount = amount

    def go(self, direction):
        default_direction = None
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')
        return self.paths.get(direction, default_direction)

    def add_paths(self, paths):
        self.paths.update(paths)


password = time.strftime("%d%m")
good_truck = str(randint(1,6))

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
You're on a road. Since you don't have enough money left, there is only one solution.
You raise your hand and pull out your thumb. You have never done hitchhiking before,
but that should change now.
... You wait...
... And you wait...
There is no car in sight and it will only take a few minutes before you will give up and return home.
But hey! It seems you got lucky. The moment you want to move away, you see a car and a truck approaching.
""", "Two options: 'go to car' or 'go to truck'.")

accident_death = Scene("Crash...", "accident_death",
"""
You wave your hands vividly in the direction of the car. As it gets closer, you run towards it.
Bad idea. Really really bad idea.
The car, without slowing down, takes you down and before you know it, you lie in a puddle of red.
Thankfully you don't have to wait for the ambulance as long as you did for the car.
Whether you like it or not, you have to spend the rest of your vacation at the hospital. Reaaaally nice food inclusive.
What a luxury!
""")

truck = Scene("Donny's Truck", "truck",
"""
You ask the truck driver for a drive. He seems nice and immediately agrees to take you a bit with him.
His name is Donny and he designed the interior of the truck himself in order to feel more at home.
There is some soft fabric on the seats and the curtain is in a nice red color.
After you drove like one hour, the truck enters a remote area. The darkness greets as far as you can see.
You can see Donny sweating and getting more shaken and impatient. Something is wrong...
""",
"""
Should you 'ask him about it' or 'immediately escape'?
""")

escape_death = Scene("Remote area", "escape_death",
"""
You sense some danger and in the momemt Donny pulls the truck over to a dark parking lot near a forest,
you open the door and try to escape. He seemed to be up to nothing good.
As you run you see Donny's face turning from confusion to anger.
"So that's how you thought of me and thank me! I won't take someone like you any longer with me!"
He yells at you and you stop, only to see how Donny goes into the forest, presumingly for urinating.
Congratulations, you upsetted the only person far and wide, who could have gotten you outside this area.
How nice of you!
""")

reststop = Scene("Reststop 'Spacelounge'", "reststop",
"""
You ask him directly what's up. He's a nice guy and something is definitely wrong, you just can't make out what it is.
He then tells you:
"I was kinda ashamed to admit it in front of a stranger, but I really need to go to a restroom... And you know... The bigger one."
You're shocked by his confession, but then gladly help to look for a reststop.
At the reststop Donny excuses himself and you take a stroll. Too bad, you didn't paid much attention.
When you come back all the trucks look so similar and you can't spot Donny. You should just go to one of the 6 trucks.
""",
"""
The first truck looks comfy, another one black and number %s allows a view at the red curtains.
""" % good_truck)

truck2 = Scene("Donny's Truck", "truck2",
"""
Great, you found Donny's truck. How could you forget his red interior (He later told you, it was the favorite color of his dead wife).
Donny journey ends in the next biggest city and you decide to spend your night there.
""", "'okay'")

reststop_death = Scene("Reststop 'Spacelounge'", "reststop_death",
"""
Oh man. You just went into the wrong truck. The driver wasn't so amused and insulted you heavily.
This traumatized you so much that you go back home and curl yourself up in your bed. The blankets shield you from the outside world.
""")

city = Scene("Big rustling City", "city",
"""
Before the trip you looked up some people on Couchsurfing, but right in front of you is also a nice bridge.
You could be adventurous and enjoy the night view.
Or maybe you can go to this restaurant. Before they close, they could need some help.
""",
"""
'try couchsurfing', 'go underneath the bridge' or to the restaurant and
'earn money'.
""")

couchsurfing = Scene("Stranger's House", "couchsurfing",
"""
You pull out the note with the adress you got from Couchsurfing and go there.
This nice lady opens the door for you. She seems happy and joyful and in celebration mode. "Come in. Come in. The more, the merrier."
You follow the invitation and enter the house. "All my friends are already here. The house is packed with people, I'm sorry."
"But you will still fit in." She gestures towards the rooms, but you see no one.
Something is strange... She smiles and smiles and then goes to the kitchen. She then comes out again with a knife.
"While I was slicing the cake I noticed it's not enough to feed everyone. I will go the backery and be back soon."
The door closes behind her and you see $10 lying on the ground and pick it up to give it to here, but she just answers it doesn't matter,
it will eventually be hers again. You become anxious. It would be better to leave.
But no! The door has a HOUSEPROTECTORv0.1 that requires a four digit password.
All the more reasons to get outta here!!!
""",
"Try it at least once without help.", 10)

guessing = Scene("HOUSE PROTECTOR v0.1", "guessing",
"""
-WRONG PASSWORD-
-AFTER 5 TRIES THE HOUSEOWNER WILL BE NOTIFIED-
-FEEL SAFE AT HOME, WITH THE HOUSEPROTECTORv0.1-
You need to get out here, as fast as possible! The nights darken and who knows, when the creep will find you!
""",
"""
Try to remember your meeting with the houseowner. There should have been some hints. %s
""" % code
)

code_death = Scene("ALARM - HOUSEPROTECTORv0.1", "code_death",
"""
As soon as you pressed enter for the last time, you knew it was over for you.
The alarm signal goes off and when you look back, your eyes meet hers. Her smile seems angelic,
but you know it is more of an diabolic grin. "Why do you wanna leave?" she softly whispers in my ear.
"Stay!"
Your vacation come to an end and so did your life. You now hang out with other corpses under the floorboard.
At least you have some company.
""")

dishes = Scene("Restaurant Galactical Dining", "dishes",
"""
Inside the restaurant you notice that help is much needed and appreciated. You take inniative and help out with the dishes.
You earn yourself $5 for your vacation.
""", "'back'", 5)

under_bridge = Scene("Blue Moon Bridge", "under_bridge",
"""
The bridge's reflection on the water looks stunning. You see newspaper lying around and you imagine how comfy it would actually be.
Near the water some people made a bonfire.
""",
""""
Just go to 'sleep' covered with the newspaper or 'read newspaper'.
Maybe you want to 'sit at the fire'.
""")

newspaper = Scene("Newspaper Milky Way", "newspaper",
"""
You read the newspaper and see an ad looking for people, who could help out with some night experiment.
Even though it sounds sketchy, you decide to do it, the pay is just too good.
After you underwent a number of tests concerning the night vision, you finally receive the pay of $30.
""", "Let's go 'back'.", 30)

fire_death = Scene("Bonfire", "fire_death",
"""
The fire warms you for a moment til it slowly gets smaller. Everyone gets busy, to get the fire started again.
It seems no one has really a clue how it works and so, after some guy thought deodorant is a good idea, you all end up
with nice 2nd degree burns. Hospital! Here you come!
""")

money = Scene("Bonanza", "money",
"""
As you slept under the beautiful night sky outside, covered with a newspaper, you reminscince about the beauty of life.
Every given moment is so valuable that you feel at ease and sleep pretty well at an unfamiliar place.
The closeness to nature makes you happy and you now can say that this free vacation was useful.
And there is also a positive side effect. When you wake up you find money next to you. People must have mistaken you for a beggar.
Thanks for the $5 nice stranger!
""", "'back'.", 5)

the_end_winner = Scene("Ticket Home", "the_end_winner",
"""
Vacation couldn't be any better. You have enough money to buy a ticket back home.
Well done! This trip had a cool adventurous vibe to it.
""")
newspaper.add_paths({
    'back': under_bridge
})

money.add_paths({
    'back': under_bridge
})

dishes.add_paths({
    'back': city
})

home.add_paths({
    'destroy the piggy bank': piggy_death,
    'go nonetheless': hitchhiking
})

hitchhiking.add_paths({
    'go to truck': truck,
    'go to car': accident_death
})

truck.add_paths({
    'ask him about it': reststop,
    'immediately escape': escape_death
})

reststop.add_paths({
    good_truck: truck2,
    '*': reststop_death
})

truck2.add_paths({
    'okay': city
})

city.add_paths({
    'try couchsurfing': couchsurfing,
    'go underneath the bridge': under_bridge,
    'earn money': dishes
})

couchsurfing.add_paths({
    code: city,
    '*': guessing
})
guessing.add_paths({
    password: city,
    '*': code_death
})

under_bridge.add_paths({
    'read newspaper': newspaper,
    'sleep': money,
    'sit by the fire': fire_death
})

# Make some useful variables to be used in the web application
SCENES = {
    home.urlname: home,
    piggy_death.urlname: piggy_death,
    hitchhiking.urlname: hitchhiking,
    truck.urlname: truck,
    escape_death.urlname: escape_death,
    accident_death.urlname: accident_death,
    dishes.urlname: dishes,
    city.urlname: city,
    reststop.urlname: reststop,
    reststop_death.urlname: reststop_death,
    couchsurfing.urlname: couchsurfing,
    code_death.urlname: code_death,
    under_bridge.urlname: under_bridge,
    newspaper.urlname: newspaper,
    money.urlname: money,
    fire_death: fire_death,
    the_end_winner.urlname: the_end_winner,
    guessing.urlname: guessing,
    truck2.urlname: truck2
}
START = home
