class Calculator():

	def add(self, num1, num2):
		return num1+num2
		
	def subtract(self, num1, num2):
		return num1-num2

	def multiply(self, num1, num2):
		return num1*num2

	def divide(self, num1, num2):
		if num2==0:
			print('num2 cannot be 0')
			return
		else:
			return num1/num2

if __name__ == '__main__':
	cal=Calculator()
	print('3+2=', cal.add(3,2))
	print('3-2=', cal.subtract(3,2))
	print('3*2=', cal.multiply(3,2))
	print('3/2=', cal.divide(3,2))
