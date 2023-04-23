def any7(nums):
    """Are any of these numbers a 7? (True/False)"""
    for num in nums:
        if num == 7:
            return True
        elif not num == 7:
            continue
    return False


print("should be True:", any7([1, 2, 7, 4, 5]))
print("should be False:", any7([1, 2, 4, 5]))
