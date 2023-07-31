
class Node:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self):
        return f'Node: {self.name}'

    def __repr__(self):
        return f'Node(name: {self.name})'