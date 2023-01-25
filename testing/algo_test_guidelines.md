# Algorithm Testing Guidelines


Ensuring your algorithm works correctly through adequate testing is necessary for software development. Although you cannot prove an algorithm is bug-free with testing, you become very confident in its robustness with thorough testing. However, you can't invest time testing every possible input permutation that your algorithm must handle. Therefore, there are always trade-offs you must balance and always time and effort you must prioritize to maximize your productivity. An efficient test suite maximizes coverage while limiting duplicate tests covering the same domain. For example, in an algorithm that's summing an integer array, a test case summing [1,2,3,4] overlaps entirely with a test case summing [6,7,8,9], so only one of these test cases is beneficial.

These are some broad guidelines for testing different data types and data structures. These are generic test scenarios that may only sometimes apply to a problem, and they don't cover edge cases specific to an algorithm. So, for example, there will be a test plan for string inputs but not test cases dedicated to an algorithm that checks if a string is a palindrome.


## String

* Null & Empty
* 1-char
* Odd / Even length
* Alphabetical
* Alphanumeric
* Capitalization / Case sensitivity
* Unsorted
* Sorted ascending / descending
* Special characters !@#$%^&*()""
* All / Some / No duplicates

---

## Integer

* Negative / Positive
* Zero
* Odd / Even

---

## Float / Double

* Negative / Positive
* Zero
* Odd / Even
* Decimals
* Precision level (how many zeros after the decimal)

---

## Array

* Null & Empty
* 1-element
* Odd / Even length
* At the first / last index
* Not in the data structure
* All / Some / No duplicates
* Unsorted
* Sorted ascending / descending

---

## Matrix

Same as Array

* 1 row / column
* Square
* Rectangle
* Uneven array lengths
* Not in the data structure

---

## Binary Tree

* Null
* 1-node
* 1-child
* 2-children
* Binary Search Tree
* Complete tree
* Deep tree
* Symmetric / Asymmetric tree
* Single-chained tree
* Duplicates
* At the root/leaf
* In the middle
* Not in the data structure

---

## N-ary Tree

Same as Binary Tree

* Less / More than N children
* Exactly N children
* Wide tree

---

## Linked List

* Null
* 1-node
* At the head / tail node
* All / Some / No duplicates
* Unsorted
* Sorted ascending / descending
* Not in the data structure

---

## Graph

* Null
* 1-node
* Directed
* Undirected
* Cycles
* Complete graph
* Sinks
* Sources
* Not in the data structure

---

## Get Kth value (Top K / First K)

* Less / More than K
* Exactly K

---

## Recursion

* Base case
* Recursive case
