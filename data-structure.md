# Data Structure

Data Structure - a particular structured way of storing data in a computer so that it can be used efficiently


[Big O](#Big-O)
[Array lists and linked list](#Array-lists)
[Stacks and Queues](#Stacks-and-Queues)


### References
https://stepik.org/course/579/


# Big O
Efficiency of Algorithm.

Time Complexity - the time complexity of a given algorithm tells us roughly how fast the algorithm performs as the input size grows

Big-O ("Big-Oh") - upper bound
Big-Ω ("Big-Omega") - lower bound
Big-ϴ ("Big-Theta") - upper bound and lower bound

Example: Print 5 header lines and  then prints the n students' names and grades on separate lines.
Number of operations = 2n + 5
Big-O notation would be O(2n + 5)
we would simplify to O(n) because we drop the constant (2n becomes n) and drop all lower terms (5 < n as n becomes large)
we always want to describe them using the tightest possible upper-bound



Space Complexity








Side notes:
Fibonacci Sequence: xn = xn-1 + xn-2
Naive Algorithm (recursive with 1.77 x 10^21 lines of code for N=100) vs Efficient Algorithm (array list with 202 lines of code for N=100)



### Array lists
constant-time access (read and write)


### Linked lists


### Stacks and Queues

Stack - last in, first out (LIFO)

Push - adds an item to a stack
Pop - extracts the most recently pushed item from the stack

For arrays, stacks do have a maximum size, for linked-list, they don't.
