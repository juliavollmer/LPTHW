
from nose.tools import *
from ex48.parser import *

def test_sentence():
    trysen = parse_sentence([('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')])
    assert_equal(trysen.subject, 'bear')
    assert_equal(trysen.verb, 'eat')
    assert_equal(trysen.object, 'honey')
