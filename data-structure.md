# UCSanDiegoX: CSE100x Data Structure
**UCSanDiegoX: [CSE100x - Data Structures: An Active Learning Approach](https://stepik.org/course/579/)**

### Definition
Data Structure - a particular structured way of storing data in a computer so that it can be used efficiently

### Contents

- [Big O](#Big-O)
- [Classes of Computation Complexity](#Classes-of-Computation-Complexity)
- [Bit-by-Bit](#Bit-by-Bit)
- [Array lists, Linked lists, Skip lists, and Circular arrays](#Array-lists)
- [Deque, Queue, and Stacks](#Abstract-Data-Types)
- [Graphs](#Graphs)


## Big O
Efficiency of Algorithm.

**Time Complexity** - the time complexity of a given algorithm tells us roughly how fast the algorithm performs as the input size grows

- Big-O ("Big-Oh") - upper bound
- Big-Ω ("Big-Omega") - lower bound
- Big-ϴ ("Big-Theta") - upper bound and lower bound
  ```
  Example: Print 5 header lines and  then prints the n students' names and grades on separate lines.

  Number of operations = 2n + 5
  Big-O notation would be O(2n + 5)

  we would simplify to O(n) because we drop the constant (2n becomes n) and drop all lower terms (5 < n as n becomes large)
  we always want to describe them using the tightest possible upper-bound
    ```

**Space Complexity**


Side notes:
Fibonacci Sequence: xn = xn-1 + xn-2
Naive Algorithm (recursive with 1.77 x 10^21 lines of code for N=100) vs Efficient Algorithm (array list with 202 lines of code for N=100)


## Classes of Computation Complexity
(need to come back to this later)
- Polynomial time (P class) - class of computational problems that can be solved in polynomial time
- Nondeterministic Polynomial time (NP class) - class of computational problems that can be verified in polynomial time (whether or not you can solve them in polynomial time)
- Nondeterministic Polynomial-time hard (NP-Hard class) - if it is at least as hard as the hardest problems in NP. Not a subset of NP.
- NP-Complete - intersection between NP and NP-Hard


## Bit-by-Bit

- bit - basic unit of information. Can have only one of two values
- byte - a unit of digital information and it is just a sequence of some number of bits. For simplicity,  we can assume that a byte is a sequence of 8 bits.

1 byte is the smallest unit of storing memory in modern computers. Every file on a computer is just a sequence of 8-bit chunks. Text, images, videos, audio, literally all filetypes.
  ```
  EXERCISE: How many distinct symbols could be represented with 4 bytes? (Write the answer as an integer, not in scientific notation)

  2^(8*4)
  ```

"decimals" meant "base 10"
The number 729 can be thought of as (10² × 7) + (10¹ × 2) + (10⁰ × 9)

"binary numbers" meant "base 2"
The number 101 can be thought of as  (2² × 1) + (2¹ × 0) + (2⁰ × 1).
In other words, 101 in binary is equal to 4 + 0 + 1 = 5 in decimal
  ```
  EXERCISE: Convert the binary number 101010 to decimal.

    (2^5 × 1) + (2^4 × 0) + (2^3 × 1) + (2² × 0) + (2¹ × 1) + (2⁰ × 0)
    = 32 + 0 + 8 + 0 + 2 + 0 = 42
  ```
  ```
  EXERCISE: Add the binary numbers 0101 and 0101
    1010
  ```
  ```
  EXERCISE: What is the result of the following bitwise expression? Assume the numbers are unsigned 8-bit numbers. Enter your answer as a decimal number (not binary).
  7 | (~125 << 3)

    Find a
    0...0111 <- 7
    Find b
    1111101 <- 125
    0000010 <- ~125
    0010000 <- << 3

    0010111 <- a | b
    2^4 + 2^2 + 2^1 + 2^0 = 23
  ```



## Array Lists
constant-time access (read and write)
  - homogeneous data structure
  - adjacent memory location
  - random **access** O(1) time (best case) (why though? b/c memory location is constant)
  - O(1) time (worst case, when inserting element in the front of the list. Same when inserting in the middle of the list. O(n/2) we drop the constant in Big-O notation, hence, O(n)). Also when we are removing elements in the middle b/c we then need to reshift the right side of the elements to the left side.
  ```
You create an array of integers (assume each integer is exactly 4 bytes) in memory, and the beginning of the array (i.e., the start of the very first cell of the array) happens to be at memory address 1000 (in decimal, not binary). What is the memory address of the start of cell 6 of the array, assuming 0-based indexing (i.e., cell 0 is the first cell of the array)?

1000 + 4 * 6
4 * 6 (bytes) instead of 8 * 4 * 6 (bits) b/c smallest chunk in memory is byte
  ```

Array Lists as "dynamic":
1. allocate some **default "large" amount of memory** initially,
2. insert elements into this initial array,
3. once initial array is full, **create a new larger array** (typically twice as large as the old array),
4. **copy** all elements from the old array into the new array, and then replace any references to the old array with references to the new array


```
Array structures (e.g. the array, or the Java ArrayList, or the C++ vector, etc.) require that all elements be the same size. However, array structures can contain strings, which can be different lengths (and thus different sizes in memory). How is this possible?

Every element contains pointers (memory addresses) to beginning of string

```

#### Summary:
- finding an element in a **sorted Array List** is O(log n) in the worst case, accessing a specific element is O(1)
- inserting into an **Array List** is O(n) in the worst case and finding an element in a non-sorted Array List is O(n)


## Linked Lists

![linked_list](https://github.com/kammybdeng/data-science-portfolio/blob/master/img/linked_list.png)

- data structure composed of nodes
- nodes are "linked" to one another via pointers
- one global *head pointer* and one global *tail pointer* (the only two nodes with direct access)

```
Write a function find(Node* node, int element) that starts at the given node and either returns true if the element exists somewhere in the Linked List, otherwise false if the element does not exist in the Linked List.


class Node:
    def __init__(self):
        self.value = None
        self.next = None

def find(node, element):
    current = node
    while current:
        if current.value == element:
            return True
        current = current.next
    return False

```

### Comparison between Array List and Linked List:
- Array List
  - PRO: can be optimized with binary search when "finding"
  - CON: needed to allocate extra space to avoid recreating backing ArrayList
- Linked List
  - PRO: constant time O(1) when inserting and deleting and dynamic allocation of memory of new node
  - CON: can't be optimized with binary search when "finding", stuck with O(n)



## Skip Lists

![skip_list](https://github.com/kammybdeng/data-science-portfolio/blob/master/img/skip_list.png)
A data structure that expands on the Linked List and uses extra forward pointers with some random number generation to simulate the binary search algorithm achievable in Array Lists.

![skip_list_2](https://github.com/kammybdeng/data-science-portfolio/blob/master/img/skip_list_2.png)


1. To find an element **e** in a Skip List, we start at the head in the highest layer.
2. When given layer i, we traverse (or move forward on) the forward pointers until *just before* we reach a node that is larger than **e** or until there are no more forward pointers on level i.
3. Then, move down one layer and continue the search.
4. If **e** exists in our Skip List, we will eventually find it (because the bottom layer is a regular Linked List, so we would step through the elements one-by-one until we find e).
5. Otherwise, if we reached down to layer 0 and still couldn't find **e**, then **e** does not exist.

```
What is the worst-case time complexity to find or remove elements from a Skip List?

O(n) (because if the heights of the nodes in the list are distributed poorly, we will effectively have a regular Linked List,)

Assuming the heights of the nodes in a Skip List are optimally-distributed (i.e., each "jump" allows you to traverse half of the remainder of the list), what is the time complexity to find or remove elements from a Skip List?

O(log n)

```

Can optimize the best distribution of heights to enable Skip List "find" algorithm to perform binary search, resulting in a O(log n) time complexity.


- Bernoulli distribution - random variable that has two possible outcomes (1 and 0)
- Binomial distribution - sum of independently, identically distributed **Bernoulli** random variables
- Geometric distribution - Given a Bernoulli distribution, the probability distribution of kth trial results in the last failure(1-p) before the first success(p). Pr(𝑋=𝑘)=(1−𝑝)^𝑘𝑝


Can sample from the Geometric distribution following Pr(𝑋=𝑘)=𝑝^𝑘(1−𝑝) to find out the height of each new node. Formula changed here, because we are interested in the **first failure(k)** instead of the **first success**.



```
To determine the heights of new nodes, you use a coin with a probability of success of p = 0.3. What is the probability that a new node will have a height of 2?


Pr(𝑋=2)=𝑝^2(1−𝑝)
Pr(𝑋=2)=(0.3)^2(0.7) = 0.063

```

## Circular Array

![circular_array_1](https://github.com/kammybdeng/data-science-portfolio/blob/master/img/circular_array_1.png)

![circular_array_2](https://github.com/kammybdeng/data-science-portfolio/blob/master/img/circular_array_2.png)


- Array List: random access, but a long time to insert
- Linked List: short time to insert, but long time to find/access
- Circular Array:
  - with heads and tail pointers -> faster to insert b/c just change pointers
  - with array list structure -> faster to access


```
What is the worst-case time complexity for an "insert" operation at the front or back of a Circular Array?

O(n)

What is the worst-case time complexity for an "insert" operation at the front or back of a Circular Array, given that the backing array is not full?

O(1)

```

## Abstract Data Types

A model for data types where the data type is defined by its behavior from the point of view of a user of the data

```
Which of the following statements are true about an Abstract Data Type?

1. Any implementations of an Abstract Data Type have a strict set of functions they must support
2. An Abstract Data Type is designed from the perspective of a user, not an implementer

```

### Deques
In short, an **Abstract Data Type** simply describes *a set of features*, and based on the features we wish to have, we need to choose an appropriate **Data Structure to use as the backbone** to implement the ADT.

```
If we only care about adding/removing/viewing elements in the front or back of a Deque﻿ (and not at all in the middle), which of the two implementation approaches we discussed would be the better choice? Doubly Linked List or Circular Array?

Doubly Linked List
Both data structures have equal time complexities, O(1), to add/remove from the ends, but a Circular Array cannot grow indefinitely and has to be resized once the backing array is full, whereas the nodes in a Linked List can be allocated dynamically (so it can grow indefinitely)
```

### Queues
Queue is considered a "First In, First Out" (FIFO) data type.



### Stacks and Queues

Stack - last in, first out (LIFO)

Push - adds an item to a stack
Pop - extracts the most recently pushed item from the stack

For arrays, stacks do have a maximum size, for linked-list, they don't.


## Graphs

Direct vs Undirected
Weighted vs Unweighted
Dense (when the number of edges is close to the upper bound) vs Sparse
*Upper Bound: |E| = |V| * |V| = |V|^2*
