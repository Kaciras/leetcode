from functools import cmp_to_key
from typing import List


class Solution:

	# 妈的玄学测速，这个答案竟然才超过 30% 运行时间
	def merge(self, intervals: List[List[int]]) -> List[List[int]]:
		if not intervals:
			return []
		intervals.sort(key=lambda x: x[0])
		result = [intervals[0]]

		for interval in intervals[1:]:
			merged = result[-1]
			if interval[0] > merged[1]:
				result.append(interval)
			else:
				merged[1] = max(interval[1], merged[1])

		return result

	# 虽然原始的做法里，双属性排序是多余的，不过也学到了个 cmp_to_key 函数
	def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
		if not intervals:
			return []

		intervals.sort(key=cmp_to_key(compare))
		result = []
		merged = intervals[0]

		for interval in intervals[1:]:

			if interval[0] > merged[1]:
				result.append(merged)
				merged = interval

			elif interval[1] > merged[1]:
				merged[1] = interval[1]

		result.append(merged)
		return result


def compare(a, b):
	left = a[0] - b[0]
	if left != 0:
		return left
	return b[1] - a[1]


if __name__ == '__main__':
	data = [[1, 3], [2, 6], [8, 10], [15, 18]]
	print(Solution().merge(data))  # [[1,6],[8,10],[15,18]]

	data = [[1, 4], [4, 5]]
	print(Solution().merge(data))  # [[1,5]]

	data = [[1, 4], [1, 5]]
	print(Solution().merge(data))  # [[1,5]]
