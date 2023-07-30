def graph_viz(G):
    """Visualize NetworkX graph.

    Parameters
    ----------
    G : networkx.Graph
        The NetworkX graph to be visualized.

    nx.draw_kamada_kawai(
        G,
        with_labels=True,
        node_size=700,
        width=3,
        font_size=14,
        font_weight="bold",
        font_color="whitesmoke",
    )
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
