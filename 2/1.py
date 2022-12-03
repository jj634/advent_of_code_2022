def main(filepath) -> int:
	win_conds = [2,0,1]

	with open(filepath) as file:
		data = file.read()
		rounds = data.split("\n")
		total = 0
		for round in rounds:
			opp = ord(round[0])-ord("A")
			me = ord(round[2])-ord("X")
			if opp == me: # draw
				total += (me + 1) + 3
			elif win_conds[me] == opp: # win
				total += (me + 1) + 6
			else: # draw
				total += (me + 1) + 0
		return total


if __name__ == "__main__":
	filepath: str = "./strategy_guide.txt"
	result = main(filepath)
	print(result)