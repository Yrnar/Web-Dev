def in1to10(n, outside_mode):
  return ( n >= 1 and n <= 10 and outside_mode == False) or ((n < 2 or n > 9) and outside_mode == True )
