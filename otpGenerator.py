import random
import smtplib

a=random.randint(100000,999999)



class mail:

    def __init__(self):
        print("Enter Sender mail ID and password")
        self.senderMail=input()
        self.pwd=input()

        print("Enter Reciever mail ID")
        self.userMail = input()


    def send(self):

        try:
            m = smtplib.SMTP('smtp.gmail.com', 587)
            m.starttls()
            m.login(self.senderMail,self.pwd)

            message = 'Subject:{}\n\n{}'.format('DEMO test','Your OneTimePassword(OTP) is ' + str(a) + '.')

            m.sendmail('loopydemo@gmail.com', self.userMail, message)
            print('mail has been sent')

            m.quit()
            obj1.validate()
        except :
            print('Email id is not valid')
            exit()





    def validate(self):
        print("Please enter the otp sent to your registered email id.")
        votp = int(input())

        if a == votp:
            print('SUCCESSFULL')
        else:
            print('Invalid otp please try again')


obj1=mail()
obj1.send()

