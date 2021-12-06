# without using stack, 99% efficient in both TC & SC
def method1(s: str) -> bool:
	print("s: %s\n" % (s))
	if not s: return False

	# size = len(s)			✓
	if len(s)%2 != 0: return False

	# l=[["(",")"],["[","]"],["{","}"]]			✓
	d={"(":")","[":"]","{":"}"}
	i=0
	while(s):
		while i<len(s) and (s[i] == "(" or s[i] == "[" or s[i] == "{"):
		# while i<size and s[i] in d.keys():		✓
			# print(i,s[i])
			i+=1
		if i==0 or i==len(s): return False
		# if (s[i] == ")" and s[i-1] == "(") or (s[i] == "]" and s[i-1] == "[") or (s[i] == "}" and s[i-1] == "{"):		✓
		# if [s[i-1],s[i]] in l:		✓
		if d[s[i-1]] == s[i]:
			# print("\t",i,s[i-1],s[i])	
			s = s[:i-1] + s[i+1:]
			# size-=2					✓
			i-=1
			# del(s[i-1],s[i])			X
			# s.remove(s[i-1])			X
			# s.remove(s[i])			X
		else: return False
		# print("\t\ts: ",s)
		# if i==-1: return True			X

	return True


# using stack, least efficient(below 10%) in both TC & SC
def method2(s: str) -> bool:
	print("s: %s\n" % (s))
	if not s: return True

	if len(s)%2 != 0: return False

	d={"(":")","[":"]","{":"}"}
	stack=[]
	i=0
	while i<len(s):
	# for _ in s:					X
		# while c in d.keys():		X
		# if s[i] in d.keys():		✓
		if s[i] == "(" or s[i] == "[" or s[i] == "{":
			stack += s[i]
			# print("1 ",i,stack)
			i+=1
		elif i==len(s) or len(stack)==0: return False
		elif d[stack[-1]] == s[i]:
			stack = stack[:-1]
			# print("2 ",i,stack)
			i+=1
		else: return False
		# i+=1						✓

	# return True  					X
	# return len(stack) == 0		✓
	return not stack


# using stack, least efficient(below 10%) in both TC & SC
def method3(s: str) -> bool:
	print("s: %s\n" % (s))
	if not s: return True

	if len(s)%2 != 0: return False

	d={"(":")","[":"]","{":"}"}
	stack=[]
	for c in s:
		# if c in d.keys():		✓
		if c == "(" or c == "[" or c == "{":
			stack += [c]
		elif len(stack)!=0 and d[stack[-1]] == c:
			stack = stack[:-1]
		else: return False

	# return len(stack) == 0		✓
	return not stack



s = ["()"]
s += ["{{)"]
s += ["()[]{}"]
s += ["(]"]
s += ["([)]"]
s += ["{[]}"]
s += ["[][]"]
s += ["((()(())))()()"]
s += ["((()(())))()()(("]
s += ["((()(())))()())("]
s += ["((()(())))()()))"]
s += ["[[[]"]


for i in range(len(s)):
	print(method1(s[i]),"\n","-"*30)
	# print(method2(s[i]),"\n","-"*30)
	# print(method3(s[i]),"\n","-"*30)



