import collections

from pytest_unordered import unordered


class Solution:
	def threeSum(self, nums: list[int]) -> list[list[int]]:
		"""使用 Counter 计数并去重，然后再判断各种情况，是最快的解法"""
		counter = collections.Counter(nums)
		pos, neg, result = [], [], []

		for v in counter.keys():
			if v >= 0:
				pos.append(v)
			else:
				neg.append(v)

		# 全零的话不需要正负数，看下有没有足够的 0 即可。
		if counter[0] > 2:
			result.append([0, 0, 0])

		# 要归零，一定得有正数和负数，然后再找一个差值凑三个。
		for i in pos:
			for j in neg:
				e = -(i + j)
				if j < e < i and counter[e] > 0:
					result.append([i, j, e])
				elif (e == i or e == j) and counter[e] > 1:
					result.append([i, j, e])

		return result

	def threeSum3(self, nums):
		"""排序从两边扫描，外层只遍历正数，该实现内存占用小"""
		nums.sort()
		i, p, result = 0, None, []

		while i < len(nums):
			v0 = nums[i]
			if v0 > 0:
				break
			i += 1
			if v0 == p:
				continue
			p = v0

			j, k = i, len(nums) - 1
			while j < k:
				e = -(v0 + nums[j])
				if e > nums[k]:
					j += 1
				elif e < nums[k]:
					k -= 1
				else:
					result.append([v0, nums[j], e])
					while j < k and nums[j] == nums[j + 1]:
						j += 1
					while j < k and nums[k] == nums[k - 1]:
						k -= 1
					j += 1
					k -= 1
		return result

	def threeSum2(self, nums):
		"""用 Set 去重会超时"""
		result, set_, v1, v2 = [], set(nums), set(), set()

		for i in range(len(nums) - 2):
			v = nums[i]
			if v in v1:
				continue
			v1.add(v)

			for j in range(i + 1, len(nums)):
				if nums[j] in v2:
					continue
				b = -(v + nums[j])
				if b in set_:
					result.append([v, nums[j], b])
					v1.add(nums[j])
					v2.add(b)
					v2.add(nums[j])

		return result


def _invoke_any_order(nums):
	"""返回的是二维数组，要做两层无序处理，写个辅助函数"""
	return unordered([unordered(x) for x in Solution().threeSum(nums)])


def test_example1():
	assert _invoke_any_order([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]


def test_example2():
	assert _invoke_any_order([0, 1, 1]) == []


def test_example3():
	assert _invoke_any_order([0, 0, 0]) == [[0, 0, 0]]


def test_case1():
	assert _invoke_any_order([1, 2, -2, -1]) == []


def test_case2():
	assert _invoke_any_order([-2, 0, 1, 1, 2]) == [[1, -2, 1], [2, -2, 0]]


def test_case3():
	assert _invoke_any_order([-1, 0, 1, 0]) == [[1, -1, 0]]


def test_case4():
	assert _invoke_any_order([3, 0, -2, -1, 1, 2]) == [[3, -2, -1], [1, -1, 0], [2, -2, 0]]


def test_user1():
	assert _invoke_any_order([1, 1, -2]) == [[1, -2, 1]]
