import re

def main(filepath) -> int:
	with open(filepath) as data:
		curr_line = data.readline()
		num_stacks : int = ((len(curr_line) - 3) // 4) + 1
		stacks = [list() for _ in range(num_stacks)]
		while curr_line[1] != "1":
			for stack_idx in range(num_stacks):
				item_idx = stack_idx * 4 + 1
				item = curr_line[item_idx]
				if item != " ":
					stacks[stack_idx].insert(0,item)
			curr_line = data.readline()
		data.readline()
		curr_line = data.readline()
		while curr_line != '':
			amount,source,dest=[int(num) for num in re.findall(r"[0-9]+",curr_line)]
			for item in stacks[source-1][-amount:]:
				stacks[dest-1].append(item)
			for _ in range(amount):
				stacks[source-1].pop()
			curr_line = data.readline()



		return ''.join([stack[-1] for stack in stacks])
			


		
		
			


if __name__ == "__main__":
	filepath: str = "./data.txt"
	result = main(filepath)
	print(result)