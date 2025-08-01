#Two sum
# Make an empty dictionary
# Look at each number and its index
# Figure out what number would complete the target
# See if that number is already in the dictionary
# If yes, return the two indices
# If no, remember this number and its index for later
# Repeat until you find the answer


def two_sums(nums,target):
    nums_map = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in nums_map:
            return [nums_map[diff],i]
        nums_map[num]=i
    


t = int(input("Enter number of test cases: "))

while t:
    nums = list(map(int, input("Enter numbers (space-separated): ").split()))
    target = int(input("Enter target: "))
    
    print("Result:", two_sums(nums, target))
    
    t -= 1