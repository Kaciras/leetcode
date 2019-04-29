class Solution:
	def exist(self, board, word):
		"""
		:type board: List[List[str]]
		:type word: str
		:rtype: bool
		"""
		if not word:
			return True

		# 对于题目而言，也可以直接修改 board[i][j] = None 来屏蔽访问过的元素
		visited = [[False] * len(board[0]) for _ in range(len(board))]

		def find(i, j, sindex):
			if visited[i][j]:
				return False
			if sindex == len(word):
				return True
			visited[i][j] = True
			char, next_ = word[sindex], []

			# 可以把范围的判断放到最前面
			if i > 0: next_.append((i - 1, j))
			if i < len(visited) - 1: next_.append((i + 1, j))
			if j > 0: next_.append((i, j - 1))
			if j < len(visited[0]) - 1: next_.append((i, j + 1))

			for x, y in next_:
				if board[x][y] == word[sindex] and find(x, y, sindex + 1):
					return True
			visited[i][j] = False
			return False

		for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j] == word[0] and find(i, j, 1):
						return True
		return False


if __name__ == '__main__':
	board = [
		['A', 'B', 'C', 'E'],
		['S', 'F', 'C', 'S'],
		['A', 'D', 'E', 'E']
	]
	print(Solution().exist(board, "ABCB"))
	print(Solution().exist(board, ""))
	print(Solution().exist(board, "ABCCED"))
	print(Solution().exist(board, "SEE"))

	print(Solution().exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))
