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

def process_tree(root,dir_list):
	if not root.is_dir:
		return root.size
	root.size = sum([process_tree(child,dir_list) for child in root.children])
	if root.size <= 100000:
		dir_list.add(root)
	return root.size

def main(filepath) -> int:
	with open(filepath) as data:
		root_node = create_tree(data)
		dir_list = set()
		process_tree(root_node,dir_list)
		return sum([dir.size for dir in dir_list])



if __name__ == "__main__":
	filepath: str = "./input.txt"
	result = main(filepath)
	print(result)