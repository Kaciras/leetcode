import json
import tempfile
import timeit

input_file = "temp/questions.cache.json"


def read_direct():
	with open(input_file) as fp:
		return json.load(fp)


def read_str():
	with open(input_file) as fp:
		return json.loads(fp.read())


def write_direct():
	with open(file, "w") as fp:
		json.dump(data, fp)


def write_str():
	with open(file, "w") as fp:
		fp.write(json.dumps(data))


file = tempfile.mktemp()
data = read_direct()

# 结果显示两种读取性能差不多，先输出str再写入文件性能更好
if __name__ == '__main__':
	print(timeit.timeit("read_direct()", number=1000, globals=locals()))
	print(timeit.timeit("read_str()", number=1000, globals=locals()))

	print(timeit.timeit("write_direct()", number=500, globals=locals()))
	print(timeit.timeit("write_str()", number=500, globals=locals()))

