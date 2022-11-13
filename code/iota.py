#a valid iota string is either "1" or of the form "0" + x + y where x,y are shorter iota strings
#we see that each iota string has one more 1's than it has 0's. in particular, the length of an iota string is odd
#moreover, the number of iota strings with n 0's is known as the Catalan number of order n.
#to each iota string we form a bracketed expression in the symbols (,*,) as follows:
# rep(iota_string) = 
# iota_string = "1" -> "*"
# iota_string = "0" + x + y -> "(<f(x)><f(y)>)" 
#for example, "011" -> (**) and "01011" -> (*(**)) and 0011011 -> ((**)(**)) and (*((**)*)) is mapped from 0100111
#this function efficiently computes the bracketed expression of an iota string, and outputs None if its input is not a valid iota string
def iota(string):
	#verifying string is not empty and contains only 0s and 1s

	for x in string:
		if x not in ['0','1']:
			return None

	if string == "":
		return None

	#we pass through the string once from start to finish. a bracket opens when we see a 0. when we see a one we write * and think of it as an input to the last opened bracket. 
	#[each bracket needs to inputs, which can be two simple *'s to create (**) or more complicated *,(**) to create (*(**))] 
	#when a bracket receives two inputs it is closed, and its value is then an input to the bracket that opened before it.
	#the stack contains for each bracket that has opened and not closed yet the number of inputs (each bracket needs two items) we've created thus far.
	#when a bracket opens, i.e. when we see a zero, a 0 is pushed to the stack. when we see a 1, it represents an input, and if the number of inputs from the last
	#open bracket was already 1, we can close the bracket (pop the top of the stack) and add one input to the bracket before
	stack = []
	expression = ""
	i = 0
	for x in string:
		if x == '0':
			stack.append(0)
			expression += "("

		else:	#x == '1'
			expression += "*"
			
			while len(stack) > 0 and stack[-1] == 1:
				stack.pop()
				expression += ")"

			if len(stack) == 0: #stack is empty, check if remainder of string is too
				if not (i==len(string)-1):
					return None
			else: #stack is not empty, and its top entry is 0
				stack[-1] = 1
		i += 1

	if not (len(stack)==0):
		return None

	return expression


#test
#	generate all binary words of length up to 10 
#	and print the valid iota words with their expressions
#
#d = {0: [""]}
#for i in range(10):
#	d[i+1] = []
#	for w in d[i]:
#		d[i+1].append(w+"0")
#		d[i+1].append(w+"1")
#
#for a in d:
#	for w in d[a]:
#		y = iota(w)
#		if y != None:
#			print(f"{w} {y}")
