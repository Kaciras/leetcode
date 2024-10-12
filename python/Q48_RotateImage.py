class Solution:
	"""可以使用一个辅助数组，代码较少。本例使用直接交换法"""

	def rotate(self, matrix: list[list[int]]):
		t, n = 0, len(matrix)
		# 顶部的循环是层数，总共为边长的一半，奇数最中间只有一个无需旋转。
		for i in range(n // 2):
			# 每一层按边长循环，依次交换四个角
			for j in range(i, n - i - 1):
				t = matrix[i][j]
				matrix[i][j] = matrix[n - 1 - j][i]
				matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
				matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
				matrix[j][n - 1 - i] = t


def test_example1():
	matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	Solution().rotate(matrix)
	assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]


def test_example2():
	matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
	Solution().rotate(matrix)
	assert matrix == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
