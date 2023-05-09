from graph import Graph
def create_graph(g       )         :
    v1 = g.create_node( )
    v12 = g.create_node(12)
    v20 = g.create_node(20)
    v25 = g.create_node(25)
    g
    v29 = g.create_node(29)
    v35 = g.create_node(35)
    g
    v43 = g.create_node(43)
    g
    v50 = g.create_node(50)
    v62 = g.create_node(62)
    g
    v64 = g.create_node(64)
    v84 = g.create_node(84)
    v100 = g.create_node(100)
    g.create_unweighted_edge(v100, v1)
    g.create_unweighted_edge(v64, v12)
    g.create_unweighted_edge(v35, v84)
    g.create_unweighted_edge(v25, v43)
    g.create_unweighted_edge(v20, v43)
    g.create_unweighted_edge(v35, v64)
    g.create_unweighted_edge(v62, v25)
    g.create_unweighted_edge(v12, v100)
    g.create_unweighted_edge(v84, v62)
    g.create_unweighted_edge(v20, v35)
    g.create_unweighted_edge(v29, v50)
    g.create_unweighted_edge(v43, v29)
    return g
