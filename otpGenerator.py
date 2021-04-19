import random
import smtplib

a=random.randint(100000,999999)



class mail:

    def __init__(self):
        print('WELCOME to otp generator')


    def send(self):


        m = smtplib.SMTP('smtp.gmail.com', 587)
        m.starttls()
        try:
            print("\nPlease enter sender's mail id and password")
            self.sender = input()
            self.pwd = input()
            m.login(self.sender, self.pwd)
        except:
            print('Sender\'s mail id and password is incorrect\n\nPlease enter valid email id and password again...')
            print('press enter to continue and x to exit  ')
            if input()=='x':
                exit()
            else:
                obj1.send()


        try:
            print("Enter receiver's mail ID")
            self.userMail = input()
            print('Enter the subject of the mail')
            self.sub = input()
            print('Enter the body text')
            self.body = input()

            message = 'Subject:{}\n\n{}'.format(self.sub,self.body + '\n' + 'your one time password is ' + str(a) + '.')
            m.sendmail('loopydemo95@gmail.com', self.userMail, message)
            print('mail has been sent')

            m.quit()
            obj1.validate()
        except:
            print('receiver\'s mail id is not valid')
            print('press enter to continue and x to exit  ')
            if input()=='x':
                exit()
            else:
                obj1.send()


    def validate(self):
        print("Please enter the otp sent to your registered email id.")
        votp = int(input())

        if a == votp:
            print('SUCCESSFULL')
        else:
            print('Invalid otp please try again')



obj1=mail()
obj1.send()

#guys if you are using sololearn, its interpreter is not working correctly with this code.
#Try this in your PC
'''you need to turn on 'allow less secure application access' in your 
google account settings(*only for senders gmail account) to login through any third party applications other than googles like an IDE.'''
