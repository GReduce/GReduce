from graph import Graph
def create_graph(g       )         :
    v1 = g.create_node(1)
    v2 = g.create_node(2)
    v3 = g.create_node(3)
    v4 = g.create_node(4)
    v5 = g.create_node(5)
    v6 = g.create_node(6)
    v7 = g.create_node(7)
    v8 = g.create_node(8)
    v9 = g.create_node(9)
    v10 = g.create_node(10)
    v11 = g.create_node(11)
    v12 = g.create_node(12)
    v13 = g.create_node(13)
    v14 = g.create_node(14)
    v15 = g.create_node(15)
    v16 = g.create_node(16)
    v17 = g.create_node(17)
    v18 = g.create_node(18)
    v19 = g.create_node(19)
    v20 = g.create_node(20)
    g.create_weighted_edge(v1, v13, 0)
    g.create_weighted_edge(v16, v8, 3)
    g.create_weighted_edge(v18, v16, 1)
    g.create_weighted_edge(v8, v7, 4)
    g.create_weighted_edge(v2, v18, 9)
    g.create_weighted_edge(v17, v20, 3)
    g.create_weighted_edge(v13, v9, 1)
    g.create_weighted_edge(v3, v1, 6)
    g.create_weighted_edge(v20, v11, 7)
    g.create_weighted_edge(v19, v2, 9)
    g.create_weighted_edge(v12, v3, 0)
    g.create_weighted_edge(v6, v12, 2)
    g
    g.create_weighted_edge(v11, v15, 1)
    g.create_weighted_edge(v7, v5, 3)
    g.create_weighted_edge(v14, v19, 8)
    g.create_weighted_edge(v15, v14, 1)
    g.create_weighted_edge(v9, v10, 0)
    g.create_weighted_edge(v5, v4, 1)
    g.create_weighted_edge(v4, v6, 3)
    g.create_weighted_edge(v6, v11, 8)
    g.create_weighted_edge(v10, v17, 0)
    return g