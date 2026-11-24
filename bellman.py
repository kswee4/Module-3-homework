'''
Hand-crafted code, written by myself, that does Bellman calculations for a given graph
'''


from dataclasses import dataclass
from operator import attrgetter

@dataclass
class Path:
    destination: str
    time_cost: int
    battery_cost: int

class Node:
    paths = []
    name=''

    def __init__(self, _name, _connections:list):
       self.name = _name
       self.paths = _connections

    def has_path(self, _name) -> bool:
        return any(connection.destination == _name for connection in self.paths)

    def get_path(self, _name) -> Path:
        target = next((path for path in self.paths if path.destination == _name), None)
        return target

all_nodes = {
   'A': Node('A', [Path('C',2,2), Path('D',4,1)]),
   'B': Node('B', []),
   'C': Node('C', [Path('E',2,1), Path('F',5,1)]),
   'D': Node('D', [Path('E',3,1), Path('F',2,2)]),
   'E': Node('E', [Path('B',2,3), Path('E',3,-4)]),
   'F': Node('F', [Path('B',4,1)]),
}

@dataclass
class BellNode:
    # these two are used as a key
    node_name = ''
    battery = 0

    # not used as a key
    precedent=''
    time_from_dest=0

    def __init__(self, _name, _battery):
        self.node_name = _name
        self.battery = _battery

all_bellnodes = []

def has_bell_node(_name, _battery):
    node = next((x for x in all_bellnodes if x.node_name == _name and x.battery == _battery), None)
    return node is not None

def get_bell_node(_name, _battery):
    node = next((x for x in all_bellnodes if x.node_name == _name and x.battery == _battery), None)
    if node == None:
        node = BellNode(_name, _battery)
        all_bellnodes.append(node)
    return node

def set_bell_node(_name, _battery, _bell_node):
    for i in range(len(all_bellnodes)):
        if all_bellnodes[i].node_name == _name and all_bellnodes[i].battery == _battery:
            all_bellnodes[i] = _bell_node
            return
    all_bellnodes.append(_bell_node)

# Specifically this function was written by ChatGPT
def print_bell_table(nodes: list[BellNode]) -> None:
    """Print time_from_dest for each node name and battery level."""
    names = sorted({node.node_name for node in nodes})
    batteries = sorted({node.battery for node in nodes})
    times = {(node.node_name, node.battery): node.time_from_dest for node in nodes}

    rows = [["node_name", *(str(battery) for battery in batteries)]]
    for name in names:
        values = [str(times.get((name, battery), "+∞")) for battery in batteries]
        rows.append([name, *values])

    widths = [max(map(len, column)) for column in zip(*rows)]
    for index, row in enumerate(rows):
        cells = [row[0].ljust(widths[0])]
        cells.extend(value.rjust(width) for value, width in zip(row[1:], widths[1:]))
        print(" | ".join(cells))
        if index == 0:
            print("-+-".join("-" * width for width in widths))

def bellman():
    # start at terminal node
    all_bellnodes.clear()
    stack = []
    stack.append(BellNode('B', 4))
    stack.append(BellNode('B', 3))
    stack.append(BellNode('B', 2))
    stack.append(BellNode('B', 1))
    stack.append(BellNode('B', 0))

    # while stack not empty
    while len(stack) > 0:
        # pop top
        curr = stack[-1]
        stack.pop()
        curr_bell = get_bell_node(curr.node_name, curr.battery)

        # go thru battery states
        for battery in range(4):
            # go thru reverse-neighbors
                for neighbor in all_nodes.values():
                    path_from_neighbor = neighbor.get_path(curr.node_name)
                    if path_from_neighbor is None:
                        continue

                    # minimum battery from neighbor isn't possible? skip this node/battery combo
                    battery_from_neighbor = max(battery + path_from_neighbor.battery_cost, 0)
                    if battery_from_neighbor > 4:
                        continue

                    # new node?
                    if not has_bell_node(neighbor.name, battery_from_neighbor):
                        new_node                = get_bell_node(neighbor.name, battery_from_neighbor)
                        new_node.precedent      = curr_bell.node_name
                        new_node.time_from_dest = curr_bell.time_from_dest + path_from_neighbor.time_cost
                        set_bell_node(neighbor.name, battery_from_neighbor, new_node)
                        stack.append(new_node)
                    else:
                        # faster than existing?
                        existing        = get_bell_node(neighbor.name, battery_from_neighbor)
                        new_time_cost   = curr_bell.time_from_dest + path_from_neighbor.time_cost
                        if new_time_cost < existing.time_from_dest or (new_time_cost == existing.time_from_dest and battery_from_neighbor < existing.battery):
                            existing.precedent      = curr_bell.node_name
                            existing.time_from_dest = curr_bell.time_from_dest + path_from_neighbor.time_cost
                            existing.battery        = battery_from_neighbor
                            set_bell_node(neighbor.name, existing.battery, existing)
                            stack.append(existing)


    # print out bellman stats
    print_bell_table(all_bellnodes)

if __name__ == "__main__":
    bellman()


