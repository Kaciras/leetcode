"""
辅助模块，包含构建链表、二叉树，打印数据结构到控制台等便捷方法
"""
from utils.linkedlist import *
from utils.bintree import *


def print_martix(martix):
	print("[")
	for row in martix:
		print("\t[" + ", ".join(map(str, row)) + "]")
	print("]")
