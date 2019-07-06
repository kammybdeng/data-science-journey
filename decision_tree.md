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

# References
https://www.quora.com/What-is-the-difference-between-gradient-boosting-and-adaboost
