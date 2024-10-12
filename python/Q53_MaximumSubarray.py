class Solution:

	def maxSubArray(self, nums: list[int]):
		# c 是当前子序列的和，m 是最大子序列的和。
		c, m = 0, nums[0]
		for n in nums:
			c += n
			# 比当前值还小，表明可以改从现在开始。
			if c < n: c = n
			# 如果比当前的结果值要大，则更新结果。
			if c > m: m = c
		return m


def test_case1():
	assert Solution().maxSubArray([-2, -1]) == -1


def test_case2():
	assert Solution().maxSubArray([-3, -2, 0, -1]) == 0


def test_example1():
	assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_example2():
	assert Solution().maxSubArray([1]) == 1


def test_example3():
	assert Solution().maxSubArray([5, 4, -1, 7, 8]) == 23


def test_user1():
	assert Solution().maxSubArray([-1]) == -1
