from logic import  *

people = ["Gilderoy", "Pomona", "Minerva", "Horace"]
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]


symbols = []
knowledge = And()


# symbols - p1
# exp : GlideroyGryffindor
for person in people:
    for house in houses:
        symbols.append(Symbol(f"{person}{house}"))

# base knoledge - p1
for person in people:
    knowledge.add(Or(
        Symbol(f"{person}Gryffindor"),
        Symbol(f"{person}Hufflepuff"),
        Symbol(f"{person}Ravenclaw"),
        Symbol(f"{person}Slytherin"),
    ))

# print('knowledge-p1:', knowledge.formula())
# print('_'*90)



# base knoledge - p2
# only one house per person
for person in people:
    for h1 in houses:
        for h2 in houses:
            if h1 != h2:
                knowledge.add(
                    Implication(Symbol(f"{person}{h1}"), Not(Symbol(f"{person}{h2}")))
                )


# print('knowledge-p2:', knowledge.formula())
# print('_'*90)



# base knoledge - p3
# only one person per houses
for house in houses:
    for p1 in people:
        for p2 in people:
            if p1 != p2:
                knowledge.add(
                    Implication(Symbol(f"{p1}{house}"), Not(Symbol(f"{p2}{house}")))
                )


# print('knowledge-p3:', knowledge.formula())
# print('_'*90)



# our knowledge

knowledge.add(Or(Symbol("GilderoyGryffindor"), Symbol("GilderoyRavenclaw")))

knowledge.add(Not(Symbol("PomonaSlytherin")))

knowledge.add(And(Symbol("MinervaGryffindor")))

# print('final knowledge:', knowledge.formula())
# print('_'*90)

# use check model to check each symbols for this knewledge base
for symbol in symbols:
    if model_check(knowledge, symbol):
        print(symbol)