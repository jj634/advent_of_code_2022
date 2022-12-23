def main(filepath) -> int:
	with open(filepath) as data:
		message = data.readline()
		result = 0
		for start_idx in range(len(message)):
			if len(set(message[start_idx:start_idx+4])) == 4:
				result = start_idx + 4
				break

		return result

if __name__ == "__main__":
	filepath: str = "./input.txt"
	result = main(filepath)
	print(result)