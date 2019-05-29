# UCSanDiegoX: CSE100x Data Structure
**UCSanDiegoX: CSE100x**

**Data Structures: An Active Learning Approach**

Data Structure - a particular structured way of storing data in a computer so that it can be used efficiently

- [Big O](#Big-O)
- [Classes of Computation Complexity](#Classes-of-Computation-Complexity)
- [Bit-by-Bit](#Bit-by-Bit)
- [Array lists and linked list](#Array-lists)
- [Stacks and Queues](#Stacks-and-Queues)


### References
https://stepik.org/course/579/


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



### Array lists
constant-time access (read and write)


### Linked lists


### Stacks and Queues

Stack - last in, first out (LIFO)

Push - adds an item to a stack
Pop - extracts the most recently pushed item from the stack

For arrays, stacks do have a maximum size, for linked-list, they don't.
