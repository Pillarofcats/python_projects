import time
import replit

def start_clock():

  firsthour = 0
  secondhour = 0
  firstminute = 0
  secondminute = 0
  firstsecond = 0
  secondsecond = 0

  end = False

  #Start clock
  while end == False:

    secondsecond = 0

    for i in range(10):
      # replit.clear()
      print(firsthour, secondhour, ":" ,firstminute, secondminute, ":",firstsecond, secondsecond)
      time.sleep(.1)
      secondsecond += 1

      #Update time
      if secondsecond == 10:
        firstsecond += 1
        secondsecond = 0

      if firstsecond == 6 and secondsecond == 0:
        secondminute += 1
        firstsecond = 0
      
      if secondminute == 10:
        firstminute += 1
        secondminute = 0

      if firstminute == 6 and secondminute == 0:
        secondhour += 1
        firstminute = 0

      if secondhour == 10:
        firsthour += 1
        secondhour = 0

      if firsthour == 2 and secondhour == 4:
        print(firsthour, secondhour, ":" ,firstminute, secondminute, ":",firstsecond, secondsecond)
        end = True
        break