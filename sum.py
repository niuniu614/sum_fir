nums = [value for value in range(1,11)]
print(nums)
target = 16
output = []
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            output.append(i)
            output.append(j)
            break
    if output:
        print(output)
        print(nums[output[0]],nums[output[1]])
        break
