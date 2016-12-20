#
from random import randint

class Scene(object):
    def __init__(self, title, urlname, description, helptext):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.paths = {}
        self.help = helptext
        self.guesses = 8
        self.header= 'Murder at Night'

    def go(self, direction):
        default_direction = None
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')
        return self.paths.get(direction, default_direction)

    def add_paths(self, paths):
        self.paths.update(paths)

code = '%d%d%d' % (randint(1,9), randint(1,9), randint(1,9))
good_pod = randint(1,5)

# Create the scenes of the game
SnowLandscape = Scene("A Snowy Place at Night", "snow_landscape",
 """
The white snow is tainted in red... You know what it is.
You standing in the middle of this wide white landscape. In front of you you can
spot a huge mansion in the distance. On your right is a dark forest
and behind you is a path leading to a small village.
""",
"""
HELP
""")

forest = Scene("The Forest", "forest",
"""
The forest is dark. As you look for a path, you get frighten by the view in front of you.
There is a corpse. Blood. And you have blood on your hand...
 """,
 """
 There is nothing else to do.
 Go 'back'.
 """
)

villa = Scene("The Huge Mansion", "villa",
"""
You enter the huge mansion. Judging from the interior, the owner must be really rich.
Oh... There is a blood trail going from the entrance to another room. You follow it.
The blood trail stops in what seems to be the study. This must have been the crimescene.
"""
"""
You're done with investigating.
Go 'back'.
""")

village = Scene("The Village", "village",
"""
"The village is in an uproar. In the forest near the village someone found a corpse.
print "Mathilda Rosa Hesse, a bestseller author was murdered and you're the prime suspect!
self.items(Item("Book", "Someone forgot it here. 'Demian' by Hermann Hesse. \nIt tells the story of Emil Sinclair, who is taught by Max Demian to look at things in a different way.", 4),
Item("Teabox", "Mrs Hesse really like drinking tea.", 0),
Item("Shoe", "Someone lost a really nice looking shoe. Seems the person was in a hurry.", 1))
print "If you follow the main street, you would reach the Sunnyhill park.
print "But maybe you would rather visit the bar on your left or the police station opposite of it?
"""
)

bar = Scene("The Night Bar Night", "bar",
"""
You see someone standing at the bar, do you want to talk to the person?
""")

speaking = Scene("Conversation", "speaking",
"""
%s
""" % person)


# Define the action commands available in each scene

bar.add_paths({
    "go out": village
})

village.add_paths({
    "go to park": park,
    "go inside the bar": bar,
    "go to the police station": police_station,
    "go back": snow_landscape
})

snow_landscape.add_paths({
    'got to mansion': villa,
    'go to forest': forest,
    'go to village': village,
    '*': death
})

villa.add_paths({
    'back': snow_landscape
})

forest.add_paths({
    'back': snow_landscape
})
# Make some useful variables to be used in the web application
SCENES = {
    snow_landscape.urlname: snow_landscape,
    forest.urlname: forest,
    villa.urlname : villa,

    guessing.urlname : guessing
}
START = home
