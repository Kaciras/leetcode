import statistics
import sys
import timeit


def serial_call(ops, arglist, module=sys.modules["__main__"]):
	"""
	用于调用LeetCode错误信息中使用俩数组表示的输入，例如：
	(操作数组) ["LRUCache","put","put","put","put", "get", "get"]
	(参数列表) [[10], [10,13], [3,17], [6,11], [10,5], [7], [8]]

	:param ops: 操作列表
	:param arglist: 参数列表
	:param module: 模块
	:return: 迭代器，包含每一次调用的返回值
	"""
	obj = getattr(module, ops[0])(*arglist[0])

	for i in range(1, len(ops)):
		op, args = ops[i], arglist[i]
		try:
			yield getattr(obj, op)(*args)
		except:
			print(f"第{i}个操作：{op} 出错，参数：{args}", file=sys.stderr)
			raise


def benckmark(function, *args, number=timeit.default_number):
	"""
	测试函数的耗时，在控制台中打印相关信息。

	如果被测函数中修改了参数，则args中被修改的那个参数需要改为其对应的工厂函数。

	:param function: 被测函数
	:param args: 被测函数的参数列表
	:param number: 测量循环次数
	"""

	def prepare_arguments():
		result = []
		for arg in args:
			if callable(arg):
				result.append(arg())
			else:
				result.append(arg)
		return result

	# 这里只能把 prepare_arguments 也算入耗时中。因为如果要在每次迭代都去 setup，那么代码应该类似：
	#
	#   total_time = 0
	#   for _ in range(...):
	#   	args = prepare_arguments()
	#   	_t0 = perf_counter()
	#   	function(*args)
	#   	total_time += perf_counter() - _t0
	#   return total_time
	#
	# 由于被测函数通常都不会用时很长，这么一来两次计时(perf_counter)时间过于接近，从而产生较大的误差。
	# 故只能把两次计时放在循环外，这样一来也就没办法排除 prepare_arguments 的时间。
	timer = timeit.Timer("function(*prepare_arguments())", globals=locals())

	times = timer.repeat(number=number)
	for usage in times:
		print(round(usage, 5))
	print(f"平均用时：{round(statistics.mean(times), 5)} 秒/百万次")
