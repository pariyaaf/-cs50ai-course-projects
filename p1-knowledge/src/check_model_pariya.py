from logic import *

p = Symbol("rain") # it is raining
q = Symbol("hargrid") # harry visited hargrid
t = Symbol("dumberdore") # harry visited dumberdore

sentence1 = And(p, q)
print(sentence1.formula())

sentence2 = Or(p, q)
print(sentence2.formula())
print(sentence2.symbols())

sentence3 = Not(t)
print(sentence3.formula())
print(sentence3.symbols())

# sentence1 = And(p, q)
# print(sentence1.formula())


# if isnt rain, then harry visited hargrid
# we can have all knowledge together
knowledge = And(Implication(Not(p), q),
                Or(q, t),
                Not(And(q,t)),
                t

                )

print(knowledge.formula())


# now we use checking model to check new query base our knowledge base
result01 = model_check(knowledge, p)
print(result01)

result02 = model_check(knowledge, q)
print(result02)