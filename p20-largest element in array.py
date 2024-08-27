def large_element (arr):
    if not arr:
        return"empty array"
    large=arr[0]
    for element in arr:
        if element>large:
            large=element
            return large
my_arr=[10,99,76,32]
result=large_element(my_arr)
print(result)