from utils import print_martix

class Solution:
	def setZeroes(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: void Do not return anything, modify matrix in-place instead.
		"""
		clear_first = 0 in matrix[0]
		clear_this = False

		for i in range(1, len(matrix)):
			for j in range(0, len(matrix[0])):
				if matrix[i][j] == 0:
					clear_this = True
					matrix[0][j] = 0
			if clear_this:
				matrix[i][:] = [0] * len(matrix[0])
			clear_this = False
		for j in range(0, len(matrix[0])):
			if matrix[0][j] == 0:
				for i in range(len(matrix)):
					matrix[i][j] = 0
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
