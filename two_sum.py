def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Возвращает индексы двух чисел, дающих в сумме target.
    Сложность: O(n).
    """
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    half = target // 2
    if half in nums:
        if target - half * 2 == 0:
            return [nums.index(half), nums.index(half)]
    return []


def main() -> None:
    # Example 1
    nums1, target1 = [2, 7, 11, 15], 9
    result1 = two_sum(nums1, target1)
    print(f"Example 1: nums={nums1}, target={target1} -> {result1}")

    # Example 2
    nums2, target2 = [3, 2, 4], 6
    result2 = two_sum(nums2, target2)
    print(f"Example 2: nums={nums2}, target={target2} -> {result2}")

    # Example 3
    nums3, target3 = [3, 3], 6
    result3 = two_sum(nums3, target3)
    print(f"Example 3: nums={nums3}, target={target3} -> {result3}")


if __name__ == "__main__":
    main()
