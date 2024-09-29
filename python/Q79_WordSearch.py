class Solution:
	def exist(self, board: list[list[str]], word: str):
		if not word:
			return True

		# 也可以直接修改 board[i][j] = None 来屏蔽访问过的元素
		visited = [[False] * len(board[0]) for _ in range(len(board))]

		def find(i, j, s_index):
			if visited[i][j]:
				return False
			if s_index == len(word):
				return True
			visited[i][j] = True
			char, next_ = word[s_index], []

			# 可以把范围的判断放到最前面
			if i > 0: next_.append((i - 1, j))
			if i < len(visited) - 1: next_.append((i + 1, j))
			if j > 0: next_.append((i, j - 1))
			if j < len(visited[0]) - 1: next_.append((i, j + 1))

			for x, y in next_:
				if board[x][y] == word[s_index] and find(x, y, s_index + 1):
					return True
			visited[i][j] = False
			return False

		for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j] == word[0] and find(i, j, 1):
						return True
		return False


if __name__ == '__main__':
	board1 = [
		['A', 'B', 'C', 'E'],
		['S', 'F', 'C', 'S'],
		['A', 'D', 'E', 'E']
	]
	print(Solution().exist(board1, "ABCB"))
	print(Solution().exist(board1, ""))
	print(Solution().exist(board1, "ABCCED"))
	print(Solution().exist(board1, "SEE"))

	print(Solution().exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))
