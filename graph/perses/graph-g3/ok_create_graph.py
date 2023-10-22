from graph import Graph
def create_graph(g       )         :
    v1 = g.create_node(1)
    v12 = g.create_node(12)
    v13 = g.create_node(13)
    v26 = g.create_node(26)
    g
    g
    v48 = g.create_node(48)
    g
    v50 = g.create_node(50)
    v56 = g.create_node(56)
    g
    v69 = g.create_node(69)
    g
    g
    v99 = g.create_node(99)
    g.create_unweighted_edge(v12, v13)
    g.create_unweighted_edge(v12, v26)
    g.create_unweighted_edge(v69, v99)
    g
    g.create_unweighted_edge(v13, v48)
    g.create_unweighted_edge(v1, v56)
    g.create_unweighted_edge(v26, v69)
    g.create_unweighted_edge(v56, v99)
    g.create_unweighted_edge(v48, v50)
    return g
