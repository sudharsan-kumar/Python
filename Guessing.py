

logo ="""
  ________                                __   .__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ _/  |_|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ |
\    \_\  \  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >  |__| |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/             \/     \/          \/            \/    \/     \/    

"""
import random
def guess (m):
  win =  random.randint(1,100)
  if m == 'easy':                                                           #Determining no. of chances
    chances = 10
  else:
    chances = 5
  while chances > 0 :                                                       #Looping the guessing part
    gues = int(input(f'Enter your guess.You have {chances} chance/s:'))     #Entering the user's guess
    if win == gues:
      return 1
    else:
      print ("Wrong.Guess again")                                             
      if gues > win:
        print ("Your guess is HIGH")
      elif gues < win:
        print ("Your guess is LOW")
      chances -= 1                                                          #Decreasing the chances
  if chances == 0:
    return 0

print(logo)
mode = input('You need to guess the number between 1 to 100. \n Enter the mode you want to play("easy" or "hard": ')
result = guess (mode)
if result == 0:
  print('You Lost')
if result == 1:
  print('You Won')
