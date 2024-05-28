# Python Program to Display Powers of 2 Using Anonymous Function.
# here we using the lambra funtion

n_terms = int(input('Enter number of terms here :'))

result = list(map(lambda x : 2 ** x ,range(n_terms+1)))

print(result)


for i in range(n_terms):
    print('The values of 2 raised to power',i,'is',result[i])