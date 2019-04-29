import aiohttp
import asyncio
import colorama
import json
import os
import string
import sys
import time

colorama.init(autoreset=True)

level_names = ["", "easy", "medium", "hard"]

CACHE_FILE = "questions.cache.json"


async def get_questions():
	"""先查看本地缓存的题目列表，没有或者一星期没更新就去网上抓"""
	if "-online" not in sys.argv and os.path.exists(CACHE_FILE):
		if os.stat(CACHE_FILE).st_mtime > (time.time() - 86400 * 7):
			return json.load(open(CACHE_FILE, "r"))

	questions = await get_questions_online()
	json.dump(questions, open(CACHE_FILE, "w"))
	return questions


async def get_questions_online():
	"""抓取所有题目列表"""
	print("从网站上下载题目列表...")

	def extract(p):
		stat, lv = p["stat"], p["difficulty"]["level"]
		title, stitle = stat["question__title"], stat["question__title_slug"]
		return {"name": process_title(title), "level": int(lv), }

	async with aiohttp.ClientSession() as session:
		async with session.get('https://leetcode-cn.com/api/problems/all/') as resp:
			data = await resp.json(content_type="text/html")

			questions = {}
			print(f"download from leetcode-cn, total questions：{data['num_total']}")

			for pair in data['stat_status_pairs']:
				questions[pair["stat"]["question_id"]] = extract(pair)
			return questions


def process_title(text):
	"""从网站采集的题目可能含有无法作为Python模块名的字符，需要去掉"""

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
	if not os.path.exists("0.py"):
		return print('unnamed file should be named "0.py"')
	print("please enter question id：", end="")
	id_ = input()

	question = (await get_questions())[id_]
	new_path = f"{level_names[question['level']]}/Q{id_}_{question['name']}.py"
	os.rename("0.py", new_path)
	print("rename 0.py to：" + new_path)


async def statistic_mode():
	easy, medium, hard = os.listdir("easy"), os.listdir("medium"), os.listdir("hard")
	total = easy + medium + hard

	print(f"题目数量({len(total)})：Easy - {len(easy)}，Medium - {len(medium)}，Hard - {len(hard)}")


# asyncio.get_event_loop().set_debug(True)

if __name__ == '__main__':
	queue = list(reversed(sys.argv[1:]))
	cmd = queue.pop()

	if cmd == "-R":  # 改名模式
		asyncio.get_event_loop().run_until_complete(rename_mode())
	elif cmd == "-S":  # 统计模式
		asyncio.get_event_loop().run_until_complete(statistic_mode())
	elif cmd == "-C":  # 命名检查模式
		asyncio.get_event_loop().run_until_complete(check())
