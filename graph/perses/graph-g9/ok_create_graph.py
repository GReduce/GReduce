from graph import Graph
def create_graph(g       )         :
    v1 = g.create_node(1)
    v2 = g.create_node(2)
    v9 = g.create_node(9)
    v11 = g.create_node(11)
    v12 = g.create_node(12)
    g
    v26 = g.create_node(26)
    g
    v29 = g.create_node(29)
    v30 = g.create_node(30)
    v33 = g.create_node(33)
    v46 = g.create_node(46)
    g
    v50 = g.create_node(50)
    g
    v64 = g.create_node(64)
    v65 = g.create_node(65)
    v68 = g.create_node(68)
    g
    v74 = g.create_node(74)
    g
    v76 = g.create_node(76)
    g
    v88 = g.create_node(88)
    v98 = g.create_node(98)
    v100 = g.create_node(100)
    g.create_unweighted_edge(v100, v1)
    g.create_unweighted_edge(v9, v76)
    g.create_unweighted_edge(v65, v64)
    g.create_unweighted_edge(v50, v74)
    g.create_unweighted_edge(v46, v65)
    g.create_unweighted_edge(v33, v98)
    g.create_unweighted_edge(v11, v88)
    g.create_unweighted_edge(v98, v11)
    g.create_unweighted_edge(v64, v12)
    g.create_unweighted_edge(v26, v68)
    g.create_unweighted_edge(v88, v46)
    g.create_unweighted_edge(v76, v30)
    g.create_unweighted_edge(v30, v33)
    g.create_unweighted_edge(v12, v100)
    g.create_unweighted_edge(v74, v65)
    g.create_unweighted_edge(v2, v26)
    g.create_unweighted_edge(v68, v9)
    g.create_unweighted_edge(v29, v50)
    g.create_unweighted_edge(v2, v29)
    return g
