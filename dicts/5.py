mydict = dict()
while True:
	s = input()
	if s == "#":
		break
	for x in s.split():
		x = x.lower()
		try:
			mydict[x] += 1
		except:
			mydict[x] = 1
f = []
for k, v in mydict.items():
	f.append([v, k])
f.sort(key = lambda x : x, reverse = True)

for i in range(len(mydict)):
	print('"', f[i][1], '" has ', f[i][0])
