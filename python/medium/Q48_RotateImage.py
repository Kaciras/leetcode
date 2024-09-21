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
