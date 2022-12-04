def main(filepath) -> int:
	with open(filepath) as file:
		data = file.read()
		rucksacks = data.split("\n")
		total = 0
		calc_item_priority = lambda type : ord(type)-ord('A') + 27 if type.isupper() else ord(type)-ord('a')+1
		for rucksack in rucksacks:
			seen = [0] * 52
			for item in rucksack[:len(rucksack)//2]:
				item_priority = calc_item_priority(item)
				seen[item_priority-1] = 1
			for item in rucksack[len(rucksack)//2:]:
				item_priority = calc_item_priority(item)
				if seen[item_priority-1]:
					total += item_priority
					break
		
		return total



if __name__ == "__main__":
	filepath: str = "./rucksacks.txt"
	result = main(filepath)
	print(result)