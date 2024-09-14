"""
辅助模块，包含构建链表、二叉树，打印数据结构到控制台等便捷方法
"""
from .binary_tree import *
from .invoker import *
from .linked_list import *


def print_martix(martix):
	print("[")
	for row in martix:
		print("\t[" + ", ".join(map(str, row)) + "]")
	print("]")
