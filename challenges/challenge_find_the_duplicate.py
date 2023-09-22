def find_duplicate(nums):
    """Faça o código aqui."""
    if (
        all(isinstance(num, int) and num > 0 for num in nums)
        and type(nums) == list
        and len(nums) > 1
    ):
        nums.sort()
        for i, num in enumerate(nums):
            if (i + 1) == len(nums):
                return False
            if num == nums[i + 1]:
                return num
    return False
