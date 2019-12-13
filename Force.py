import getpass
import time
import string
numbers = list(string.ascii_letters)

def crack(password):
   pwned = ''
   i1 = 0
   i2 = 0
   i3 = 0
   i4 = 0
   ncaracteres = 1
   ispwned = False
   start = time.time()
   while (ispwned == False):
      #Inicia Prueba un Solo caracter
      if ncaracteres == 1:
         pwned = numbers[i1]
         if pwned != password:
            if i1 != 51:
               i1 = i1 + 1
            else:
               ncaracteres = ncaracteres + 1
               i1 = 0
         else:
            ispwned = True
       # Inicia Prueba Dos caracteres
      elif ncaracteres == 2:
         pwned = numbers[i2] + numbers[i1]
         if pwned != password:
            if i2 <= 51 and i1 <= 51 and ((i2+i1) != 102):
               if i1 != 51:
                  i1 = i1+1
               else:
                  i2 = i2 + 1
                  i1 = 0
            else:
               ncaracteres = ncaracteres + 1
               i1 = 0
               i2 =0
         else:
            ispwned = True
      # Inicia Prueba Tres caracteres
      elif ncaracteres == 3:
         pwned = numbers[i3] + numbers[i2] + numbers[i1]
         if pwned != password:
            if i3 <= 51 and i2 <= 51 and i1 <= 51 and (i1+i2+i3) != 153:
               if i1 != 51:
                  i1 = i1+1
               elif i1 == 51 and i2 != 51:
                  i2 = i2 + 1
                  i1 = 0
               else:
                  i3 = i3 + 1
                  i2 = 0
                  i1 = 0
            else:
               ncaracteres = ncaracteres + 1
               i1 = 0
               i2 = 0
               i3 = 0
         else:
            ispwned = True
      # Inicia Prueba Cuatro caracteres
      elif ncaracteres == 4:
         pwned = numbers[i4] + numbers[i3] + numbers[i2] + numbers[i1]
         if pwned != password:
            if i4 <= 51 and i3 <= 51 and i2 <= 51 and i1 <= 51:
               if i1 != 51:
                  i1 = i1+1
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
               ncaracteres = ncaracteres + 1
               i1 = 0
               i2 = 0
               i3 = 0
         else:
            ispwned = True





   end = time.time()
   seconds = str(end - start)
   print ("You have been pwned your password is: "+ pwned)
   print("Elapsed time:" + seconds + " seconds")


def main():
   h = 0
   contains = False

   password = getpass.getpass("Enter your password: ")

   while h != len(password):
      test = password[h]
      if test.isdigit():
         contains = True
      h = h + 1

   if len(password) <= 4 and len(password) > 0 and contains == False:
      crack(password)
   else:
      print("Error the password must have a maximum of 4 characters")
      main()

main()
