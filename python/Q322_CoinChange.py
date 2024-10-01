class Solution:

	def coinChange(self, coins: list[int], amount: int):
		"""
		动态规划问题常用的填坑法，下标代表能组合出的数（不能组合的为INF），
		数组值代表组合出此数的最少步骤

		这题改用其他语言做了，Python 死活超时......
		"""
		dp = [0x7FFFFFFE] * (amount + 1)
		dp[0] = 0
		coins = set(coins)

		for coin in coins:
			for i in range(coin, amount + 1):
				dp[i] = min(dp[i - coin] + 1, dp[i])

		return dp[amount] if dp[amount] != 0x7FFFFFFE else -1

	def coinChange_0(self, coins: list[int], amount: int):
		"""
		最开始的想法，按照人的思维，先上大的，不行从上一个继续尝试小的，可惜超时了。
		"""
		coins.sort(reverse=True)
		count = 0x7FFFFFFF

		def greedy(value, last, depth):
			nonlocal count
			if value == 0:
				count = min(count, depth)
			if value < 0:
				return
			for coin in coins:
				if coin > last:
					continue
				greedy(value - coin, coin, depth + 1)

		greedy(amount, float("inf"), 0)
		return -1 if count == float("inf") else count


if __name__ == '__main__':
	func = Solution().coinChange

	print(func([176, 6, 366, 357, 484, 226, 1, 104, 160, 331], 5557))
	print(func([399, 313, 460, 317, 401, 173, 116, 17, 121], 7335))
	print(func([125, 146, 125, 252, 226, 25, 24, 308, 50], 8402))
	print(func([84, 457, 478, 309, 350, 349, 422, 469, 100, 432, 188], 6993))
	print(func([3, 7, 405, 436], 8839))
	print(func([186, 419, 83, 408], 6249))  # 20
	print(func([], 3))
	print(func([1, 2, 5], 11))
	print(func([2], 3))
	print(func([1, 2147483647], 2))
