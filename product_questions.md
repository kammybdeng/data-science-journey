# Product questions

## Outline

- Understand the business
- Goal
- Customer
- KPIs, metrics of success
- Pain points

----
Current business problem/goal
Profit
Revenue, expense
Fraud detection etc.
Growth - number of users
LTV, CAC, engagement etc.
Acquisition - WOF, viral, organic search,
Conversion - behaviors, understand preferences
Retention - expand and sustainability
Resurrected - periodic analysis on # of users



### Test the hypothesis
A/B test
Stats
Independency (control group should not affect the treatment group and vice versa)
Matching markets
Pros - more independency (b/c behaviors of users within the same market will greatly affect (relatively) the others )
Cons - noisy, does not guarantee consistency and similarity, and not much markets are a “good match” - market bias
Matching individuals



Result
A/B test
Stats
Novelty effect
selection bias
Seasonality - compare previous years data
Product
Cost and effect from a business perspective to decide deploy or not
Survey
Stats
selection bias



### Machine Learning model (assist in analysis & making predictions & finding patterns on big data)
General types of models
- Classification (Fraud, Churn vs no churn etc.)
Fraud
Anomaly detection - identifying abnormal patterns
- Regression (housing prices)
Missing values
In practice vs academia
In practice - missing values actually tells us something about the users, hence, we do not want to replace it with something else
Academia - often replaced with median, mean, and etc.
Prediction

### Why is it so important?
b/c for long-term metrics, we cannot wait till 1 year to see the result, hence we use a short-term proxy to predict the long-term metrics
Train model with previous short term proxy and have long term metrics as the targets, then from the short-term data we collected through A/B tests, we can then make long-term predictions

### Additional notes

- Defining the right metric to measure
- Type of business

- Outliers dominated
- Metrics are sensitive to outliers
- Outliers are rare
- Metrics not sensitive to outliers
- Vanity metric vs Clarity metric
Ex. number of downloads vs.active engagement time with product (software-based)
Ex. how much each customer buys vs how often they buy (E-commerce)



- Cohort Analysis
- Partition users into different cohorts/groups based on their time of entrance or other factors
- Funnel analysis
- Sequences of events performed by users
- Churn
- Failed charge



### How to calculate for how long I should run an A/B test? (How to estimate the sample size in a t-test)

- Significant level -  0.05
- Power - 0.8
- Expected sample deviation of the change
- Minimum effect size you are interested in detecting

Calculated require sample size /  # of traffic per day = # days
- If # days >= 14 - good to go
- If # days < 14 - would still want to run for 14 days to capture weekly pattern, but can split into 80% control and 20% treatment to avoid wasting traffic


### What are the drawbacks of using supervised machine learning to predict fraud

Imbalanced class
Ways to correct:
- Internal loss function to penalize false negative
- Aggressive cut-off point
Other drawbacks
If misclassified as legitimate before, the model could recognize this pattern and mis-predict it to be legitimate again

People find new ways to commit fraud -> won’t be able to keep up
More reliable technique
- Anomaly detection - detect abnormal patterns
  - Yet, in the beginning the model will be very noisy (curse of dimensionality). Will need to invest a lot of time and effort to shorten the dimension to meaningful features(indicators)

Combination of both
- Follows the fraud pattern -> fraud
- Demonstrates anomaly pattern -> fraud

### Give an example of a case in which you run an A/B test, test wins with significant p-value, but you still choose not to make the change (what are the cost of making the change)

Some examples of cost:
- Human labor cost
- Engineering time to make the change, product to draft the documentations, customer service to help with questions
- Risk of bugs
- Consider short term cost and long term cost
- Justify the gain is worthy and “relevant” (product team)
- Check if the test was a multiple comparison problem -> if so, the significance level should not be 5%
b/c # false positive = # variables * 0.05


### Do you expect that Uber trips without rider reviews have been better, worse, or same as trips with reviews? (handling missing value)

- Because riders decides whether or not to leave reviews(not random, self-selection bias), the distribution for the missing values will not follow the distribution of the non missing values
- Build a machine learning model to predict these ratings
- In practice, we could expect that they are related to bad experience b/c some cultures don’t want to give bad ratings (domain knowledge)
- However, if this is an input to another model, better to not replace the rating
Can insert -1 as to distinguish this group from the rest

### If 70% of Facebook users on iOS use Instagram, but only 35% of Facebook users on Android use Instagram, how would you investigate the discrepancy?

- It really means: “when predicting Y, is X (mobile operation system) a discriminant variable or not”
- If yes, what’s the actual difference? If not, what are the actual discriminant variables?
- Analysis: the OS could just be the proxy for other variables such as age, country, education b/c Americans are more likely to use the iOS system and Instagram
- Build decision tree with user-related variables and the OS to predict Instagram usage, if the top splits are on the user-related info that means OS is merely a proxy
- If OS is really the root cause that means one app is better than the other. Thus, we can further collect variables like loading time, user clicks bugs, and etc.

### At Facebook we use as a metric number of likes per user per week. And, each week, we check it year over year to control for seasonality. This week, the metric is dramatically down. How would you find out the reason? Logging is fine as well as the query we used to get the data.

