hashmap = {}
for i, num in nums:
    complement = target - num
    if complement in hashmap:
        return [hashmap[complement], i]
    hashmap[num] = i
return []