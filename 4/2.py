import re

def main(filepath) -> int:
	with open(filepath) as pairs:
		total = 0
		for pair in pairs:
			pair_ranges = [int(num) for num in re.split(r"-|,",pair)]
			first_elf_start,first_elf_end,second_elf_start,second_elf_end = pair_ranges
			first_start_contained = second_elf_start <= first_elf_start <= second_elf_end
			second_start_contained = first_elf_start <= second_elf_start <= first_elf_end
			if first_start_contained or second_start_contained:
				total += 1
		return total


if __name__ == "__main__":
	filepath: str = "./pairs.txt"
	result = main(filepath)
	print(result)