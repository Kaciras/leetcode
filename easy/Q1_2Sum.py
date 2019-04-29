class Solution:

	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		visited = dict()
		for i in range(len(nums)):
			n = nums[i]
			another = target - n
			if another in visited.keys():
				return [visited[another], i]
			visited[n] = i

if __name__ == '__main__':
	print(Solution().twoSum([2, 7, 11, 15], 9))