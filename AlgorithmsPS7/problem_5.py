# test_graph = {'A': set(['B', 'C']),
# 		 'B': set(['A', 'D', 'E']),
# 		 'C': set(['A', 'F']),
# 		 'D': set(['B']),
# 		 'E': set(['B', 'F']),
# 		 'F': set(['C', 'E'])}

test_graph = {'1': set(['2', '3','6']),
		'2': set(['4', '1']),
		'3': set(['1', '5']),
		'5': set(['3','6','7']),
		'6': set(['4', '1','5']),
		'4': set(['2', '6']),
			'7': set(['5'])}


vertices = []
path_list = []


for key in test_graph:
	vertices.append(key)
#this builds a list of vertices.only done once. 	

#this is pretty much a normal bfs that returns shortest and longest path 

def bfs_paths(adj_list, begin, end):
	queue = [(begin, [begin])]
	#this is our original queue, with our begin node, and out list 
	while len(queue) != 0: 
   	#while the queue still exists
		(vertex, path) = queue.pop(0)
		#vertex and path are set and the first vertex is popped off of the queue
		for next in adj_list[vertex] - set(path):
		   	#this finds the next vertex that we are now at in the adj_list, subtracts the set path from it 
			if (next == end):
				yield path + [next]
			#if we reached our final goal, yield the path 
			else: 
				queue.append((next, path + [next]))

def diam():
	diameter = 0
	for x in vertices:
	#iterates through one set of the vertices 
		for y in vertices:
		#iterates throught the set of vertices 
			if (y != x):
			#if we aren't calculating path to ourselves 			
				temp = list(bfs_paths(test_graph,x,y))[0]
				#calculate shorest path bewteen the two nodes. 
				#path_list.append(temp)
				#this builds our path list for debugging purpoeses. Not necessary for final run 
				if (len(temp) -1  > diameter):
					diameter = len(temp) -1 
					#checks the length of the bfs optimal path between two nodes, if the amount of edges are bigger than our largest diameter, we change our dimaeter to the new biggest edge length
	return diameter 

print diam()

