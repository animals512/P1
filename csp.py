import itertools
variables=["A","B","C"]
colors=["Red","Blue","Yellow"]
all_assignments=itertools.product(colors, repeat=len(variables))

def valid (i):
	A,B,C=i
	return (A!= B) and (B!= C) and (A!= C)
solutions =[]
for i in all_assignments:
	if valid(i):
		solutions.append(dict(zip(variables, i)))
print("Valid coloring of the map: ")
for sol in solutions:
	print(sol)
