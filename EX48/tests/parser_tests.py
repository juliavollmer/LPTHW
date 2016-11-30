## I don't really know how to do this

from nose.tools import *
from ex48 import parser

def test_subj():
    assert_equal(parse_verb(('verb', 'run'), 'run')
    print "Running setup for automated tests!"

def test_sentence():
    trysen = parse_sentence([('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')])
    assert_equal(trysen, [()])
    print "Running teardown for automated tests!"

def test_obj():
    print "Running the first and only automated test!"

def test_verb():
    pass
