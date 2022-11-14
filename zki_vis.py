from treelib import Node, Tree
import json
import sys

f = open(sys.argv[1])
data = json.load(f)
f.close()

tree = Tree()

tree.create_node("Harry2", "harry2")


tree.create_node("Harry", "harry")  # No parent means its the root node
tree.create_node("Jane",  "jane"   , parent="harry")
tree.create_node("Bill",  "bill"   , parent="harry")
tree.create_node("Diane", "diane"  , parent="jane")
tree.create_node("Mary",  "mary"   , parent="diane")
tree.create_node("Mark",  "mark"   , parent="jane")

tree.show()

tree.to_graphviz()
