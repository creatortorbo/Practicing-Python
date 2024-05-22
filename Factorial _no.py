# Find the Factorial of a Number
num = int(input('Enter a number :'))

factorial = 1

if (num <0):
  print('Not factorial')
elif (num==0):
  print('0 factorial')
if (num>0):

 for  i in range(1,num+1):
    factorial = factorial * i

print('The factorial of the given input is',factorial)
    

                              