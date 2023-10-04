def largestSubarrayWithSumZero(nums):
    if not nums:
        return 0
    
    sum_map = {}  
    max_length = 0
    cumulative_sum = 0
    
    for i in range(len(nums)):
        cumulative_sum += nums[i]
        
        if cumulative_sum == 0:
            max_length = i + 1
        
        if cumulative_sum in sum_map:
            max_length = max(max_length, i - sum_map[cumulative_sum])
        else:
            sum_map[cumulative_sum] = i
    
    return max_length

nums = [15, -2, 2, -8, 1, 7, 10, 23]
result = largestSubarrayWithSumZero(nums)
print(result)
