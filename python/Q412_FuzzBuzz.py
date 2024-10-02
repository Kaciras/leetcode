class Solution:

	def fizzBuzz(self, n: int):
		result = [""] * n
		while n > 0:
			if n % 15 == 0:
				result[n - 1] = "FizzBuzz"
			elif n % 3 == 0:
				result[n - 1] = "Fizz"
			elif n % 5 == 0:
				result[n - 1] = "Buzz"
			else:
				result[n - 1] = str(n)
			n -= 1
		return result


if __name__ == '__main__':
	print(Solution().fizzBuzz(15))
