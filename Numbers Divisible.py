# # Python Program to Find Numbers Divisible by Another Number
# # num = int(input('Enter a number :'))

# for i in range (1,100):
#    if i % 13 == 0 :
#       print('The number is divisible by another number :',i)
# #    else :
# #       print('Not divisible by another number ',i)


# here 2 using Lambda function and filter ()
 
l = [39,48,26,98,33,67,87]

result = list(filter(lambda x: x % 13 ==0 ,l))

print('The number divisible by',result)