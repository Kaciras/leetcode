class Solution:
	def isValidSudoku(self, board: list[list[str]]):
		rows = [{} for _ in range(9)]
		columns = [{} for _ in range(9)]
		blocks = [{} for _ in range(9)]

		for i in range(9):
			for j in range(9):
				num = board[i][j]
				if not num.isdigit():
					continue

				if rows[i].__contains__(num):
					return False
				rows[i][num] = True

				if columns[j].__contains__(num):
					return False
				columns[j][num] = True

				index = j // 3 * 3 + i // 3
				if blocks[index].__contains__(num):
					return False
				blocks[index][num] = True
		return True


if __name__ == '__main__':
	print(Solution().isValidSudoku([
		["5", "3", ".", ".", "7", ".", ".", ".", "."],
		["6", ".", ".", "1", "9", "5", ".", ".", "."],
		[".", "9", "8", ".", ".", ".", ".", "6", "."],
		["8", ".", ".", ".", "6", ".", ".", ".", "3"],
		["4", ".", ".", "8", ".", "3", ".", ".", "1"],
		["7", ".", ".", ".", "2", ".", ".", ".", "6"],
		[".", "6", ".", ".", ".", ".", "2", "8", "."],
		[".", ".", ".", "4", "1", "9", ".", ".", "5"],
		[".", ".", ".", ".", "8", ".", ".", "7", "9"]
	]))
	print(Solution().isValidSudoku([
		["8", "3", ".", ".", "7", ".", ".", ".", "."],
		["6", ".", ".", "1", "9", "5", ".", ".", "."],
		[".", "9", "8", ".", ".", ".", ".", "6", "."],
		["8", ".", ".", ".", "6", ".", ".", ".", "3"],
		["4", ".", ".", "8", ".", "3", ".", ".", "1"],
		["7", ".", ".", ".", "2", ".", ".", ".", "6"],
		[".", "6", ".", ".", ".", ".", "2", "8", "."],
		[".", ".", ".", "4", "1", "9", ".", ".", "5"],
		[".", ".", ".", ".", "8", ".", ".", "7", "9"]
	]))
