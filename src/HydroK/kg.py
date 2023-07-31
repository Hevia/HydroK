from node import Node
from typing import Dict, List, Tuple

class KG:
    def __init__(self) -> None:
        self.edges: Dict[str, List[str]] = {}
        self.nodes: Dict[str, Node] = {}

    def __str__(self):
        return f'Nodes: {self.nodes} Edges: {self.edges}'

    def __repr__(self):
        return f'KG(Nodes:\'{self.edges}\', Edges:{self.edges})'

    def from_csv(self, path: str) -> None:
        pass

    def from_text(self, text: str) -> None:
        pass

    def to_csv(self, path: str) -> None:
        pass

    def to_text(self) -> str:
        pass

    # TODO: Node | str
    def add_node(self, node) -> None:
        # Check to see if it exists already, if so raise an exception
        if isinstance(node, str):
            insert_node = Node(node)
        else:
            insert_node = node

        if insert_node.name in self.nodes:
            raise Exception(f"Node {insert_node.name} already exists in the graph")
        else:
            self.nodes[insert_node.name] = insert_node

    def add_edge(self, head, tail) -> None:
        # Check to see if the head and tail nodes exist, if not raise an exception
        if isinstance(head, Node):
            head_ref = head.name
        elif isinstance(head, str):
            head_ref = head
        else:
            raise Exception(f"Invalid type for head: {type(head)}")
        
        if isinstance(tail, Node):
            tail_ref = tail.name
        elif isinstance(tail, str):
            tail_ref = tail
        else:
            raise Exception(f"Invalid type for tail: {type(tail)}")

        if head_ref not in self.nodes:
            raise Exception(f"Node {head_ref} does not exist in the graph")
        if tail_ref not in self.nodes:
            raise Exception(f"Node {tail_ref} does not exist in the graph")

        if head_ref not in self.edges:
            self.edges[head_ref] = []
        self.edges[head_ref].append(tail_ref)

        # We're just assuming any edge is bidirectional for now
        # if tail_ref not in self.edges:
        #     self.edges[tail_ref] = []
        # self.edges[tail_ref].append(head_ref)

    def get_nodes(self) -> List[Node]:
        return list(self.nodes.values())

    def get_edges(self) -> List[Tuple[Node, Node]]:
        edges: List[Tuple[Node, Node]] = []
        for head in self.edges:
            for tail in self.edges[head]:
                edges.append((self.nodes[head], self.nodes[tail]))
        return edges
    
    def get_node(self, name) -> Node:
        if isinstance(name, Node):
            name_ref = name.name

        if name_ref not in self.nodes:
            raise Exception(f"Node {name_ref} does not exist in the graph")
        return self.nodes[name_ref]

    def get_edge(self, head, tail) -> Tuple[Node, Node]:
        if isinstance(head, Node):
            head_ref = head.name
        if isinstance(tail, Node):
            tail_ref = tail.name

        if head_ref not in self.nodes:
            raise Exception(f"Node {head_ref} does not exist in the graph")
        if tail_ref not in self.nodes:
            raise Exception(f"Node {tail_ref} does not exist in the graph")
        
        if head_ref not in self.edges:
            raise Exception(f"Node {head_ref} has no edges")
        if tail_ref not in self.edges[head_ref]:
            raise Exception(f"Node {head_ref} does not have an edge to {tail_ref}")
        
        return (self.nodes[head_ref], self.nodes[tail_ref])