# nums = (3,3)
# target = 6

def two_sum(nums:list, target:int) -> list:
    n = len(nums)

    for index_i in range(n-1):
        for index_j in range(index_i + 1, n):
            if nums[index_i] + nums[index_j] == target:
                return [index_i, index_j]
    return []


if __name__ == "__main__":
    print(two_sum([2, -4, 11, -15], -19))