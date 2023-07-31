from node import Node


class KG:
    def __init__(self) -> None:
        edges = {}
        nodes = {}

    def from_csv(self, path: str) -> None:
        pass

    def from_text(self, text: str) -> None:
        pass

    def to_csv(self, path: str) -> None:
        pass

    def to_text(self) -> str:
        pass

    def add_node(self, node: Node | str) -> None:
        # Check to see if it exists already, if so raise an exception
        if isinstance(node, str):
            node = Node(node)
            if node.name in self.nodes:
                raise Exception(f"Node {node.name} already exists in the graph")
            else:
                self.nodes[node.name] = node

    def add_edge(self, head: Node | str, tail: Node | str) -> None:
        # Check to see if the head and tail nodes exist, if not raise an exception
        if isinstance(head, str):
            head = Node(head)
        if isinstance(tail, str):
            tail = Node(tail)

        if head.name not in self.nodes:
            raise Exception(f"Node {head.name} does not exist in the graph")
        if tail.name not in self.nodes:
            raise Exception(f"Node {tail.name} does not exist in the graph")

        # Check to see if the edge already exists, if so raise an exception
        if (head, tail) in self.edges:
            raise Exception(f"Edge {head.name} -> {tail.name} already exists in the graph")
        else:
            self.edges[head.name] = tail

    def get_nodes(self) -> list[Node]:
        pass

    def get_edges(self) -> list[tuple[Node, Node]]:
        pass

    def get_node(self, name: str) -> Node:
        pass

    def get_edge(self, head: Node | str, tail: Node | str) -> tuple[Node, Node]:
        pass