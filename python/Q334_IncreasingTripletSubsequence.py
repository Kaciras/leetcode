class Solution:

	def increasingTriplet(self, nums: list[int]):
		"""
		三个连续递增是有限状态，搞俩变量完事。
		这里的关键在于一旦 second 赋值即表明已有两个递增。
		"""
		if len(nums) < 3:
			return False
		first = second = float('inf')
		for n in nums:
			if n <= first:
				first = n
			elif n <= second:
				second = n
			else:
				return True
		return False

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

	def increasingTriplet_2(self, nums: list[int]):
		return self.increasingN(nums, 3)

	def increasingTriplet_1(self, nums: list[int]):
		"""
		这个其实等价于increasingN，只是分成俩数组搞复杂了
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
	assert Solution().increasingTriplet([5, 1, 5, 5, 2, 5, 4]) == True
	assert Solution().increasingTriplet([2, 5, 3, 4, 5]) == True
	assert Solution().increasingTriplet([3, 4, 1, 5]) == True
	assert Solution().increasingTriplet([6, 9, 1, 2, 7]) == True

	assert Solution().increasingTriplet([2, 4, -2, -3]) == False
	assert Solution().increasingTriplet([5, 4, 3, 2, 1]) == False
