def main(filepath) -> int:
	with open(filepath) as file:
		data = file.read()
		elf_list = data.split("\n\n")
		max_elf = 0
		for elf in elf_list:
			curr_total = sum([int(calorie) for calorie in elf.split("\n")])
			max_elf = max(max_elf,curr_total)
			
		print(max_elf)


if __name__ == "__main__":
	filepath: str = "./nums.txt"
	main(filepath)