- Break down the metric decrease/increase by steps and investigate individually
- Numerator vs Denominator (this year/ last year) , (total numbers of likes / total numbers of users)
Where is the majority fall?
- Additional users signed up -> but much less engaging
- Build a tree model. Label users during the “up weeks” as 1 and other previous weeks as 0. Look at the top splits, they will tell the characteristics of these new users
- Then conclude to a single country/area that have an increase/decrease in numbers of users, then state a hypothesis
- Local marketing campaign -> up vs local competitor launch -> down
- If we concluded that the number of likes went down, most likely it’s because of bugs

### How would you measure the performance of the customer service department?


- All departments should either relate to revenue or growth. This one can be rephrased into a growth problem
In another word, if the performance is great, we should be able to retain and gain users, if not, otherwise.
- If we want to increase LTV
    - Find a short-term proxy for this long-term metric
- We can define 1 for users who had the customer service ticket and bought stuff within 1 year, and 0 otherwise.
- Then we build a tree to see which variable most highly impacted the categorization, then that will be the variable that we are interested in

### FB- should we add a love button? (New feature implementation)


- Find the proxy to see if there’s already a demand in the market
- Use NLP to go through comments to see if they are related to the love category -> then this shows demand
- Pick a crucial metric that will predicted to be highly impacted by this change
- User engagement - number of actions (likes/comments/post/etc.) per user within a certain time frame.


### You were launching a messaging app. Define 2 metrics that you’d choose to monitor app performance during the first months. Why do you chose them?

- Applies to any newly launched products
- Goal: Growth (targeting growth as the high level goal)
- Ultimately, as many users as possible and want the number of engaged users to go up over time
- Acquire new users (new signups / day - users that have message >= 1 message within the first X days)
- Retain current users (avg. messages / day / user) -> if possible, choose something that will incentivize other users actions
- Avoid vanity(futility/pointless) metrics
- One way to check: would lots of fake accounts affect our metric


### You have to predict conversion rate on Airbnb using user country as one of the input variables. How would you deal with the missing values in “country”?

In practice, the high, high majority of these missing values come from the fact that the users chose not to give (privacy setting, not completing profile) -> these are valuable info of users
If we can predict the missing values with other variables, we can include those variables into a model that works well with correlated variables (like tree-based models)
Safest Approach
Label missing values as “no_country”
Use other variables like IP address, service provider that can provide insights of the missing value and include them into the training set
Then we will know whether or not they filled out the country section and where they are based

### How to estimate the value of a user coming to your e-commerce store when they land on your home-page for the first time (How much should we pay for a click on our ad that leads to our site/ estimate LTV)

Define LTV
Total revenue per user within first year of first visit
Sometimes, the value is greater than this b/c network effect that users can bring in other users
Approach:
Collect previous data and train
Browsing behaviors - the source they came from
SEO - keyword they searched for
Ads - ad text
Direct link - search engine
Continuous predictions (Regression trees)
Assign a predicted $ to each segment


### Which variables are important to predict a fake listing on eBay?

- Characteristics of listings
- Not genuine/organic image
- Similar text/description
- Low price
- Characteristics of seller
- Unique IP address, bank account, credit card # -> check if they associate with multiple user accounts
no/little ratings
- Browsing behavior - spend too less time/ too familiar with the website


### Explain the drawbacks of running an A/B test by market (i.e all people in one market get version A and another market get version B)


- Users in different markets will never be as similar as the users in the same market
- Assuming full independence btw. users in different markets might be a stretch
- Past metrics show similar behavior, but could react differently in a new testing
- External factors - competitor launches, political events
- Only test “relevant” features, features that are supposed to be highly impacted by user behaviors

### Suddenly, our dashboard shows that the number of picture uploads per day by Internet Explorer users went to zero. What could be the reason?

- Segment users by various features
- Browser, device, country, etc.
- Technical issues/bugs
- The upload button is not working (front-end)
Unable to record the picture upload action (back-end)
Query that access the table is not working properly (DBMS)
unable to visualize the metric on Dashboard b/c of Dashboard code error/bugs (DBMS)

### How would you find out if someone put a fake school on LinkedIn? I.e. they actually didn’t attend it (in progress)


Number of connections (first degree, second, third degree) from that school and year
Location



### You are supposed to run an A/B test for 3 weeks based on sample size calculation. But after 1 week, p-value is already significant with test winning. So your product manager pressures you to stop the test and declare it a winner. What would you tell her?

Sport match analogy
Soccer
Leading team doesn’t necessarily mean that they will win, there’s a fixed time frame we need to get through to have a determination


### Between the following two metrics, which one would you choose to measure response time of an inquiry at Airbnb:
percent of responses within 16 hours; or
average response time considering only responses within 16 hours

 1 is better.
Includes the entire population
Not sensitive to outliers
Yet only focus on providing good enough experience
Can have one aggressive (within 1 hour) or one lenient (within 16 hours)


### In on-line gaming companies, do you expect the average revenue per user to be larger or smaller than the median revenue per user? Assume the following business model: free for download and in-app purchases


The median will be smaller than the mean, because the distribution will be skewed to the right (a lot of users use the freemium plan and only a few making high amounts of purchase)
We want the model be able to capture the outliers -> model that will be sensitive to the outliers -> tree-based models would not be a good model

### How would you increase revenue from advertising clicks if you were working or an ads company

- Break down ad click revenue
- CTR (click through rate) - probability of users clicking the ad when they see it
- Total number of ads shown to users
- Cost per click
- Think of scenarios that would bring up the ratio
- Increase CTR by better targeting - build products that
