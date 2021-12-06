# without using stack, Avg TC & SC
def method1(s: str) -> bool:
	print("s: %s\n" % (s))
	size = len(s)
	if size%2 != 0: return False

	# l=[["(",")"],["[","]"],["{","}"]]
	d={"(":")","[":"]","{":"}"}
	i=0
	# for _ in range(size):
	while(s):
		while i<len(s) and (s[i] == "(" or s[i] == "[" or s[i] == "{"):
			print(i,s[i])
			i+=1
		if i==0 or i==len(s): return False
		# if (s[i] == ")" and s[i-1] == "(") or (s[i] == "]" and s[i-1] == "[") or (s[i] == "}" and s[i-1] == "{"):
		# if [s[i-1],s[i]] in l:
		if d[s[i-1]] == s[i]:
			print("\t",i,s[i-1],s[i])	
			s = s[:i-1] + s[i+1:]
			i-=1
			# del(s[i-1],s[i])
			# s.remove(s[i-1])
			# s.remove(s[i])
		else: return False
		print("\t\ts: ",s)
		# if i==-1: return True

	return True





s = ["()"]
s += ["{{)"]
s += ["()[]{}"]
s += ["(]"]
s += ["([)]"]
s += ["{[]}"]
s += ["[][]"]
s += ["((()(())))()()(("]
s += ["((()(())))()())("]
s += ["((()(())))()()))"]

for i in range(len(s)):
	print(method1(s[i]),"\n","-"*70)



