def secondlargest(arr):
    nums = sorted(set(arr))

    if(len(nums) < 2):
        return -1
    else:
        return nums[-2]






arr = list(map(int, input("Enter numbers separated by commas: ").split(',')))
result = secondlargest(arr)
if(result != -1):
    print("Second Largest And Distinct Number : ", result)
else:
    print("Not found : ", result)