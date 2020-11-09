#__________graphs___________

def make_graph():
	return {}

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
        
        
maz=[['S','X',' ','X'],
	[' ',' ',' ',' '],
	[' ','X',' ','X'],
	[' ','X','G','X']]
        
def print_maze(maze):
	for i in range(len(maze)):
		for j in range(len(maze[0])):
			print(maze[i][j])
    
def maze2graph(maze):
	def cell_to_graph(cell):
		idxs = [(0, -1), (-1, 0), (1, 0), (0, 1)]
		for idx in idxs:
			if cell[0]+idx[0] in range(len(maze)) and cell[1]+idx[1] in range(len(maze[0])) and \
			maze[cell[0]+idx[0]][cell[1]+idx[1]] in [' ', 'G'] and \
			(cell[0]+idx[0], cell[1]+idx[1]) not in G[cell]:			
						add_edge(G, ( cell, (cell[0]+idx[0], cell[1]+idx[1])))
						cell_to_graph( (cell[0]+idx[0], cell[1]+idx[1]))


	G = make_graph()
	add_vertex(G, (0, 0) )
	cell_to_graph((0, 0))
	return G


print(maze2graph(maz))
	

def find_path(G, maze, node):
	if maze[node[0]][node[1]] == 'G':
		return [node]

	maze[node[0]][node[1]] = 'V'

	for i in G[node]:
		if maze[i[0]][i[1]] != 'V':
			path = find_path(G, maze, i)
			if path:
				return [node] + path

graph = maze2graph(maze)
res_maze = find_path(graph, maze, (0, 0))
print_maze(maze)