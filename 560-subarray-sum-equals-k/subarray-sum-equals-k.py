class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        sum_count = {0: 1}  # Important: prefix_sum 0 seen once initially

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in sum_count:
                count += sum_count[prefix_sum - k]
            sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
        
        return count
