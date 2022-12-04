import re

def main(filepath) -> int:
	with open(filepath) as pairs:
		total = 0
		for pair in pairs:
			pair_ranges = [int(num) for num in re.split(r"-|,",pair)]
			first_elf_start,first_elf_end,second_elf_start,second_elf_end = pair_ranges
			first_fully_contains = first_elf_start <= second_elf_start and first_elf_end >= second_elf_end
			second_fully_contains = second_elf_start <= first_elf_start and second_elf_end >= first_elf_end
			if first_fully_contains or second_fully_contains:
				total += 1
		return total


if __name__ == "__main__":
	filepath: str = "./pairs.txt"
	result = main(filepath)
	print(result)