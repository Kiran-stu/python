import random
import pyttsx3

num = random.randint(1,20)

a=pyttsx3.init()

a.say('Welcome to Guessing game')
a.say("A random number is selected between 1 to 20")
a.say("Now you try to guess the number\n")
a.say("Guess the number "+"  you have only 5 chances!!")
print("Enter the number you have guessed")
a.runAndWait()



for i in range(1, 6):


    ch = int(input())
    if ch < num:
        a.say(str(ch) + " is not CORRECT")
        a.runAndWait()
        if i==4:
            a.say("Last chance")
            a.runAndWait()
        if i!=5:
            a.say("try out a number greater than "+str(ch))
            a.runAndWait()
        else:
            a.say('so close')
            a.runAndWait()

    if ch > num:
        a.say("ohh! You guessed higher than the number")
        a.runAndWait()
        if i==4:
            a.say("Last chance")
            a.runAndWait()
        if i != 5:
            a.say("Try out a number less than "+str(ch))
            a.runAndWait()
        else:
            a.say("soo close")
            a.runAndWait()
    if ch == num:
        break


if num == ch:
    a.say("You're god damn right\n" + "The number was " + str(num))
    a.say("You won the game")
    a.runAndWait()

else:
    a.say("The number was "+ str(num))
    a.say("try again , you failed")
    a.runAndWait()

