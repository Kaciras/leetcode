import collections


class Solution:
	def threeSum(self, nums):
		"""使用Counter计数并去重，然后再判断各种情况，是最优的解法"""
		ct = collections.Counter(nums)
		pos, neg, result = [], [], []

		for v in ct.keys():
			if v >= 0:
				pos.append(v)
			else:
				neg.append(v)

		if ct.get(0) > 2:
			result.append([0, 0, 0])

		for i in pos:
			for j in neg:
				e = -(i + j)
				if j < e < i:
					result.append([i, j, e])
				elif (e == i or e == j) and ct[e] > 1:
					result.append([i, j, e])
		return result

	def threeSum3(self, nums):
		"""排序从两边扫描，外层只遍历正数"""
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
		"""
		用Set去重会超时
		"""
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


if __name__ == '__main__':
	print(Solution().threeSum([-2, 0, 1, 1, 2]))  # 2
	print(Solution().threeSum([-1, 0, 1, 0]))  # 1
	print(Solution().threeSum([0, 0, 0, 0, 0, 0]))  # 1
	print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))  # 2
	print(Solution().threeSum([3, 0, -2, -1, 1, 2]))  # 3
