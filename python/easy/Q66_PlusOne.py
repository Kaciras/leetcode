class Solution:
	"""代码最少的方法是转成整数再转字符串，但是那样太没意思了"""

	def plusOne(self, digits: list[int]):
		r, j = [], True
		for i in range(len(digits) - 1, -1, -1):
			if j:
				v = digits[i] + 1
				if v > 9:
					v -= 10
					j = True
				else:
					j = False
				r.append(v)
			else:
				r.append(digits[i])
		if j:
			r.append(1)
		return r[::-1]


if __name__ == '__main__':
	print(Solution().plusOne([1, 2, 3]))  # [1, 2, 4]
	print(Solution().plusOne([9, 9, 9]))  # [1, 0, 0, 0]
