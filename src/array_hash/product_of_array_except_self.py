def product_of_array_except_self(nums: list[int]) -> list[int]:
    # calculate the left products
    left_products = [1] * len(nums)
    for i in range(1, len(nums)):
        left_products[i] = left_products[i-1] * nums[i-1]

    # calculate the right products
    right_products = [1] * len(nums)
    for i in range(len(nums) - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i+1]

    result = [left_products[i] * right_products[i] for i in range(0, len(nums))]
    return result
