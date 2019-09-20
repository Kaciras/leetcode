import asyncio
import json
import os
import string
import sys
from datetime import datetime, date, timedelta

import aiohttp
import colorama

colorama.init(autoreset=True)

level_names = ["", "easy", "medium", "hard"]

CACHE_FILE = "temp/questions.cache.json"


async def get_questions():
	"""先查看本地缓存的题目列表，没有或者一星期没更新就去网上抓"""

	if "-online" not in sys.argv and os.path.exists(CACHE_FILE):

		# LeetCode 在每周末的中午12点结束比赛，同时公开比赛题目
		dof = (date.today().weekday() + 1) % 7
		last_sunday = datetime.now() - timedelta(days=dof)
		last_update = last_sunday.replace(hour=12, minute=0, second=0, microsecond=0)
		ts = (last_update - datetime.fromtimestamp(0)).total_seconds()

		if os.stat(CACHE_FILE).st_mtime > ts:
			print("使用缓存的题库")
			with open(CACHE_FILE, "r") as fp:
				return json.load(fp)

	print("从LeetCode中文站下载题库")
	questions = await get_questions_online()
	with open(CACHE_FILE, "w") as fp:
		json.dump(questions, fp)

	return questions


async def get_questions_online():
	"""抓取所有题目列表"""

	def extract(item):
		stat, lv = item["stat"], item["difficulty"]["level"]
		title, stitle = stat["question__title"], stat["question__title_slug"]
		return {"name": process_title(title), "level": int(lv), }

	async with aiohttp.ClientSession() as session:
		async with session.get('https://leetcode-cn.com/api/problems/all/') as resp:
			questions = {}
			data = await resp.json(content_type="text/html")
			print("从LeetCode中文站下载问题列表，总计：" + str(data['num_total']))

			for pair in data['stat_status_pairs']:
				questions[pair["stat"]["question_id"]] = extract(pair)

			return questions


def process_title(text):
	"""从网站采集的题目可能含有无法作为Python模块名的字符，需要处理一下"""

	# 去除所有的标点符号
	text = text.translate(str.maketrans("", "", string.punctuation))

	# 题目名是以空格分隔单词的，分别对每一个单词处理
	parts, results = text.strip().split(" "), []
	for part in parts:

		# 过滤掉空白的字符串（原字符串中连续的空白字符）
		if not part:
			continue

		# 每个单词首字母大写，变为驼峰式命名
		if part[0] in string.ascii_lowercase:
			part = part[0].upper() + part[1:]

		results.append(part)

	return "".join(results)


async def check():
	col = {
		"easy": colorama.Fore.GREEN + "easy",
		"medium": colorama.Fore.YELLOW + "medium",
		"hard": colorama.Fore.RED + "hard"
	}
	questions = await get_questions()

	def check_dir(level):
		ln = level_names[level]

		for file in sorted(os.listdir(ln)):
			id_, name = file.split("_")
			name = name[:-3]
			q = questions[int(id_)]
			errors = []

			if q["name"] != name:
				errors.append(f"文件名：{name}，建议名：Q{q['name']}")
			if q["level"] != level:
				errors.append(f"难度：{col[ln]}，题目难度{level_names[int(q['level'])]}")

			if errors:
				print(id_ + " " + "；".join(errors))

	check_dir(1)
	check_dir(2)
	check_dir(3)


async def rename_mode():
	"""重命名功能，自动查找问题的难度和名字，将临时文件 0.py 移动到合适的目录"""
	if not os.path.exists("0.py"):
		return print('unnamed file should be named "0.py"')

	questions = await get_questions()

	print(colorama.Fore.LIGHTYELLOW_EX + "输入问题的ID：", end="")
	id_ = input().strip()

	if id_ not in questions:
		return print(colorama.Fore.LIGHTRED_EX + "在题库中找不到指定ID的问题")

	lv, name = questions[id_]['level'], questions[id_]['name']
	new_path = f"{level_names[lv]}/Q{id_}_{name}.py"

	os.rename("0.py", new_path)
	os.system("git add " + new_path)
	print(colorama.Fore.LIGHTBLUE_EX + "归档新的解答：" + new_path)


async def statistic_mode():
	easy, medium, hard = os.listdir("easy"), os.listdir("medium"), os.listdir("hard")
	total = easy + medium + hard

	print(f"题目数量({len(total)})：Easy - {len(easy)}，Medium - {len(medium)}，Hard - {len(hard)}")


if __name__ == '__main__':
	queue = list(reversed(sys.argv[1:]))
	cmd = queue.pop()
	# asyncio.get_event_loop().set_debug(True)

	if cmd == "-R":  # 改名模式
		asyncio.get_event_loop().run_until_complete(rename_mode())
	elif cmd == "-S":  # 统计模式
		asyncio.get_event_loop().run_until_complete(statistic_mode())
	elif cmd == "-C":  # 命名检查
		asyncio.get_event_loop().run_until_complete(check())
