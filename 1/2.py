def main(filepath) -> int:
	with open(filepath) as file:
		data = file.read()
		elf_list = data.split("\n\n")
		top_three = [0,0,0]
		for elf in elf_list:
			curr_total = sum([int(calorie) for calorie in elf.split("\n")])
			if curr_total > top_three[2]:
				top_three.pop(0)
				top_three.insert(2,curr_total)
			elif curr_total > top_three[1]:
				top_three.pop(0)
				top_three.insert(1,curr_total)
			elif curr_total > top_three[0]:
				top_three.pop(0)
				top_three.insert(0,curr_total)
			
		print(sum(top_three))


if __name__ == "__main__":
	filepath: str = "./nums.txt"
	main(filepath)