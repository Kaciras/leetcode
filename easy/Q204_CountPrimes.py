import math

class Solution:

	def countPrimes(self, n):
		if n < 3:
			return 0
		arr = [1] * n
		for i in range(2, int(math.sqrt(n)) + 1):
			if arr[i]:
				arr[i + i: n: i] = [0] * len(arr[i + i:n:i])
		return sum(arr) - 2

	def countPrimes_old(self, n):
		"""
		这个方法超时了，但是无需额外空间
		"""
		if n < 3:
			return 0

		count = 1
		for i in range(3, n, 2):
			valid = True
			s = math.ceil(math.sqrt(i))

			while s > 2:
				if i % s == 0:
					valid = False
					break
				s -= 1
			if valid:
				count += 1

		return count


if __name__ == '__main__':
	print(Solution().countPrimes(2))
	print(Solution().countPrimes(10))
	print(Solution().countPrimes(100))
