learners_french = input().split()
pianists = input().split()
swimmers = input().split()
X = Y = Z = set()
for a in learners_french:
	X.add(a)
for b in pianists:
	Y.add(b)
for c in swimmers:
	Z.add(c)
L = set()
L = (Y.intersection(Z)).difference(X)
result = []
for x in D:
	result.append(x)
print(*result)
