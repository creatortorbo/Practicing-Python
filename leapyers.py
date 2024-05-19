# here we find the leap year
leap_years = int(input('Enter a number :'))

if (leap_years%100==0) and (leap_years%400):
    print('it leap years',leap_years)

elif (leap_years%4==0) and (leap_years%100!=0):
    print('it is leap years ',leap_years)

else :
    print('Not leap years')