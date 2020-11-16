s = set()
while True:
	x = int(input())
	if x == 0:
		break
	if x in s:
		print("Число уже встречалось")
	else:
		print("Число не встречалось")
		s.add(x)
