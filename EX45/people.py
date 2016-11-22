class Person(object):

    def __init__(self, name):
        self.name = name
        self.voc_money = "Reaction to money question."
        self.voc_name = "Reaction to name question."
        self.voc_murder = "Reaction to question about the murder."
        self.voc_gibson = "Reaction to question about Gibson."
        self.voc_error = "Reaction to unclear answer."

    def money(self):
        print self.voc_money[randint(0, len(self.voc_money)-1)]

    def murder(self):
        pass

    def gibson(self):
        print self.voc_gibson[randint(0, len(self.voc_gibson)-1)]
