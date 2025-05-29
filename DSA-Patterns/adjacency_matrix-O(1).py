#adjacency matrix of an undrected graph
#TimeComplexity-O(1) for addingedge ,removing egde,checking edge
#Space usage: O(n²) → If you have 1000 nodes...that’s a million cells. RIP RAM.
class Graph:
    def __init__(self,num_of_nodes):
        self.adj_matrix=[[0] * num_of_nodes for i in range(num_of_nodes)]
    def adding_edge(self,u,v):
        self.adj_matrix[u][v]=1
        self.adj_matrix[v][u]=1
    def removing_edge(self,u,v):
        self.adj_matrix[u][v]=0
        self.adj_matrix[v][u]=0
    def has_egde(self,u,v):
        return self.adj_matrix[u][v]==1
    def print_matrix(self):
        for rows in self.adj_matrix:
            print(rows)
if __name__=="__main__":
    g=Graph(3)
    g.adding_edge(0,1)
    g.adding_edge(1,2)
    g.print_matrix()





