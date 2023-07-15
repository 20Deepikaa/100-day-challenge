
def secondmax(nums):
    nums.sort()
    return nums[1]
N = int(input())
for _ in range(N):
    nums = list(map(int, input().split()))
    second_max = secondmax(nums)
    print(second_max)
