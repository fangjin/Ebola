#!/usr/bin/python
# -*- coding: utf-8 -*-
import networkx as nx
import argparse
import matplotlib.pyplot as plt

def	get_graph(graph_file):
	G=nx.Graph()
	with open(graph_file, "r") as rg:
		for line in rg:
			tmp = line.strip().split(" ",2)
			if len(tmp) > 1:
				#nodelist.append(str(tmp[0]))
				#nodelist.append(str(tmp[1]))
				G.add_nodes_from([str(tmp[0]), str(tmp[1])])
				G.add_edge(str(tmp[0]), str(tmp[1]), weight=tmp[2])
	#nx.draw(G,node_color = 'blue')
	#plt.show()
	return G


def	main(graph, outfile):
	result = get_graph(graph)
	nx.write_gexf(result, outfile)
	#cliques = [clique for clique in nx.find_cliques(result) if len(clique)>2]
	#print cliques



main("./DQE/20141006_filter_rumor_sample/edges.txt", "./DQE/20141006_filter_rumor_sample/20141006_new_sample_weithgt.gexf")


# zombies
