def max_end3(nums):
  nums[0] = nums[1] = nums[2] = max(nums[0], nums[2])
  return nums