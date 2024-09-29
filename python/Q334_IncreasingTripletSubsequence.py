class Solution:

	def increasingN(self, nums, n):
		if n < 2:
			raise ValueError()
		if len(nums) < n:
			return False

		incs = [float("inf")] * (n - 1)
		for x in nums:
			found = True
			for i, v in enumerate(incs):
				if x <= v:
					found, incs[i] = False, x
					break
			if found:
				return True
		return False

	def increasingTriplet(self, nums):
		return self.increasingN(nums, 3)

	def increasingTriplet_old(self, nums):
		"""
		这个其实等价于increasingN，只是分成俩数组搞复杂了
		:type nums: List[int]
		:rtype: bool
		"""
		if len(nums) < 3:
			return False

		a = [nums[0]]
		b = [nums[0]]

		for x in nums[1:]:
			if x > a[-1]:
				if len(a) == 2:
					return True
				a.append(x)

			for i, v in enumerate(b):
				if v >= x:
					b = b[:i]
					break
			if len(b) == 2:
				return True
			b.append(x)

			if len(b) > len(a):
				a = b[:]

		return False


if __name__ == '__main__':
	print(Solution().increasingTriplet([5, 1, 5, 5, 2, 5, 4]))
	print(Solution().increasingTriplet([2, 5, 3, 4, 5]))
	print(Solution().increasingTriplet([3, 4, 1, 5]))
	print(Solution().increasingTriplet([6, 9, 1, 2, 7]))

	print(Solution().increasingTriplet([5, 4, 3, 2, 1]))
	print(Solution().increasingTriplet([2,4,-2,-3]))
