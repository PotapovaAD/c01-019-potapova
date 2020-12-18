a = list(map(int, input().split()))
b = list(map(int, input().split()))

X = Y = Z = set()
for q in a:
	X.add(q)
for q in b:
	Y.add(q)
Z = X.union(Y)

print(len(X))
print(len(Y))
print(len(Z))
