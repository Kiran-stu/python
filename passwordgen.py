import random

password=('a','e','q',')','(','^','%','_','+','}','!','@','4','1','~','w','/','*','7',']','A','d','H','e','r','f','<','?','r','Y','>','z','`','#','b','-','8','1','0','6','j','e','5','3','g','^','P','u','2','w')


#b='kiran'
print('Password Generator\n')
#print(len(password))
print('Enter the lenght of the password you need to generate')
length=int(input())

if(length==0):
    print('Enter valid length\n')
else:
    print('your password is ready\n')
for i in range(0,length):
    a=random.randrange(0,50,1)
    #sample.append(a)
    print(str(password[a]),end='')