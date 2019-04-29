class Solution:

	def reverseBits(self, n):
		"""使用二进制字符串来翻转"""
		b = bin(n)[2:]
		b = "0" * (32 - len(b)) + b
		return int(b[::-1], 2)

	def reverseBits_2(self, n):
		"""不依赖任何语言特性的实现"""
		n = (n & 0xAAAAAAAA) >> 1 | (n & 0x55555555) << 1
		n = (n & 0xCCCCCCCC) >> 2 | (n & 0x33333333) << 2
		n = (n & 0xF0F0F0F0) >> 4 | (n & 0x0F0F0F0F) << 4
		n = (n & 0xFF00FF00) >> 8 | (n & 0x00FF00FF) << 8
		return (n & 0xFFFF0000) >> 16 | (n & 0x0000FFFF) << 16


if __name__ == '__main__':
	print(Solution().reverseBits(43261596))  # 964176192
