def front3(str):
  n = 3
  if len(str) < n:
    n = len(str)
  return str[:n] * 3
