class Solution:

	def removeDuplicates(self, nums: list[int]):
		last, length = None, 0
		for n in nums:
			if last != n:
				nums[length] = n
				last = n
				length += 1
		return length


def test_example1():
	nums = [1, 1, 2]
	length = Solution().removeDuplicates(nums)
	assert nums[:length] == [1, 2]


def test_example2():
	nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
	length = Solution().removeDuplicates(nums)
	assert nums[:length] == [0, 1, 2, 3, 4]
