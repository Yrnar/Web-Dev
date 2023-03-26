def alarm_clock(day, vacation):
  if day > 0 and day < 6 and vacation == False:
    return "7:00"
  elif ((day == 0 or day == 6) and not vacation) or (day >= 1 and day <= 5 and vacation):
    return "10:00"
  return "off"
