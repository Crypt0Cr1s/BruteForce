import getpass
import time
import string
from threading import Thread

pwned = ''
ispwned = False



def unCaracter(numbers,password,i1,ispwned):
    start = time.time()
    while (ispwned == False and i1 <= 51):
        pwned = numbers[i1]
        if pwned != password:
            if i1 != 51:
                i1 = i1 + 1
            else:
                i1 = i1 + 1
                print("The password doesnt have 1 characters closing thread")
        else:

            end = time.time()
            ispwned = True
            print("You have been pwned your password is: " + pwned)
            seconds = str(end - start)
            print("Elapsed time:" + seconds + " seconds")


def dosCaracter(numbers,password,ispwned,i1,i2):
    start = time.time()
    while (ispwned == False and i2<=51):
        pwned = numbers[i1] + numbers[i2]
        if pwned != password:
            if i2 <= 51 and i1 <= 51 and ((i2 + i1) != 102):
                if i1 != 51:
                    i1 = i1 + 1
                else:
                    i2 = i2 + 1
                    i1 = 0
            else:
                i2 = i2 + 1
                print("The password doesnt have 2 characters closing thread")
        else:
            end = time.time()
            ispwned = True
            print("You have been pwned your password is: " + pwned)
            seconds = str(end - start)
            print("Elapsed time:" + seconds + " seconds")



def tresCaracter(numbers,password,ispwned,i1,i2,i3):
    start = time.time()
    while (ispwned == False and i3 <= 51):
        pwned = numbers[i3] + numbers[i2] + numbers[i1]
        if pwned != password:
            if i3 <= 51 and i2 <= 51 and i1 <= 51 and (i1 + i2 + i3) != 153:
                if i1 != 51:
                    i1 = i1 + 1
                elif i1 == 51 and i2 != 51:
                    i2 = i2 + 1
                    i1 = 0
                else:
                    i3 = i3 + 1
                    i2 = 0
                    i1 = 0
            else:
                i3 = i3 + 1
                print("The password doesnt have 3 characters closing thread")
        else:
            end = time.time()
            ispwned = True
            print("You have been pwned your password is: " + pwned)
            seconds = str(end - start)
            print("Elapsed time:" + seconds + " seconds")

def cuatroCaracter(numbers,password,ispwned,i1,i2,i3,i4):
    start = time.time()
    while (ispwned == False and i4 <= 51):
        pwned = numbers[i4] + numbers[i3] + numbers[i2] + numbers[i1]
        if pwned != password:
            if i4 <= 51 and i3 <= 51 and i2 <= 51 and i1 <= 51 and (i1 + i2 + i3 + i4) != 204:
                if i1 != 51:
                    i1 = i1 + 1
                elif i1 == 51 and i2 != 51:
                    i2 = i2 + 1
                    i1 = 0
                elif i1 == 51 and i2 == 51 and i3 != 51:
                    i3 = i3 + 1
                    i2 = 0
                    i1 = 0
                elif i1 == 51 and i2 == 51 and i3 == 51 and i4 != 51:
                    i4 = i4 + 1
                    i3 = 0
                    i2 = 0
                    i1 = 0
            else:
                i4 = i4 + 1
                print("The password doesnt have 4 characters closing thread")
        else:
            end = time.time()
            ispwned = True
            print("You have been pwned your password is: " + pwned)
            seconds = str(end - start)
            print("Elapsed time:" + seconds + " seconds")


def main():
    numbers = list(string.ascii_letters)
    h = 0
    contains = False
    password = getpass.getpass("Enter your password: ")
    while h != len(password):
        test = password[h]
        if test.isdigit():
            contains = True
        h = h + 1

    if len(password) <= 4 and len(password) > 0 and contains == False:
        i1 = 0
        i2 = 0
        i3 = 0
        i4 = 0

        thread1 = Thread(target = unCaracter, args = (numbers, password, i1, ispwned))
        thread2 = Thread(target = dosCaracter, args = (numbers, password,ispwned,i1,i2))
        thread3 = Thread(target = tresCaracter, args = (numbers,password,ispwned,i1,i2,i3))
        thread4 = Thread(target=cuatroCaracter, args = (numbers, password, ispwned, i1, i2, i3,i4))

        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()

    else:
        print ("Error the password must have a maximum of 4 characters and doesn't contain numbers")
        main()





main()