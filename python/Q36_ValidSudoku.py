from itertools import product


class Solution:
	def isValidSudoku(self, board: list[list[str]]):
		rows = [{} for _ in range(9)]
		columns = [{} for _ in range(9)]
		blocks = [{} for _ in range(9)]

		for i, j in product(range(9), range(9)):
			# 如果格子不是数字就跳过
			num = board[i][j]
			if not num.isdigit():
				continue

			# 检查行是否有重复的
			if rows[i].__contains__(num):
				return False
			rows[i][num] = True

			# 检查列是否有重复的
			if columns[j].__contains__(num):
				return False
			columns[j][num] = True

			# 检查 3x3 块内是否有重复的
			index = j // 3 * 3 + i // 3
			if blocks[index].__contains__(num):
				return False
			blocks[index][num] = True

		return True


def test_example1():
	assert Solution().isValidSudoku([
		["5", "3", ".", ".", "7", ".", ".", ".", "."],
		["6", ".", ".", "1", "9", "5", ".", ".", "."],
		[".", "9", "8", ".", ".", ".", ".", "6", "."],
		["8", ".", ".", ".", "6", ".", ".", ".", "3"],
		["4", ".", ".", "8", ".", "3", ".", ".", "1"],
		["7", ".", ".", ".", "2", ".", ".", ".", "6"],
		[".", "6", ".", ".", ".", ".", "2", "8", "."],
		[".", ".", ".", "4", "1", "9", ".", ".", "5"],
		[".", ".", ".", ".", "8", ".", ".", "7", "9"]
	])


def test_example2():
	assert not Solution().isValidSudoku([
		["8", "3", ".", ".", "7", ".", ".", ".", "."],
		["6", ".", ".", "1", "9", "5", ".", ".", "."],
		[".", "9", "8", ".", ".", ".", ".", "6", "."],
		["8", ".", ".", ".", "6", ".", ".", ".", "3"],
		["4", ".", ".", "8", ".", "3", ".", ".", "1"],
		["7", ".", ".", ".", "2", ".", ".", ".", "6"],
		[".", "6", ".", ".", ".", ".", "2", "8", "."],
		[".", ".", ".", "4", "1", "9", ".", ".", "5"],
		[".", ".", ".", ".", "8", ".", ".", "7", "9"]
	])
