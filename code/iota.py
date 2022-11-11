#a valid iota string is either "1" or of the form "0" + x + y where x,y are shorter iota strings. for example "011" is a valid iota string. so are "00111" and "01011".
#we can see that each iota string has one more 1's than it has 0's. in particular, the length of an iota string is odd.
#moreover, the number of iota strings with n 0's is known as the Catalan number of order n.
#to each iota string we correspond a (well bracketed) expression in the symbols (,*,) as follows:
# exp(iota_string) = 
# iota_string = "1" -> "*"
# iota_string = "0" + x + y -> "(<exp(x)><exp(y)>)" 
#for example, "011" -> (**) and "01011" -> (*(**)) and 0011011 -> ((**)(**)) and (*((**)*)) is mapped from 0100111


#this function efficiently computes the bracketed expression of an iota string (and outputs None if its input is not a valid iota string)
def iota(string):
	#edge cases
	if string == "1":
		return "*"

	if string == "" or string[0] != '0':
		return None

	#we pass through the string once from start to finish. a bracket opens when we see a 0. when we see a 1 we write * and think of it as an input to the last opened bracket. 
	#[each bracket needs two valid inputs, which can be two simple *'s to create (**), but can be more complicated, like *,(**) creating (*(**))] 
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
		else:
			if not (x == '1' and len(stack) > 0):
				return None

			expression += "*"
			
			if stack[-1] == 0:
				stack[-1] = 1
			else:
				while len(stack) > 0 and stack[-1] == 1:
					stack.pop()
					expression += ")"

				if len(stack) == 0:
					if not (i==len(string)-1):
						return None
				else: #if stack is not empty, and its top entry is 0
					stack[-1] = 1
		i += 1

	if not (len(stack)==0):
		return None

	return expression

