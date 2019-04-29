class Solution:
	"""其他方法有使用字典来计数等"""

	def intersect(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[int]
		"""
		nums1.sort()
		nums2.sort()
		r, i, j = [], 0, 0
		while i < len(nums1) and j < len(nums2):
			a, b = nums1[i], nums2[j]
			if a < b:
				i += 1
			elif a > b:
				j += 1
			else:
				r.append(a)
				i += 1
				j += 1
		return r


if __name__ == '__main__':
	print(Solution().intersect([1, 2, 2, 1], [2, 2]))  # [2, 2]
