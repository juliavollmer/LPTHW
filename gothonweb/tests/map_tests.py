from nose.tools import *
from map1 import *

def test_scene():
    gold = Scene("GoldScene", "goldroom",
                """This room has gold in it you can grab. There's a
                door to the north.""", "Help")
    assert_equal(gold.title, "GoldScene")
    assert_equal(gold.urlname, "goldroom")
    assert_equal(gold.paths, {})
    assert_equal(gold.help, "Help")

def test_scene_paths():
    center = Scene("Center", "center", "Test scene in the center.", None)
    north = Scene("North", "north", "Test scene in the north.", None)
    south = Scene("South", "south", "Test scene in the south.", None)

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Scene("Start", "start", "You can go west and down a hole.", None)
    west = Scene("Trees", "Trees", "There are trees here, you can go east.", None)
    down = Scene("Dungeon", "dungeon", "It's dark down here, you can go up.", None)

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)

def test_gothon_game_map():
    assert_equal(START.go('shoot!'), shoot_death)
    assert_equal(START.go('dodge!'), dodge_death)
    room = START.go('tell a joke')
    assert_equal(room, laser_weapon_armory)
    assert_equal(room.go('*'), guessing)

    assert_equal(guessing.go(code), the_bridge)
    second = room.go(code)
    assert_equal(second, the_bridge)
    assert_equal(second.go("throw the bomb"), throw_death)

    third = second.go('slowly place the bomb')
    assert_equal(third, escape_pod)
    assert_equal(third.go(good_pod), the_end_winner)
    assert_equal(third.go('*'), the_end_loser)
