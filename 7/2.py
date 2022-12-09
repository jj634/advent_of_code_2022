import re

class Node:
	def __init__(self,name,size,parent,is_dir):
		self.name = name
		self.size = size
		self.children = set()
		self.parent = parent
		self.is_dir = is_dir
	def add_child(self,n):
		self.children.add(n)

def create_tree(data):
	root_node = Node("/",-1,None,True)
	curr_node = root_node
	curr_line = data.readline()
	while curr_line != "":
		if curr_line[:4] == "$ cd":
			dest = curr_line[5:-1]
			if dest == "..":
				if curr_node.name == "/":
					raise Exception("Root doesn't have a parent")
				curr_node = curr_node.parent
			elif dest == "/":
				curr_node = root_node
			else:
				for child in curr_node.children:
					if child.name == dest:
						curr_node = child
						break
				if curr_node.name != dest:
					raise Exception("Dest not found")
			curr_line = data.readline()
		elif curr_line[:4] == "$ ls":
			curr_line = data.readline()
			while curr_line != "" and curr_line[0] != "$":
				first,second = curr_line.split(" ")
				second=second[:-1]
				if first.isdigit(): # file
					curr_node.add_child(Node(second,int(first),curr_node,False))
				else: # dir
					curr_node.add_child(Node(second,-1,curr_node,True))
				curr_line = data.readline()
	while curr_node.name != "/":
		curr_node = curr_node.parent
	return curr_node

def size_tree(root):
	if not root.is_dir:
		return root.size
	root.size = sum([size_tree(child) for child in root.children])
	return root.size

def find_min(root,del_min,curr_min):
	if root.size >= del_min:
		curr_min = min(curr_min,root.size)
		dir_children = [child for child in root.children if child.is_dir]
		for child in dir_children:
			curr_min = min(curr_min,find_min(child,del_min,curr_min))
		return curr_min
	return curr_min


def main(filepath) -> int:
	with open(filepath) as data:
		total_size = 70000000
		space_needed = 30000000
		
		root_node = create_tree(data)
		size_tree(root_node)
		del_min = space_needed - (total_size - root_node.size)
		curr_min = root_node.size
		return find_min(root_node,del_min,curr_min)




if __name__ == "__main__":
	filepath: str = "./input.txt"
	result = main(filepath)
	print(result)