# Python Program to Check Prime Number 
num = int(input("Enter a number :"))

if (num == 1):
  print('it is not a prime number')

elif (num>1):
  for i in range(2,num):
    if (num % i == 0):
      print('it not a prime number')
    break

else:
  print(num,'prime number')