def caught_speeding(speed, is_birthday):
  if speed <= 60 or speed <= 65 and is_birthday:
    return 0
  if speed >= 61 and speed <= 80 or speed >= 66 and speed <= 85 and is_birthday:
    return 1
  if speed >= 81 or speed >= 86 and is_birthday:
    return 2
