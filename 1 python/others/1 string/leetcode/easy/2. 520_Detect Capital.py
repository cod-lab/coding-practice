def method1(word: str) -> bool:			# most efficient in both TC & SC among all below methods
	# if not word: return 0
	l=len(word)
	if l==1 : return 1

	if ord(word[0])	>= 97:		# first letter small
		for i in range(1,l):	# from second letter
			if ord(word[i]) <= 90: return 0
		return 1

	# else		first letter capital
	if ord(word[1])	>= 97:		# second letter small
		for i in range(2,l):	# from third letter
			if ord(word[i]) <= 90: return 0
		return 1

	# else		second letter also capital
	for i in range(2,l):	# from third letter
		if ord(word[i]) >= 97: return 0
	return 1


def method2(word: str) -> bool:			# least efficient among all methods
	l=len(word)
	if l==1 : return 1

	if ord(word[0])	>= 97:		# first letter small
		for i in range(1,l):	# from second letter
			if ord(word[i]) <= 90: return 0
		return 1

	# else		first letter capital
	c=1
	for i in range(1,l):
		# print(c,word[i])
		if ord(word[i]) <= 90: c+=1

	# print(c)
	if c==1 or c==l: return 1
	return 0


def method3(word: str) -> bool:			# slower than method1 and faster than method2
	l=len(word)
	if l==1 : return 1
	
	c=0
	for i in range(1,l):
		if ord(word[i]) <= 90: c+=1

	if ord(word[0])	<= 90 and (c==0 or c==l-1): return 1
	if ord(word[0]) >=97 and c==0: return 1
	return 0



word=[]
word += ["ab"]
word += ["aB"]
word += ["abc"]
word += ["leetcodE"]
word += ["Google"]
word += ["FlaG"]
word += ["USA"]

# print(word)
for i in range(len(word)):
	# print("\n",i,method1(word[i]))
	# print("\n",i,method2(word[i]))
	print("\n",i,method3(word[i]))

