class Solution:
	"""可以使用一个辅助数组，代码较少。本例使用直接交换法"""
	
	def rotate(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: void Do not return anything, modify matrix in-place instead.
		"""
		i, t = 0, 0
		while i + i < len(matrix):
			for j in range(i, len(matrix) - i - 1):
				t = matrix[i][j]
				matrix[i][j] = matrix[len(matrix) - 1 - j][i]
				matrix[len(matrix) - 1 - j][i] = matrix[len(matrix) - 1 - i][len(matrix) - 1 - j]
				matrix[len(matrix) - 1 - i][len(matrix) - 1 - j] = matrix[j][len(matrix) - 1 - i]
				matrix[j][len(matrix) - 1 - i] = t
			i += 1


def test(matrix):
	Solution().rotate(matrix)
	print(matrix)


if __name__ == '__main__':
	test([
		[5, 1, 9, 11],
		[2, 4, 8, 10],
		[13, 3, 6, 7],
		[15, 14, 12, 16]
	])
	test([
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]
	])
