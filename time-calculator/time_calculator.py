def add_time(start, duration, startingday = None):

  #Inital variables
  day = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
  final_hour = 0
  final_day = ''
  start_hour_military = 0
  ampm = ["AM","PM"]

  #Split start into time and ampm
  start = start.rsplit(" ")
  start_time = start[0]
  start_ampm = start[1]

  #Get start time AM/PM
  curr_ampm = ampm.index(start_ampm)

  #Format start and duration times ['#','#']
  start_time = start_time.rsplit(":")
  duration_time = duration.rsplit(":")

  #Duration time hours and start time hours to integer
  dur_hour = int(duration_time[0])
  start_hour = int(start_time[0])

  #Add final time minutes
  final_min = int(start_time[1]) + int(duration_time[1])

  #Calculate roll over minutes and convert final min to str
  if final_min >= 60:
    final_min -= 60
    dur_hour += 1

  if final_min > 9:
    final_min = str(final_min)
  else:
    final_min = '0' + str(final_min)

  #Calculate final time with dur_hour (minutes already calculated as final_min)

  #Convert start hour to military
  #If time start time is initially in the PM
  if curr_ampm == 1 and start_hour == 12:
    start_hour_military = 12
  if curr_ampm == 1 and start_hour <= 11:
    start_hour_military = start_hour + 12

  #If time start time is initially in the AM 
  if curr_ampm == 0 and start_hour == 12:
    start_hour_military = 0
  if curr_ampm == 0 and start_hour <= 11:
    start_hour_military = start_hour

  #Calculate remaining hours left in a day from duration hours
  remaining_dur_hours = dur_hour % 24

  #Calculate days
  days = int(dur_hour / 24)

  #Calculate days overlap from start hour military and remaining dur hours by add_time
  hours_overlap = start_hour_military + remaining_dur_hours
  if hours_overlap >= 24:
    days += 1
  final_hour_military = hours_overlap % 24

  #Convert militray final hour to regular time format
  if final_hour_military == 0:
    final_hour = 12
    curr_ampm = 0
  if final_hour_military > 0 and final_hour_military < 12:
    final_hour = final_hour_military
    curr_ampm = 0
  if final_hour_military == 12:
    final_hour = 12
    curr_ampm = 1
  if final_hour_military > 12 and final_hour_military < 24:
    final_hour = final_hour_military - 12
    curr_ampm = 1
  if final_hour_military == 24:
    final_hour = final_hour_military - 12
    curr_ampm = 0

  #Convert final hour to string
  final_hour = str(final_hour)

  #Print end time with no new line
  print(final_hour + ':' + final_min, ampm[curr_ampm], end = '')

  #Print final day
  if startingday != None:
    startingday = startingday.lower().capitalize()
    curr_day = day.index(startingday)
    day_calc = (curr_day + days) % 7
    final_day = day[day_calc]
    print(", " + final_day, end = ' ')

  #Print number of days
  if days > 1:
    print(" (" + str(days) + " days later)")
  elif days == 1:
    print(" (next day)")
  

  