# Find the Largest Among Three Numbers
number1 = int(input('Enter a fist number :'))
number2 = int(input('Enter a second number :'))
number3 = int(input('Enter a third number :'))

if (number1>number2) and (number1>number3):
     print(number1,'number is largest')

elif (number2>number1) and (number2>number3):
     print(number2,'number is largest',number2)

else :
     print(number3,'number is largest')
