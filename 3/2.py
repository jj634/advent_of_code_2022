import re

def main(filepath) -> int:
	with open(filepath) as file:
		data = file.read()
		rucksacks = data.split("\n")
		calc_item_priority = lambda type : ord(type)-ord('A') + 27 if type.isupper() else ord(type)-ord('a')+1
		total = 0
		for rucksacks_idx in range(len(rucksacks)//3):
			seen = [[0] * 52,[0] * 52,[0] * 52] # i hate python
			group=rucksacks[rucksacks_idx*3:(rucksacks_idx*3)+3]
			for group_idx in range(3):
				rucksack = group[group_idx]
				for item in rucksack:
					item_priority = calc_item_priority(item)
					seen[group_idx][item_priority-1] = 1
			for priority in range(1,53):
				if seen[0][priority-1] and seen[1][priority-1] and seen[2][priority-1]:
					total += priority
					break

		return total



if __name__ == "__main__":
	filepath: str = "./rucksacks.txt"
	result = main(filepath)
	print(result)