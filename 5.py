t = dict()
while True:
	s = input()
	if s == "0":
		break
	for x in s.split():
		x = x.lower()
		try:
			t[x] += 1
		except:
			t[x] = 1
#mydict.sort()
films = []
for k, v in t.items():
	films.append([v, k])
films.sort(key = lambda x : x, reverse = True)

for i in range(len(t)):
	print('"', films[i][1], '" has ', films[i][0])
