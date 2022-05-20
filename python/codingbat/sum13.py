def sum13(nums):
    total = 0
    blacklist = []

    for n, i in enumerate(nums):
        if nums[i] == 13:
            blacklist.append(i, i + 1)

    for n, i in enumerate(nums):
        if i not in blacklist:
            total += nums[n]


print(sum13([1, 2, 2, 1]))
print(sum13([1, 1]))
print(sum13([1, 2, 2, 1, 13]))
