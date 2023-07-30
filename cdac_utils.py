def graph_viz(G):
    """Visualize NetworkX graph.
    """
    options = {
        "node_size": 900,
        "width": 5,
        "arrowstyle": "->",
        "arrowsize": 18,
        "font_size": 20,
        "font_weight": "bold",
        "font_color": "yellow",
    }
    pos = nx.kamada_kawai_layout(G)  # pos = nx.nx_agraph.graphviz_layout(G)
    nx.draw_networkx(G, pos, **options)
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.axis("off")
    plt.show()
