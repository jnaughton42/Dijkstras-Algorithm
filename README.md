# Dijkstras Algorithm Program for Data Structures and Algorithms (Spring 2024)

Simple Dijkstra's Algorithm implementation with Min-Heap priority queue for Data Structures &amp; Algorithms.

Outputs all optimal paths from start node to other nodes

## Input File Format

1. First Line: nodeName1,nodeName2,nodeName3,nodeName4
2. Second Line: startNode,endNode
3. Subsequent Lines: weight(node1->node1),weight(node1->node2),weight(node1->node3),weight(node1->node4)

### Example:

```
A,B,C,D,E
A,E
0,1,-,-,4
1,0,1,-,2
-,1,0,1,-
-,-,1,0,1
2,2,-,1,0
```

## Potential Improvements

- Code is confusing and poorly commented, need organization into more functions and more/more detailed comments
- Fix sloppy solutions (like starting a counter at -2)
- Actually search specifically for end node
- Add unit tests
