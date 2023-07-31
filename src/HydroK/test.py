from kg import KG

kg = KG()
kg.add_node('a')
kg.add_node('b')
kg.add_node('c')

kg.add_edge('a', 'b')
kg.add_edge('b', 'c')

print(kg)