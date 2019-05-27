from typing import List


class Solution:

	def rotate(self, nums: List[int], k: int) -> None:
		"""三次翻转法，分别翻转被移动的部分、剩下的部分，最后再整个翻转一下"""
		k = len(nums) - k % len(nums)
		nums[::-1] = nums[k - 1::-1] + nums[:k - 1:-1]


def test(nums, k):
	Solution().rotate(nums, k)
	print(nums)


if __name__ == '__main__':
	test([1, 2], 1)  # [2, 1]
	test([1, 2], 2) # [1, 2]
	test([1], 1) # [1]
	test([1, 2, 3, 4, 5, 6, 7], 3)  # [5,6,7,1,2,3,4]
	test([-1, -100, 3, 99], 2)  # [3,99,-1,-100]
