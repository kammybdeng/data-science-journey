
## Week 1
## Nearest Neighbor Classification

MNIST images: 
- size 28 x 28 (784 pixels total)
- each pixel is grayscale: 0-255
- each image is transformed into a 784 dimension vector with [R1, R2, ..., R28]

R1 - Row 1 of 28 pixels

Euclidean distance(L2 distance)

Accuracy of nearest neighbor on MNIST
- In general, training error is an overly optimistic predictor of future performance
- What test error would we expect for a **random classifier**? (one that picks a label 0-9 at random?)
    - **90%**
- test error of a nearest neighbor on test set of 10,000 points
    - **3.09%**

### Improving Nearest Neighbor 
1. K-nearest neighbor classification
    - find *k numbers* of nearest neighbors in the training set
    - then return the most common(majority) label amongst these *k* neighbors

How to find the best k?
- Cross-validation
- find the k with the lowest error rate
- Final(average) error rate = sum(e1,...., en)/n, where n is the number of folds

2. Better distance functions
    - L2 distance between slightly shifted images is high
    - want a distance function that allows small translation and rotations 
    - **tangent distance** or a board family of natural deformation, **shape context**

#### Related problem: feature selection
- feature selection is part of picking a distance function
- noisy feature can disrupt nearest neighbors

#### Algorithmic issue: speeding up NN search
- Naive search takes time O(n) for training set of size n!
- Luckily, we have some other data structures for speeding up NN search, like:
    1. locality sensitive hashing
    2. ball trees
    3. k-d trees


## Distance Functions
1. Lp norms
2. Metric spaces

Measuring distance is R^m
**1. Lp norms**
- usual choice: Euclidean(L2), which is p=2, L2
- P = 1: sum(|xi - zi|)
- P = 2: sum(|xi - zi|^2)^(1/2)
- P = infinity: maxi|xi - zi|

**2. Metric spaces**
- d(x,y) >= 0 (nonnegativity)
- d(x,y) = 0 if and only if x = y
- d(x,y) = d(y,x) (symmetry)
- d(x,z) <= d(x,y) + d(y,z) (triangular inequality)

Example: Edit distance
- d(x,y): number of insertion, deletion, substitution

A **non-metric distance** function: Kullback-Leibler divergence or relative entropy between p, q, where p, q be probability distributions on some set X.

p = (1/2, 1/4, 1/8, 1/8)
q = (1/6, 1/3, 1/3, 1/6)


## Week 2
## Generative Approach to Classification

If a coin is flipped 5 times, what is the size of the sample space(the set of all possible outcomes) for the experiment?
- 2^5 = 32


## Week 6
## Support Vector Machines





Course: https://www.edx.org/course/machine-learning-fundamentals-3




## Data Preprocessing
## Python - Object-oriented programming

Class - the entire model/structure
Object - the instance of the class
Method - the tool that can be used on the object instance


# Decision Trees
- CART (Classification and Regression Trees)
- Each split is to reduce entropy(disorder), thus trying to maximize homogeneity in child nodes compared to the parent node.
- Information gain = decrease in entropy
- Gain(T, X) = Entropy(T) - Entropy(T, X)

### False Positives and False Negatives

- False Positives - Type I error
- False Negatives - Type II error (missing a real positive - might be more serious. Though cases vary on context of the problem)

## Ensemble learning
Steps:
1. Pick at random K data points(subset of sample) from training set
2. Build Decision Tree associated to these K data points
3. Choose the number of Ntree of trees you want to build and repeat Steps 1 and 2
4. For new data point, each one of your Ntree tree will predict a category. The final result is the majority vote from your Ntree trees result.

## "Commitee" decision vs Boosting

    "Commitee" decision
    - trivial examples
    - equal weights (majority vote)
    - might want to weight unevenly

    Boosting
    - focus new learners on examples that others get wrong
    - train learners sequentially
    - convert many "weak" learners into a complex predictor

### Random Forest(Majority vote)


### Gradient Boosting

the weak learner trains on the remaining errors (so-called pseudo-residuals) of the strong learner



#### XGBoost (Gradient Boosting)


### AdaBoosting

Changes the sample distribution by modifying the weights attached to each of the instances. It increases the weights of the wrongly predicted instances and decreases the ones of the correctly predicted instances.

Course: https://www.quora.com/What-is-the-difference-between-gradient-boosting-and-adaboost
