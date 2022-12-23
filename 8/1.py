def compute_maxes(forest):
	forest_height = len(forest)
	forest_width = len(forest[0])
	
	left_maxes = [[-1]*forest_width for _ in range(forest_height)]
	for i in range(1,forest_height-1):
		left_max = forest[i][0]
		for j in range(1,forest_width-1):
			left_max = max(left_max,forest[i][j-1])
			left_maxes[i][j] = left_max
	
	
	right_maxes = [[-1]*forest_width for _ in range(forest_height)]
	for i in range(1,forest_height-1):
		right_max = forest[i][forest_width-1]
		for j in range(forest_width-2,0,-1):
			right_max = max(right_max,forest[i][j+1])
			right_maxes[i][j] = right_max

	
	top_maxes = [[-1]*forest_width for _ in range(forest_height)]
	for j in range(1,forest_width-1):
		top_max = forest[0][j]
		for i in range(1,forest_height-1):
			top_max = max(top_max,forest[i-1][j])
			top_maxes[i][j] = top_max

	bottom_maxes = [[-1]*forest_width for _ in range(forest_height)]
	for j in range(1,forest_width-1):
		bottom_max = forest[forest_height-1][j]
		for i in range(forest_height-2,0,-1):
			bottom_max = max(bottom_max,forest[i+1][j])
			bottom_maxes[i][j] = bottom_max

	min_maxes = [[-1]*forest_width for _ in range(forest_height)]
	for i in range(1,forest_height-1):
		for j in range(1,forest_width-1):
			min_maxes[i][j] = min(left_maxes[i][j],right_maxes[i][j],top_maxes[i][j],bottom_maxes[i][j])

	return min_maxes

def main(filepath) -> int:
	with open(filepath) as data:
		data_rows = data.read().split("\n")
		forest = [[int(row[i]) for i in range(len(row))]for row in data_rows]
		min_maxes = compute_maxes(forest)
		forest_height = len(forest)
		forest_width = len(forest[0])
		visible = (forest_height + forest_width - 2) * 2
		for i in range(1,forest_height-1):
			for j in range(1,forest_width-1):
				if forest[i][j] > min_maxes[i][j]:
					visible += 1
		return visible

if __name__ == "__main__":
	filepath: str = "./input.txt"
	result = main(filepath)
	print(result)