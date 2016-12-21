from random import randint

class Scene(object):
    def __init__(self, title, urlname, description, helptext=None):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.paths = {}
        self.help = helptext
        self.guesses = 8
        self.header= 'Gothons Of Planet Percal #25'
        self.amount = 0

    def go(self, direction):
        default_direction = None
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')
        return self.paths.get(direction, default_direction)

    def add_paths(self, paths):
        self.paths.update(paths)

code = '%d%d' % (randint(1,9), randint(1,9))
good_pod = '%d'% randint(1,5)

# Create the scenes of the game
central_corridor = Scene("Central Corridor", "central_corridor",
"""
The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew. You are the last surviving member (oh noes!) and your
last mission is to get the neutron destruct bomb from the Weapons Armory,
put it in the bridge, and blow up the ship after getting into an escape pod.

You're now running down the central corridor to the Weapons Armory when a
Gothon hops out in an evil clown costume filled with hate. He's blocking the door
to the Armory and about to pull a weapon to blast you.
""",
"""
Be fast and 'dodge!' Or you could 'tell a joke'\n
and distract the Gothon. You could also try to\n
defend yourself by shooting first, 'shoot!'
 """)

laser_weapon_armory = Scene("Laser Weapon Armory", "laser_weapon_armory",
"""
Lucky for you they made you learn Gothon insults in the academy.
You tell the one Gothon joke you know:
Lbhe zbgure vg fb sng, jura fur vfvg nebhaq gut ubhfr, fur fvgf nebhaq gut ubhfr.
The Gothon bursts into laughter and rolls around on the ground. While its
laughing you run up and use your copy of Nietzsche's notebooks (translated into Gothon)
to lecture the Gothon on the shaky foundations of its ideologies. While it tries
to cope with its existential crisis, you leap through the Weapon Armory door.

You dive roll into the Weapon Armory, crouch and scan the room for more Gothons
that might be hiding. It's dead quiet, too quiet.
You stand up and run to the far side of the room and find the neutron bomb in its
container. There's a keypad lock on the box and you need the code to get the bomb
out. If you get the code wrong 10 times then the lock closes forever and you can't
get the bomb. The code is 2 digits.
 """,
 """
 One of the digits is: %s
 """ % code#[randint(0,1)]
)

guessing = Scene("Keypad Lock", "guessing",
"""
BZZZZEDD!
The code must have been wrong, but you need the code to get the bomb
out. Remember, if you get the code wrong 10 times then the lock closes forever and you can't
get the bomb. The code is 2 digits.
""",
"""
The first digit is: %s
Code: %s
""" % (code[0], code))

the_bridge = Scene("The Bridge", "the_bridge",
"""
The container clicks open and the seal breaks, letting gas out. You grab the
neutron bomb and run like heck to the bridge where you place it in the right spot.

You burst into the Bridge with the bomb under your arm and surprise 5 Gothons
who are trying to take control of the ship. Each of them has an uglier clown costume
that the last. They don't pull their weapons out of fear that they will set off
the bomb under your arm.
""",
"""
Remember your bomb?
You can either 'throw the bomb' or
'slowly place the bomb'. Decide between
these two options.
""")

escape_pod = Scene("Escape Pod", "escape_pod",
"""
You gesture towards the bomb and threaten to set it off, the Gothons put up
their arms and ask for a truce. You inch backwards to the door, open it, and
carefully place the bomb on the floor, waving your finger over the detonate button.
Then you jump back through the door, hit the close button and zap the lock so they
can't get out. Now that the bomb is placed you run to the escape pod.

You rush through the ship desperately trying to make it to the escape pod. It seems
like there's no Gothons around, so you run as fast as possible. Eventually you reach
the room with the escape pods, and you now need to pick one to take. Some of them could
be damaged, but you don't have time to look. There's 5 pods, which one do you take?
""",
"""
Asking for help, when you just have to
choose a number between 1 and 5 seems boring.
But here you go:
%s
""" % good_pod)

shoot_death = Scene("Death...", "shoot_death",
"""
Quick on the draw you yank out your blaster and fire it at the Gothon.
His clown costume is flowing and moving around his body, which throws
off your aim. Your laser hits his costume but misses him entirely. This
completely ruins his brand new costume his mother bought him, which
makes him fly into an insane rage and blast you repeatedly in the face until
you are dead. Then he eats you.
""")

dodge_death = Scene("Death...", "dodge_death",
"""
Like a world class boxer you dodge, weave, slip and slide right
as the Gothon's blaster cranks a laser past your head.
In the middle of your artful dodge your foot slips and you
bang your head on the metal wall and pass out.
You wake up shortly after only to die as the Gothon stomps on
your head and eats you.
""")

code_death = Scene("Death...", "code_death",
"""
The lock buzzes one last time and then you hear a sickening
melting sound as the mechanism is fused together.
You decide to sit there, and finally the Gothons blow up the
ship from their ship and you die.
""")

throw_death = Scene("Death...", "code_death",
"""
In a panic you throw the bomb at the group of Gothons
and make a leap for the door. Right as you drop it a
Gothon shoots you right in the back killing you.
As you die you see another Gothon frantically try to disarm
the bomb. You die knowing they will probably blow up when
it goes off.
""")

the_end_winner = Scene("You Made It!", "the_end_winner",
"""
You jump into pod %s and hit the eject button. The pod flies out into space heading
to the planet below. As you're heading down, you look back and see your ship implode
and then explode like a supernova, taking down the Gothon ship at the same time.
You made it!
""" % good_pod)

the_end_death = Scene("...", "the_end_death",
"""
You jump into a random pod and hit the eject button. The pod escapes into space
but there's a crack in the hull. Uh oh. The pod implodes and you with it.
""")

# Define the action commands available in each scene
escape_pod.add_paths({
    good_pod: the_end_winner,
    '*': the_end_death
})

the_bridge.add_paths({
    'throw the bomb': throw_death,
    'slowly place the bomb': escape_pod
})

laser_weapon_armory.add_paths({
    code: the_bridge,
    '*': guessing
})

guessing.add_paths({
    code: the_bridge,
    '*': code_death
})

central_corridor.add_paths({
    'shoot!':shoot_death,
    'dodge!':dodge_death,
    'tell a joke': laser_weapon_armory
})

# Make some useful variables to be used in the web application
SCENES = {
    central_corridor.urlname: central_corridor,
    laser_weapon_armory.urlname: laser_weapon_armory,
    the_bridge.urlname : the_bridge,
    escape_pod.urlname : escape_pod,
    the_end_winner.urlname : the_end_winner,
    the_end_death.urlname : the_end_death,
    shoot_death.urlname : shoot_death,
    dodge_death.urlname : dodge_death,
    throw_death.urlname : throw_death,
    guessing.urlname : guessing
}
START = central_corridor
