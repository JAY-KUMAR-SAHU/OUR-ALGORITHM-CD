import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import csv

#quality measures
def unifiability (G, Ci, Cj):
    sum1, sum2, sum3 = 0, 0, 0
    for i in Ci:
        for j in Cj:
            sum1 += 1 if G.has_edge(i, j) else 0
    for i in Ci:
        for j in G:
            sum2 += 1 if G.has_edge(i, j) else 0
        for j in Cj:
            sum2 -= 1 if G.has_edge(i, j) else 0
    for i in Cj:
        for j in G:
            sum3 += 1 if G.has_edge(i, j) else 0
        for j in Ci:
            sum3 -= 1 if G.has_edge(i, j) else 0
    return sum1 / (sum2 + sum3 - sum1)
#Average Uniformality
def AVU (G, cluster):
    #CALLING UNIFIABILITY FOR ALL CLUSTERS
    sum_unifiability = 0
    for i in cluster:
        for j in cluster:
            if i != j:
                sum_unifiability += unifiability (G, cluster[i], cluster[j])
    return sum_unifiability / len (cluster)

#Isolability
def isolability (G, Ci):
    sum1, sum2 = 0, 0
    for i in Ci:
        for j in Ci:
            sum1 += 1 if G.has_edge(i, j) else 0
    for i in Ci:
        for j in G:
            if i != j:
                sum2 += 1 if G.has_edge(i, j) else 0
    return sum1 / (sum1 + sum2)

#average isolabiltiy
def AVI (G, cluster):
    sum = 0
    for i in cluster:
        sum += isolability (G, cluster[i])
    return sum / len (cluster)

G = nx.Graph()
with open("dolphins.csv", mode ='r') as file:
   csvFile = csv.DictReader(file)
   for line in csvFile:
        G.add_edge(int(line['Source'])-1, int(line['Target'])-1)
# G.add_edges_from([[1,2], [2,3], [1,3], [1,4], [1,5], [3,5],
#                   [6,7], [7,8], [8,9], [6,9], [6,8], [7,9],
#                   [10,11], [11,12], [10,12],
#                   [9,12], [2,7]])
# G=nx.karate_club_graph()
plt.title('Original Graph', fontsize=40)
nx.draw(G, with_labels=True, node_color='r')
plt.show()
deg=G.degree()
# deg=sorted(G.degree(), key=lambda x: x[1], reverse=True)
print("deg = ", deg)
n=len(deg)
print(n)
# edge_betwenness = nx.edge_betweenness_centrality(G).items()
# sorted(edge_betwenness, key=lambda pair: -pair[1])[0][0]
NUM_ITERATIONS = (int)(n*0.15)
for i in range(0, NUM_ITERATIONS):
    edge_betweenness = nx.edge_betweenness_centrality(G).items()
    # print("\nStep ",i," : EB : ", edge_betweenness)
    print("\nStep ",i+1)
    deg=G.degree()
    # deg=sorted(G.degree(), key=lambda x: x[1], reverse=True)
    # print("deg = ", deg)
    
    # EB=nx.edge_betweenness(G);
    edge_to_delete = sorted(edge_betweenness, key=lambda pair: -pair[1])[0][0]
    u=edge_to_delete[0];
    v=edge_to_delete[1];
    # print("deg of ", u, " : ", deg[u], ", v : ", deg[v])
    if(deg[u]==1 or deg[v]==1):
        # print("No deletion")
        # plt.title('Step %s\nEdge %s NO DELETION'%(i, edge_to_delete), fontsize=20)  
        # nx.draw(G, with_labels=True, node_color='r')
        # plt.show()
        continue
    else :
        # print('Edge ', edge_to_delete,' Deleted')
        G.remove_edge(*edge_to_delete)
        # plt.title('Step %s\nEdge %s Deleted'%(i, edge_to_delete), fontsize=20)  
        # nx.draw(G, with_labels=True, node_color='r')
        # plt.show()

com=nx.connected_components(G)
count=1
for i in com :
    print(count, i)
    count+=1
plt.title('FINAL', fontsize=20)  
nx.draw(G, with_labels=True, node_color='r')
plt.show()
