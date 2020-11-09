# ---------------------------- Trees -------------------------------

import operator

def binary_tree(value):
	''' Make new tree '''
	return [value, [], []]

def insert_left(root, subtree):
	''' Insert subtree into the left branch '''
	root.pop(1)
	root.insert(1, subtree)

def insert_right(root, subtree):
	''' Insert subtree into the right branch '''
	root.pop(2)
	root.insert(2, subtree)


def get_root_value(root):
	''' Get root value in the node root '''
	return root[0]

def get_left_child(root):
	return root[1]

def get_right_child(root):
	return root[2]

def print_exp(tree):
	''' Printing the expression tree in a readable form '''
	value = ''
	if tree:
		if get_left_child(tree):
			value = '(' + print_exp(get_left_child(tree))
		value = value + str(get_root_value(tree))
		if get_right_child(tree):
			value = value + print_exp(get_right_child(tree)) + ')'
	return value


def postorder_evaluate(exp):
	ops = {
		'+': operator.add,
		'-': operator.sub,
		'*': operator.mul,
		'/': operator.truediv,
		'%': operator.mod,
		'^': operator.pow
	}

	res1 = None
	res2 = None

	if exp:
		res1 = postorder_evaluate(get_left_child(exp))
		res2 = postorder_evaluate(get_right_child(exp))
		if res1 and res2:
			return ops[get_root_value(exp)](res1, res2)
		else:
			return get_root_value(exp)



signs = ('+', '-', '*', '/', '^', '%')

def build_exp_tree(st):
	''' Build the expression tree from the st string '''

	# Base case - if str is a number - return end node
	if st >= '0' and st <= '9': # if st is a number...
		return [int(st), [], []]

	# else - divide expression in two parts

	br = 0  # Number open uncompleted brackets
	idx = 1 # Index of the sign that divide expression into two parts

	# If all brackets are closed and current symbol is a sign - find the sign
	while True:
		if br == 0 and st[idx] in signs:
			break

		if st[idx] == '(': br += 1
		elif st[idx] == ')': br -= 1
		idx += 1

	tree = binary_tree(st[idx])
	# Build each branch recursevely
	insert_left(tree, build_exp_tree(st[1:idx]))
	insert_right(tree, build_exp_tree(st[idx+1:-1]))

	return tree

'''
str_exp = '((((3+1)*3)/((9-5)+2))-((3*(7-4))+6))'
tree = build_exp_tree(str_exp)
print('String', str_exp)
print('Tree: ', tree)
print('Exp Result: ', postorder_evaluate(tree))
'''



# ------------------------------- Graph ----------------------------------

maze = [[ 'S', 'X', ' ', ' ', ' ', ' ', ' ', ' '],
 		[ ' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X'],
 		[ ' ', 'X', ' ', 'X', ' ', 'X', ' ', ' '],
 		[ ' ', 'x', ' ', 'X', ' ', 'X', 'X', 'X'],
 		[ ' ', ' ', 'X', 'X', ' ', ' ', ' ', 'X'],
 		[ 'X', ' ', ' ', ' ', ' ', 'X', ' ', ' '],
 		[ ' ', 'X', ' ', 'X', ' ', 'X', 'X', ' '],
 		[ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
 		[ ' ', ' ', ' ', 'X', 'X', 'X', 'X', 'X'],
 		[ ' ', ' ', ' ', ' ', 'X', 'X', 'X', 'X'],
 		[ ' ', 'X', 'X', 'X', 'X', ' ', 'X', 'X'],
 		[ ' ', ' ', ' ', ' ', 'X', ' ', 'X', 'X'],
 		[ ' ', 'X', ' ', ' ', 'X', ' ', ' ', ' '],
 		[ ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'G']]

def make_graph(init_node):
	return {init_node: []}

def add_vertex(G, vertex):
	if vertex not in G:
		G[vertex] = []

def add_edge(G, edge):
	(vertex1, vertex2) = tuple(edge)
	if vertex1 in G:
		G[vertex1].append(vertex2)
	else:
		G[vertex1] = [vertex2]

	if vertex2 in G:
		G[vertex2].append(vertex1)
	else:
		G[vertex2] = [vertex1]

def print_maze(m):
	''' Print maze in a readable form '''

	for i in range(len(m)):
		for j in range(len(m[0])):
			print(maze[i][j]),
		print
	print

def maze2graph(maze):
	''' Get matrix maze, return graph '''

	def cell_to_graph(c, maze):
		''' 
		Examine cell and its neighbours
		c (cell) - current cell
		i (index) - shift index
		'''

		# if current index + shift index is not out of range and \
		# neighbour is an empty cell and \
		# neighbour is not in the graph yet, then
		# add edge between current cell and neighbour and launch recursion for the neighbour
		for i in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
			if c[0]+i[0] in range(len(maze)) and c[1]+i[1] in range(len(maze[0])) and \
				maze[c[0]+i[0]][c[1]+i[1]] != 'X' and \
				(c[0]+i[0], c[1]+i[1]) not in G[c]:
					add_edge(G, ( c, (c[0]+i[0], c[1]+i[1])))
					cell_to_graph((c[0]+i[0], c[1]+i[1]), maze)



	G = make_graph((0, 0))
	cell_to_graph((0, 0), maze )
	return G

def solve_maze(maze):
	# Base case - meet the finish
	if maze[node[0]][node[1]] == 'G':
		return [node]

	# Mark current cell as visited
	maze[node[0]][node[1]] = 'V'

	# For each neighbour launch recursion ( if neighbour is not visited )
	for i in G[node]:
		if maze[i[0]][i[1]] != 'V':
			path = find_path(G, maze, i)
			if path:
				return [node] + path


graph = maze2graph(maze)
res_maze = find_path(graph, maze, (0, 0))
print_maze(maze)

