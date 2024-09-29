from utils import benckmark


class Solution:
	"""保存 prev 为局部变量，耗时降低了0.9秒/百万次"""

	def generate(self, numRows: int):
		result = [[1]]
		for i in range(1, numRows):
			row, prev = [1], result[i - 1]
			for j in range(i - 1):
				row.append(prev[j] + prev[j + 1])
			row.append(1)
			result.append(row)
		return result


if __name__ == '__main__':
	print(Solution().generate(5))
	benckmark(Solution().generate, 6)
