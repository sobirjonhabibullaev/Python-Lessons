from typing import NewType


nums = list(range(101))
new_nums = []
for i in nums:
    if i % 3 != 0 and i % 8 != 0:
        new_nums.append(i)
print(new_nums)
