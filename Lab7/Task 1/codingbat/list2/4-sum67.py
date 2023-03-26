def sum67(nums):
  s = 0
  flag = False
      
  for i in range(len(nums)):
    if nums[i] == 6:
      flag = True
    if not flag:
      s += nums[i]
    if nums[i] == 7 and flag:
      flag = False
            
  return s