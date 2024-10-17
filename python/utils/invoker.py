import statistics
import sys
import timeit
from typing import Callable


def serial_call(ops, arglist, module=sys.modules["__main__"]):
	"""
	用于调用 LeetCode 错误信息中使用俩数组表示的输入，例如：
	(操作数组) ["LRUCache","put","put","put","put", "get", "get"]
	(参数列表) [[10], [10,13], [3,17], [6,11], [10,5], [7], [8]]

	:param ops: 操作列表
	:param arglist: 参数列表
	:param module: 模块
	"""
	obj = getattr(module, ops[0])(*arglist[0])

	# 首个调用总是创建对象
	return_values = [None]

	for i in range(1, len(ops)):
		op, args = ops[i], arglist[i]
		try:
			return_values.append(getattr(obj, op)(*args))
		except:
			print(f"第{i}个操作：{op} 出错，参数：{args}", file=sys.stderr)
			raise

	print(return_values)


def benckmark(function: Callable, *args, ratio=1):
	"""
	测试函数的耗时，在控制台中打印相关信息。
	如果被测函数中修改了参数，则args中被修改的那个参数需要改为其对应的工厂函数。

	:param function: 被测函数
	:param args: 被测函数的参数列表
	:param ratio: 循环次数倍率，越大测量越精确，但需要更长的时间
	"""

	def prepare_arguments():
		result = []
		for arg in args:
			if callable(arg):
				result.append(arg())
			else:
				result.append(arg)
		return result

	# 这样做影响是会增大不同参数下的运行时间，特别是有工厂函数时，但对于同样的参数之间的比较则无影响。
	timer = timeit.Timer("function(*prepare_arguments())", globals=locals())

	# noinspection PyUnresolvedReferences
	times = timer.repeat(number=int(timeit.default_number * ratio))
	for usage in times:
		print(round(usage / ratio, 5))

	print(f"平均用时：{round(statistics.mean(times) / ratio, 5)} s/MOps")
