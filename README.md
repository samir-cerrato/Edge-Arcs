# Edge-Arcs
Read in a sequence of digraphs and output the number of (uni-directed connections) arcs and (bi-directed connections) edges between pairs of vertices.

Each digraph will be specified by an integer n ≤100000 indicating the number of vertices, followed by
the adjacency lists (one list per line) for these vertices implicitly labeled 0, . . . , n −1. Each line will
be a sequence of integers between 0 and n −1 separated by spaces, with possible leading and trailing
spaces.

A digraph of order 0, which is not processed, will terminate the input sequence. (Note: each input
digraph will have at most 10 million arcs.)

Sample Input:

5

1 2

0 

0 1

4

3

 4
 
 1 3 2
 
 0

0

Output will be of the format:

Digraph x: y z

where x denotes the sequence number of the input starting at 1, and y is the number of arcs (that
aren’t edges) and z is the number of edges.

Sample Output:

Digraph 1: 1 3

Digraph 2: 2 1
