from matplotlib import pyplot as plt
from pylab import *
import math
import networkx as nx                  # import networkx
import numpy as np
import time
import random
import heapq


def dj_shortest_path(G, start, end):
   def flatten(L):       # this flattens our linked list 
      while len(L) > 0: #while our length of linked list is greater than 0: 
         yield L[0]
         L = L[1] #append the rest of our list.

   q = [(0, start, ())]  # This makes a heap witht: cost, path_head, rest of path .
   visited = set()       # Visited vertices.
   while True:
      (cost, v1, path) = heapq.heappop(q) #pop the path off of the top of the heap 
      if v1 not in visited:
         visited.add(v1)
         if v1 == end: #if we are at the end 
            return list(flatten(path))[::-1] + [v1] #return a list flattened with the destination 
         path = (v1, path)
         for (v2, cost2) in G[v1].iteritems():
            if v2 not in visited:
               heapq.heappush(q, (cost + cost2, v2, path))

test_g = {'s':{'u':30, 'x':5},
     'u':{'v':1, 'x':15},
     'v':{'y':4},
     'x':{'u':3, 'v':1, 'y':2},
     'y':{'s':7, 'v':6}}

print "HI  ",dj_shortest_path(test_g,'s','y')




def calc_prob(n):
	return (5.0/(n-1))

def dj_graph(tests,nodes):

	axis([0, math.log10(nodes), 0, .02])
	xlabel('Amount of Nodes (log_10 logarithmic scale)')
	ylabel('Runtime in Seconds')

	t = arange(0.0, math.log10(nodes), 0.01)
	s = 2*nodes*(math.log(nodes,2))
	print s
	
	total = 0 
	for i in range (3,nodes):

		for t in range (1,tests):
			G = nx.erdos_renyi_graph(i,calc_prob(i),directed = True)
			#this creates the graph 

			cleaner = nx.adjacency_matrix(G)

			counter = 0 
			bad = 100000

			for y in cleaner:

				row_sum = np.sum(y)

				if row_sum == 0: 
					G.remove_node(counter)
					#print "Removed node:", counter
					bad = counter
					#if the row sum is 0, then remove it from graph 

				counter += 1

			time_start = time.time()

			start = random.randint(0,i-1)
			#print "Start is:", start
			dest = random.randint(0,i - 1)
			#print "Dest is:", dest

			while start == bad: 
				start = random.randint(0,i-1)

			while dest == bad: 
				dest = random.randint(0,i - 1)


			try: nx.dijkstra_path(G, start ,dest)	
			
			except: 
				print "BAD TESt"
				pass


			total += (time.time() - time_start)



			#print "Run time is",total

		node_set = total/tests
		


		
		plot(math.log10(i),[node_set],'ro')
		plot(math.log10(i),[node_set])

		print "Average time for ", i, " is ", node_set

	show()


dj_graph(20,200)