# Python Program to Check If the Number is Armstrong or Not?
num = int(input('Enter a number is :'))

sum = 0
temp = num 

while temp >0:
   digit = temp%10
   cube = digit ** 3
   sum = sum + cube 
   temp//= 10  # here it removing the last number


if sum == num :
   print('it is an armstrong number')
else:
   print('it is  not aramstrong number')