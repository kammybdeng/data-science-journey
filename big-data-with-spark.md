# UCSanDiegoX: DSE230x Big Data Analytics Using Spark
**UCSanDiegoX: [DSE230x Big Data Analytics Using Spark](https://www.edx.org/course/big-data-analytics-using-spark)**

### Contents

- [Memory Latency](#Memory-Latency)
- [Spark vs Hadoop](#Spark-vs-Hadoop)

## Memory Latency

- In Big Data, the major source of **latency** is reading and writing to storage.
- **Latency**: the amount of time a packet of data takes to get from one designated point to another
- **Caching** : reduces storage latency by bringing relevant data close to the CPU

- **Cache Hit**: able to retrieve from cache
- **Cache Miss**: when byte is not in Cache, need to free up space in cache and replace
- **Temporal Locality**: multiple accesses to *same* address within a short time period
  - example: the parameters/weights in a model
- **Spatial Locality**: multiple accesses to *close-together* address within a short time period
  - Benefits:
    - memory is partitioned into Blocks/Lines and *memory locations that are close to each other are likely to fall in the same block*, resulting in more cache hits

#### Traversal of 6 elements touches 4 pages in **Linked List**
![linked_list](https://github.com/kammybdeng/data-science-portfolio/blob/master/img/spatial_locality_1.png)


#### Traversal of 6 elements touches 2 pages in **Array**
![linked_list](https://github.com/kammybdeng/data-science-portfolio/blob/master/img/spatial_locality_2.png)

```
What is the primary reason that a linked-list will cause more cache misses than an array?

Linked list elements are not stored in consecutive memory locations.

```


```
Given the following code, determine which type of locality is present:

A = [0]*10000
sum = 0
for i in range(10000):
    sum += A[i] + i

Spacial locality

```

### Memory Hierarchy
- *top* of hierarchy: small and fast storage close to CPU
- *bottom* of hierarchy: large and slow storage further from CPU

- Data Processing Cluster: many computers linked through an ethernet connection
  - storage is shared
  - "caching" is replaced by "shuffling"
  - *Spark RDD* (Resilient distribution dataset)

### Row-wise vs Column-wise Scanning

Traversing a numpy array *row-wise* is faster than *column-wise* because of locality.

### Memory Hierarchy
- *top* of hierarchy: small and fast storage close to CPU
- *bottom* of hierarchy: large and slow storage further from CPU

- Data Processing Cluster: many computers linked through an ethernet connection
  - storage is shared
  - "caching" is replaced by "shuffling"
  - *Spark RDD* (Resilient distribution dataset)


### Spark vs Hadoop
- Hadoop: distributed files
- Spark: distributed memory

#### Spark Context
- PySpark program runs on the main node and control is achieved with a *SparkContext* object
- A notebook can have only one *SparkContext* object

### Hadoop File System (HDFS)
- break down files into chunks, make copies, and distribute copies randomly to multiple commodity computers.

![HDFS](https://github.com/kammybdeng/data-science-portfolio/blob/master/img/HDFS.png)

#### Resilient Distributed Dataset (RDD)
- main data structure in Spark
- a list with no direct access to, because it's distributed
- RDD1 -> RDD2 is a lineage
- RDD2 can be consumed as it is being generated
- By default are not **materialized**: stored in memory. *They do materialized if cached or otherwise persisted.*
