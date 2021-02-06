import random

password=('a','e','q',')','(','^','%','_','+','}','!','@','4','1','~','w','/','*','7',']','A','d','H','e','r','f','<','?','r','Y','>','z','`','#','b','-','8','1','0','6','j','e','5','3','g','^','P','u','2','w')


#b='kiran'
print('Password Generator\n')
#print(len(password))


infi=0
print('Press X to start and S to stop and R to regenrate the password')
while infi!='x':

    infi=input()

    if infi=='x':
        break

    #lenght=0

    try:
        print('Enter the lenght of the password you need to generate')
        length = int(input())
        if (length == 0):
            print('Enter valid length\n')
        else:
            print('your password is ')
    except:
        print('No value Entered pls Re-enter idiot')
        print('Press Enter to continue')
        continue

    print('\n')

    for i in range(0, length):
        a = random.randrange(0, 50, 1)
        # sample.append(a)
        print(str(password[a]), end='')
    print('\n')
    print('\nPress Enter to continue')
