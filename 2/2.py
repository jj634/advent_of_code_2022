def main(filepath) -> int:
	win_conds = [2,0,1]

	with open(filepath) as file:
		data = file.read()
		rounds = data.split("\n")
		total = 0
		for round in rounds:
			opp = ord(round[0])-ord("A")
			result = ord(round[2])-ord("X")
			if result == 0: # loss
				total += win_conds[opp] + 1 + result
			elif result == 1: # draw
				total += (opp + 1) + 3
			else: # win
				total += (win_conds.index(opp) + 1) + 6
		return total


if __name__ == "__main__":
	filepath: str = "./strategy_guide.txt"
	result = main(filepath)
	print(result)