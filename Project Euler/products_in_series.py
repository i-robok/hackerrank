import sys


def int2list(num):
    return [int(x) for x in str(num)]

def largestProduct(nums, k):
    largest_product = 0
    for i in range(len(nums) - k + 1):
        product = 1
        for j in range(k):
            product *= nums[i + j]
        largest_product = max(largest_product, product)

    return largest_product



t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()

    num_list = int2list(num)
    print(num_list)
    print(largestProduct(num_list, k))
