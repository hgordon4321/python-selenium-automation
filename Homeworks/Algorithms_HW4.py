# Problem 1
def even_first(nums: list):
    index = 0
    for i in range(len(nums)):
        if nums[index] % 2:
            nums.append(nums.pop(index))
        else:
            index += 1
    return nums



# Problem 2
def increment(number: list):
    number[-1] +=1
    for i in range(len(number))[::-1]:
        if number[i] == 10:
            number[i] = 0
            if i > 0:
                number[i-1] += 1
            else:
                number.insert(0, 1)
    return number


# Function Calls:
print('1:', even_first([5, 7, 9, 4, 6, 13, 4]))

print('2.1:', increment([5, 8, 4, 2]))
print('2.3:', increment([4, 9, 9, 9]))
print('2.3:', increment([9, 9, 9, 9]))