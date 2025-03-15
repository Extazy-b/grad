from vector import Vector
from typing import Tuple, List

def interpol(points: List[Tuple[int]]) -> List[Tuple[int]]:
    n = len(points)
    X = tuple(point[0] for point in points)
    Y = tuple(point[1] for point in points)
    graph = []
    for t in range(points[0][0], points[n-1][0]+1):
        y = 0
        for i in range(n):
            q = Y[i]
            for j in range(n):
                if j != i:
                    q = q * (t-X[j]) / (X[i] - X[j])
            y = y + q
        graph.append((t, y))
    return graph
    

def main(points: List[Tuple[int]], colors: Tuple[Vector]) -> Tuple[int]:
    return ()