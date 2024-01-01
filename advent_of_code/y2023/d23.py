from dataclasses import dataclass
from string import ascii_uppercase

from tinsel import BaseSolution, Grid


class Node:
    id_index = 0

    @classmethod
    def get_id(cls):
        s = ""

        d, r = divmod(cls.id_index, 26)
        s += ascii_uppercase[r]

        while d:
            d, r = divmod(d - 1, 26)
            s += ascii_uppercase[r]

        cls.id_index += 1

        return s[::-1]

    def __init__(self):
        self._edges: list["Edge"] = []
        self.directed_edges: list["Edge"] = []

        self.id = self.get_id()

    def add_connection(self, length: int, node: "Node" = None, directed=False):
        if node is None:
            node = Node()

        edge = Edge(length, node)

        self._edges.append(edge)

        if directed:
            self.directed_edges.append(edge)

        return edge

    def edges(self, directed=True):
        if directed:
            return iter(self.directed_edges)
        return iter(self._edges)

    def __hash__(self) -> int:
        return hash(self.id)

    def __repr__(self) -> str:
        return f"Node({self.id}, {self._edges})"


@dataclass
class Edge:
    length: int
    node: Node

    def __repr__(self):
        return f"Edge(l={self.length}, {self.node.id})"


class Solution(BaseSolution):
    SLOPES: dict[str, tuple[int, int]] = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}
    DELTAS = {v: k for k, v in SLOPES.items()}

    graph: dict[tuple[int, int], Node]

    def valid_steps(self, grid: Grid, x: int, y: int, seen: set):
        ways = []
        for nx, ny in grid.neighbor_coords(x, y, corners=False):
            if (nx, ny) in seen or (c := grid.get(nx, ny)) == "#":
                continue

            if c in self.SLOPES:
                dx, dy = nx - x, ny - y

                if (dx, dy) != self.SLOPES[c]:
                    continue

            ways.append((nx, ny))

        return ways

    def generate_graph(
        self,
        grid: Grid,
        cx: int,
        cy: int,
        seen: set = None,
        graph: dict[tuple, Node] = None,
        current_node: Node = None,
    ):
        slopes_seen = 0

        if seen is None:
            slopes_seen += 1
            seen = {(cx, cy)}

        if graph is None:
            graph = {(cx, cy): Node()}
            current_node = graph[cx, cy]

        x, y = cx, cy

        edge_length = 0

        while len(ways := self.valid_steps(grid, x, y, seen)) == 1 and slopes_seen < 2:
            slopes_seen += grid.get(x, y) != "."
            x, y = ways[0]
            seen.add((x, y))
            edge_length += 1

        if len(ways) == 0:
            new_node = current_node.add_connection(edge_length, directed=True).node
            graph[x, y] = new_node
            return

        edge_length += 1

        if (x, y) in graph:
            current_node.add_connection(edge_length, graph[x, y], True)
            graph[x, y].add_connection(edge_length, current_node)
            return

        new_node = current_node.add_connection(edge_length, directed=True).node
        new_node.add_connection(edge_length, current_node)

        graph[x, y] = new_node

        for nx, ny in ways:
            self.generate_graph(grid, nx, ny, seen | set(), graph, new_node)

        return graph

    def maximize_graph(self, node: Node, seen: set = None, directed=True):
        if seen is None:
            seen = {node}

        max_len = 0

        for edge in node.edges(directed):
            if edge.node in seen:
                continue

            max_len = max(max_len, self.maximize_graph(edge.node, seen | {edge.node}, directed) + edge.length)

        return max_len

    def part1(self, puzzle_input: str):
        grid = Grid(puzzle_input)
        self.graph = self.generate_graph(grid, 1, 0)
        return self.maximize_graph(self.graph[1, 0])

    def part2(self, puzzle_input: str):
        return self.maximize_graph(self.graph[1, 0], directed=False)
