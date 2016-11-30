lexicon = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back',
            'go', 'stop', 'kill', 'eat',
            'the', 'in', 'of', 'from', 'at', 'it',
            'door', 'bear', 'princess', 'cabinet']

def scan(userinput):
    words = userinput.split()
    result = []
    for word in words:
        result.append(classify(word))
    return result

def classify(word):
    # test if word is a direction
    #if so return ('direction', word)
    if word in ['north', 'south', 'east']:
        return ('direction', word)
    # test if word is a verb
    #if so return ('verb', word)
    elif word in ['go', 'kill', 'eat',]:
        return ('verb', word)
    # test if word is a stop
    #if so return ('stop', word)
    elif word in ['the', 'in', 'of']:
        return ('stop', word)
    # test if word is a noun
    #if so return ('noun', word)
    elif word in ['bear', 'princess']:
        return ('noun', word)
    # test if word is a number
    #if so return ('number', word)
    else:
        try:
            thenumber = int(word)
            return ('number', thenumber)
        except ValueError:
            # word is not a number
            return ('error', word)
