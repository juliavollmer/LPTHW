from nose.tools import *
from app import app
from tests.tools import assert_response
from map1 import code

client = app.test_client() # create a testing client (like a fake web browser)
client.testing = True # enable this so that errors in your web app bubble up to the testing client

def test_index():
    global client
    resp = client.get("/") # with this client you can do all kinds of stuff
    assert_response(resp, status=302) # the root url should give back a redirect

    resp = client.get("/game")
    assert_response(resp) # valid response
    resp = client.post('/game') #POST, but provide no data
    assert_response(resp, contains="You died!")

    #Go to another scene
    testdata = {'userinput': 'tell a joke'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Laser Weapon Armory")

    #from there go to yet another scene
    testdata = {'userinput': code}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains='The Bridge')
