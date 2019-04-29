class Solution:

	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		last, length = None, 0
		for n in nums:
			if last != n:
				nums[length] = n
				last = n
				length += 1
		return length


if __name__ == '__main__':
	input_0 = [1, 1, 2]
	print(str(Solution().removeDuplicates(input_0)) + " " + str(input_0))

	input_1 = [0,0,1,1,1,2,2,3,3,4]
	print(str(Solution().removeDuplicates(input_1)) + " " + str(input_1))
