class Solution:
	"""TODO 组合数"""

	def uniquePaths(self, m, n):
		paths = [1] * n
		for i in range(1, m):
			for j in range(1, n):
				paths[j] = paths[j] + paths[j - 1]
		return paths[-1]

	def uniquePaths_0(self, m, n):
		"""
		:type m: int
		:type n: int
		:rtype: int
		"""
		visited = [[0] * m for _ in range(n)]

		def find(x, y):
			if x == 0 and y == 0:
				return 1
			if visited[y][x]:
				return visited[y][x]

			paths = 0
			if x > 0:
				paths += find(x - 1, y)
			if y > 0:
				paths += find(x, y - 1)

			visited[y][x] = paths
			return paths

		return find(m - 1, n - 1)

if __name__ == '__main__':
	print(Solution().uniquePaths(2, 2))
	print(Solution().uniquePaths(3, 2))
	print(Solution().uniquePaths(7, 3))
