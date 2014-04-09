from matplotlib import pyplot as plt
import networkx as NX                  # import networkx
import numpy as NP


def calc_prob(n):
	return (5.0/(n-1))

def diam_calc(G,x):
	diameter = 0 
	for i in range(x):
		stats = NX.single_source_shortest_path_length(G,i)
		#print i 
		#print stats
		if diameter < max(stats.values()):
			diameter =  max(stats.values())
	return diameter

def create_first_graph(tests,nodes):

	plt.axis([0, (nodes + 10), 0, 20])
	plt.xlabel('Amount of Nodes')
	plt.ylabel('Diameter')

	for i in range(3,nodes): 
	#this is the number of nodes, between 5 and 30 
		avg_node = 0
		avg_node_diam = 0
		for y in range(0,tests):
		#this runs 100 tests for each node	
			G = NX.erdos_renyi_graph(i,calc_prob(i))
			diameter = diam_calc(G,i)
			avg_node += diameter
			#this builds a erdos graph with amount i nodes and the probability of that node 
			#print ("Diam is: ",diameter, "for graph iwth nodes", i)
			#this prints the diameter of the graph
		avg_node_diam = avg_node/tests
		print("Avg diam for node:", i, " is ", avg_node_diam)
		plt.plot([i],[avg_node_diam],'ro')

	plt.show()



create_first_graph(30,76) 
