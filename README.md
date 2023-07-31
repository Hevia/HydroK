# HydroK

HydroK (pronounced Hydro-K or however you want!) is a simple knowledge graph library for Python. Designed to be embedded in other applications with a choice of local file or SQLite storage.

Example Usage:

```python
from hydrok.kg import KG

kg = KG()
kg.add_node('a')
kg.add_node('b')
kg.add_node('c')

kg.add_edge('a', 'b')
kg.add_edge('b', 'c')

kg.find_path('a', 'c')
>>> ['a', 'b', 'c']
```

Using with Transformers + REBEL (relation extraction model):

```python
from hydrok.kg import KG

kg = KG()
```

More examples can be found in the [Examples/]() folder.


# References & Inspiration

- [Zincbase](https://github.com/complexdb/zincbase) 