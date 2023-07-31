# HydroGraph

HydroGraph is a simple graph library for Python. Designed to be easily extensible and usable for quick prototyping or production environments.

HydroGraph has no graph algorithms built in. It merely provides an interface for storing nodes & edges. The goal is to give projects a simple graph interface with no dependencies and you only build out what your project needs.

Example Usage:

```python
from hydrok.kg import KG

kg = KG()
kg.add_node('a')
kg.add_node('b')
kg.add_node('c')

kg.add_edge('a', 'b')
kg.add_edge('b', 'c')

print(kg)
```

More examples can be found in the [Examples/]() folder such as:
- [Using SQLite as a backend]()
- [Deploying HydroGraph to WASM]()
- [Creating a knowledge graph from text using Transformers]()
- [Converting a HydroGraph to a Networkx graph]()
- [Extending HydroGraph with custom node/edge types]()
- [Link prediction with HydroGraph]()

# References & Inspiration

- [Zincbase](https://github.com/complexdb/zincbase) As the initial inspiration for a small knowledge base written with a simple API.
- [GraphDB](https://github.com/CodyKochmann/graphdb) A SQLite backed graph database written in Python.