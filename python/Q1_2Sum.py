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


def test_example1():
	assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]


def test_example2():
	assert Solution().twoSum([3, 2, 4], 6) == [1, 2]


def test_example3():
	assert Solution().twoSum([3, 3], 6) == [0, 1]


def test_case1():
	assert Solution().twoSum([2, 1, -8, 7, 11, 15], 9) == [0, 3]


if __name__ == '__main__':
	benckmark(Solution().twoSum, [2, 1, -8, 7, 11, 15], 9)
