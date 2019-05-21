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
	times = timeit.repeat("function(*args)", globals=locals(), number=number)
	for usage in times:
		print(round(usage, 5))
	print(f"平均用时：{round(statistics.mean(times), 5)} 秒/百万次")

	# tracemalloc.start()
	# before = tracemalloc.take_snapshot()
	# function(*args)
	# after = tracemalloc.take_snapshot()
	# tracemalloc.stop()
	#
	# ft = [tracemalloc.Filter(True, __file__)]
	# ttt = after.filter_traces(ft).compare_to(before.filter_traces(ft), "lineno")
	# for stat in ttt:
	# 	print(stat)
