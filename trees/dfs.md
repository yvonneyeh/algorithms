# Depth-First Search and Depth-First Traversal

Depth-first search (DFS) is a method for exploring a tree or graph. In a DFS, you go as deep as possible down one path before backing up and trying a different one.

Depth-first search is like walking through a corn maze. You explore one path, hit a dead end, and go back and try a different one.

Here's a how a DFS would traverse this tree, starting with the root:

Our depth-first search has us start at the root node at the top of the tree. We'd go down the first path we find until we hit a dead end then head down the next leftmost path until we reach a dead end.

## Advantages:

- Depth-first search on a binary tree generally requires less memory than breadth-first.
- Depth-first search can be easily implemented with recursion.

## Disadvantages

- A DFS doesn't necessarily find the shortest path to a node, while breadth-first search does.
