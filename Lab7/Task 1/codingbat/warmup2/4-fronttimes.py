def front_times(str, n):
  a = 3
  if len(str) < a:
    a = len(str)
  return str[:a] * n
