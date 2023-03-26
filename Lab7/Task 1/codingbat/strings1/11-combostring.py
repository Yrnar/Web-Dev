def combo_string(a, b):
  temp = ""
  if len(a) < len(b):
    temp = b
    b = a
    a = temp
  return b + a + b
    
