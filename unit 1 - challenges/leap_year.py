#this program is designed for calculates leap year 

n=int(input('Enter year :'))
if n%4==0 and n%100 and n%400:
    print(n,' is leap year')
    
else:
    print (n,' is not leap year')
    