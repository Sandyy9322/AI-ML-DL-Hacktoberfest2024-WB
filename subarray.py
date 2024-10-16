def max_subarray_sum(nums):
    # Initialize variables
    max_current = max_global = nums[0]  # Start with the first element
    
    for i in range(1, len(nums)):
        # Dynamic programming step:
        max_current = max(nums[i], max_current + nums[i])
        
        # Update global maximum if current max is greater
        if max_current > max_global:
            max_global = max_current
    
    return max_global

# Example usage
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(nums)
print("Maximum Subarray Sum is:", result)
