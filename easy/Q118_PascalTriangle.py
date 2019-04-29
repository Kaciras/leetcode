class Solution:
	def generate(self, numRows):
		"""
		:type numRows: int
		:rtype: List[List[int]]
		"""
		result = [[1]]
		for i in range(1, numRows):
			row = [1]
			for j in range(i - 1):
				row.append(result[i - 1][j] + result[i - 1][j + 1])
			row.append(1)
			result.append(row)
		return result


if __name__ == '__main__':
	print(Solution().generate(5))
