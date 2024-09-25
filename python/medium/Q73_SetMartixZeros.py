from utils import print_martix

class Solution:
	def setZeroes(self, matrix: list[list[int]]):
		clear_first = 0 in matrix[0]
		clear_this = False

		for i in range(1, len(matrix)):

			# 扫每行，记录要清的列，以及改行是否要清。
			for j in range(0, len(matrix[0])):
				if matrix[i][j] == 0:
					clear_this = True
					matrix[0][j] = 0

			# 一行扫完再就可以清理该行了。
			if clear_this:
				matrix[i][:] = [0] * len(matrix[0])
				clear_this = False

		# 扫完了，开始清理列。
		for j in range(0, len(matrix[0])):
			if matrix[0][j] == 0:
				for i in range(len(matrix)):
					matrix[i][j] = 0

		# 最后清理用来记录列的第一行。
		if clear_first:
			matrix[0][:] = [0] * len(matrix[0])


def test(martix):
	Solution().setZeroes(martix)
	print_martix(martix)


if __name__ == '__main__':
	test([
		[0, 1, 2, 0],
		[3, 4, 5, 2],
		[1, 3, 1, 5]
	])
	test([[]])
