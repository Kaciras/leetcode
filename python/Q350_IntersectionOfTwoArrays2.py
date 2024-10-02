class Solution:
	"""其他方法有使用字典来计数等"""

	def intersect(self, nums1: list[int], nums2: list[int]):
		"""先排序然后找共同的，O(m + n)时间"""
		nums1.sort()
		nums2.sort()
		result, i, j = [], 0, 0

		while i < len(nums1) and j < len(nums2):
			a, b = nums1[i], nums2[j]
			if a < b:
				i += 1
			elif a > b:
				j += 1
			else:
				i += 1
				j += 1
				result.append(a)

		return result


if __name__ == '__main__':
	print(Solution().intersect([1, 2, 2, 1], [2, 2]))  # [2, 2]
	print(Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # [4, 9]
