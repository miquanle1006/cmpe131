def calculator(number1, number2, operator):
	"""

	"""

	result = 0
	num1 = float(number1)
	num2 = float(number2)
	
	if operator in ('+','-','*','/','//','**'):
		if operator == '+':	
			result= num1 + num2	 
		elif operator == '-':	
			result= num1 - num2	 	
		elif operator == '*':	
			result= num1 * num2	 	
		elif operator == '/':	
			result= num1 / num2	 	
		elif operator == '//':	
			result= num1 // num2	 	
		elif operator == '**':	
			result= num1 ** num2	 		
	else:
		print('Invalid value!!!')
		return False
	return result

def parse_input():
	"""

	"""

	prompt = eval('input("Enter equation: ")')
	text = prompt.split(' ')
	num1 = text[0]
	num2 = text[2]
	operator = text[1]
	return calculator(num1,num2,operator)	


