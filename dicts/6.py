def parents(d, name):
	par = []
	if name in d:
		return d[name]
	else:
		print("There is no such person!")
		return par

def grandparents(d, name):
	grand = []
	if name in d:
		for x in d[name]:
			if x in d:
				for i in d[x]:
					grand.append(i)
	else:
		print("There is no such person!")
	return grand

mydict = dict()
while True:
	x = input()
	if x == "#":
		break
	x = x.split()
	if x[0] in mydict.keys():
		mydict[x[0]] += x[1:]
	else:
		mydict[x[0]] = x[1:]
print(*parents(mydict, "Potapova"))
print(*grandparents(mydict, "Potapova"))

