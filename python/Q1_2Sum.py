from utils import benckmark


# 虽然本地快了点，但在 leetcode 上还是 56ms
class Solution:

	def twoSum(self, nums: list[int], target: int):
		"""
		直接 key in dict 而不是 key in dict.keys()，耗时降低了 0.3 秒/百万次
		使用 enumerate(nums) 代替 range(len(nums)))，耗时降低了 0.07 秒/百万次
		visited = dict() 比 visited = {} 写法竟然慢了 0.1 秒/百万次
		"""
		visited = {}
		for i, n in enumerate(nums):
			another = target - n
			if another in visited:
				return [visited[another], i]
			visited[n] = i


if __name__ == '__main__':
	assert Solution().twoSum([2, 1, -8, 7, 11, 15], 9) == [0, 3]
	benckmark(Solution().twoSum, [2, 1, -8, 7, 11, 15], 9)
