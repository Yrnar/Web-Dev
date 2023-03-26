def sum13(nums):
  s = 0
  i = 0
  while len(nums) > i:
    if nums[i] != 13:
      s += nums[i]
    else: i += 1
    i += 1
  return s
