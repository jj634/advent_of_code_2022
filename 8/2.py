def traverse(forest, start, step_fn):
	view_dist = 1
	start_height = forest[start[0]][start[1]]
	next_pos = step_fn(start)
	on_edge = lambda pos : pos[0] == 0 or pos[1] == 0 or pos[0] == len(forest)-1 or pos[1] == len(forest[0])-1

	on_taller = lambda pos : forest[pos[0]][pos[1]] >= start_height
	while not (on_taller(next_pos) or on_edge(next_pos)):
		view_dist += 1
		next_pos = step_fn(next_pos)
	return view_dist

def main(filepath) -> int:
	with open(filepath) as data:
		data_rows = data.read().split("\n")
		forest = [[int(row[i]) for i in range(len(row))]for row in data_rows]
		forest_height = len(forest)
		forest_width = len(forest[0])
		directions = [(0,1),(0,-1),(1,0),(-1,0)]
		max_scenic_score = -1
		for i in range(1,forest_height-1):
			for j in range(1,forest_width-1):
				scenic_score = 1
				for direction in directions:
					step_fn = lambda pos : (pos[0] + direction[0], pos[1] + direction[1])
					scenic_score *= traverse(forest,(i,j),step_fn)
				max_scenic_score = max(scenic_score, max_scenic_score)
		return max_scenic_score

if __name__ == "__main__":
	filepath: str = "./input.txt"
	result = main(filepath)
	print(result)