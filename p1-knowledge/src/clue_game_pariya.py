import termcolor
from logic import *


mustard = Symbol("ColMustard")
plum = Symbol("ProfPlum")
scarlet = Symbol("MsScarlet")
characters = [mustard, plum, scarlet] # list

ballroom = Symbol("ballroom")
kitchen = Symbol("kitchen")
library = Symbol("library")
rooms = [ballroom, kitchen, library]

knife = Symbol("knife")
revolver = Symbol("revolver")
wrench = Symbol("wrench")
weapons = [knife, revolver, wrench]

symbols = characters + rooms + weapons # list


# func to check symbol with knowledge
def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: YES", "green")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: MAYBE")


# knowledge


# base knowledge
knowledge = And(Or(mustard, plum, scarlet),
                Or(kitchen, library, ballroom),
                Or(knife, revolver, wrench)
    )

print(knowledge.formula())
check_knowledge(knowledge)

print('_'*100)



knowledge.add(Not(mustard))
knowledge.add(Not(kitchen))
knowledge.add(Not(revolver))
# initial knowledge
knowledge.add(Or(Not(scarlet), Not(library), Not(wrench)))

# card knowledge
knowledge.add(Not(ballroom))
knowledge.add(Not(plum))

# Known cards

print(knowledge.formula())
check_knowledge(knowledge)


