def maxSubArray(nums):
    # 动态规划，原地修改数组
    maxnum = nums[0]
    for i in range(1,len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
        maxnum = max(maxnum,nums[i])
    print(maxnum)
while(1):
    arr = input("")
    num = [int(n) for n in arr.split()]    
    maxSubArray(num)
