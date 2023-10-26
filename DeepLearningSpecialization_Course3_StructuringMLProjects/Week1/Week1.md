## Course 3: Setting up Your ML Projects (Week 1)
### Why ML Strategy
- He has seen teams go out to collect data only to realize that is not what they wanted.

#### Orthogonalization
- Its like having a single knob to tune a single function
- You don't want to couple features. Imagine you had a car and a knob that tunes 0.3 of the angle you turn and 0.7 of your speed.

#### Chain of assumptions in ML
1. Fit trainset well on cost function
   - Bigger network
   - Adam optimizer
2. Fit dev set well on cost function
    - Regularization
    - Biggest training set
3. Fit test set well on cost function
    - Bigger dev set
4. Performs well in real world
    - change dev set or cost function
- This makes it seem like data rules this part of the software world.
- Early stopping is an example of something that may affect both the training set and dev set.
  - How??? I do not get the intuition for this.

### Setting Up your Goal
#### Single Number Evaluation Metric
#### Understanding Precision and Recall
- Idea -> Code -> Experiment in a loop.
- Precision and Recall make literally zero sense to me right now.
  - Precision: totalPositive / (totalPositive + falsePositive)
    - or truePositive/actualResults
    - So the question now is how are (totalPositive+falsePositive) the actualResults ?
  - Recall: truePositive/(truePositive+falseNegative)
    - or truePositive / predictedResults
- These two metrics are only focused on the positive answer(which is the correct answer) and the metrics related to the predicted number of positive results (precision) vs the actual number of positive results(recall)
  - truePositives -> correctly classified positive results
  - precision = truePositives/predictedPositives
  - recall = truePositives/totalPositives
- F1-Score is the harmonic mean of the precision and recall values. Optimizing the F1-score means optimizing for precision and recall.
- We use accuracy in a multi-class problem when the data is evenly distributed between classes but precision/recall becomes more important when the data is unevenly distributed as is likely the case with real life situations.
- there is a precision/recall curve that shows the tradeoff between each and what it would be when there is a 100% on both precision and recall.
- Calculating area under the curve (AUC) in a precision/recall curve is good.
  - A classifier that tries to maximize the area under the curve is a good classifier. Maximizing AUC means you are maximizing both the precision and recall.
- (What is a harmonic mean?)
- An average is good when you have a ton of numbers and you have different classes of things with those numbers. And you want to figure out what the best thing is
### Setting up your goal
#### Satisficing and Optimizing Metrics
- Optimizing means it has to be the best possible
- Satisficing means it just has to meet a certain threshold and its good.
- In general, if you have N metrics pick 1 to optimize and N-1 for satisficing
#### Set up Train/Dev/Test Sets
- Having different distributions on dev and test sets is like trying to hit a target and optimizing for it and then at test time having a completely different target.
- Consider choosing a dev set and test set to reflect data you expect to get in the future and consider important to do well on.
#### Size of the Dev and Test Sets
- This is changing in the era of deep learning.
#### Old way of splitting data
- 70% train, 30% test
- 60% train, 20% dev, 20% test.
- these are for datasets like 100, 1000, 10,000
- In the era of deep learning the dataset is like 1 million.
  - 98% train, 1% dev, 1% test.
  - Wow but does this affect the models effectiveness in the real world having so few data to tune and finally validate on.
#### Size of test set
- Set your test set to be big enough to give high confidence in the overall performance of your system
- Train, dev split.
  - If you are tuning on the subset it should be called dev and not test.
  - You can have no test set.
    - But not recommended. Its better to get a unbiased view of your model.
    - I wonder if you are only allowed to validate on the test set once. That must be nerve wracking.
#### When to Change Dev/test sets and metrics
- When the metrics are predicting that an algorithm is nice but you as the user would prefer a different algorithm that is a sign you need to change your metrics or choose a different dev/test set.
- You can give a bigger weight to a classifier's weights that predicts porn images if that is what you would like the classifier to stop doing. The way to do that is through the labeling in your dev and test set??
  - He does not give the details
  - One way to define a new evaluation metric.
#### Orthogonalization for cat pictures: anti-porn
1. Determine the metrics
2. Worry separately about how to do well on this metric.
- Think about these two as two separate steps.
- If you do not have the metric or evaluation aspect defined well then just start with something
### Why human-level performance?
- Its much more feasible now to have human level performance.
- What Andrew Ng's seen:
  - Progress is rising pretty fast up to the human performance threshold when the model gets past that the progress tends to slow down.
    - There is a theoretical upper limit called the bayes optimal error.
  - bayes optimal error - best possible error
- 1. Human level performance is not that far from bayes optimal error
- 2. Worse than human level there are tools to use to bring the progress up
    - Labeled data from humans
    - Gain insight from manual error analysis: Why did a person get this right?
    - Better analysis of bias/variance
#### Avoidable Bias
- Example 1:
  - Humans: 1%
  - Training error: 8%
  - Dev Error: 10%
    - Focus on bias. Try to do better on the training set.
- Example 2:
  - Humans: 7.5%
  - Training error: 8%
  - Dev Error: 10%
    - Focus on reducing variance. Might try regularization to bring dev error closer to training error
- Nothing can be better than bayes error.
  - I wonder how this is calculated.
- Avoidable Bias: Difference between bayes error or approximation of Bayes error and the training error.
  - This is not widely used terminology but its helpful for thinking about these things.
- Human level error can be seen as a proxy for bayes error because it usually is.

### Understanding Human Level Performance
- Human level error can be used to estimate Bayes error
- What is "human-level" error?
  - Imagine having a regular person, a typical professional, an experienced professional, and a team of experienced professionals.
    - This is in order of decreasing error rate
    - Which of these error rates would you choose?
- Bayes error is less than or equal to the smallest error rate we get.
- Should I focus on the avoidable bias or reducing variance? That is the question to answer.
  - You will focus on the bigger one.

### Surpassing human-level performance
- Once you have surpassed human level performance its harder to use human intuition to solve the problem.
#### Problems where ML significantly surpasses human-level performance
- Online adverstising
- Product recommendations
- Logistics (predicting transit time)
- Loan approvals
- All of these are:
  - Structured data
  - Not natural perception
  - Looked at more data than any single human ever has.
### Improving your Model Performance
#### The two fundamental assumptions of supervised learning
1. You can fit the training set pretty well
   - Avoidable bias
2. The training set performance generalizes pretty well to the dev/test set.
   - Variance
#### Reducing (avoidable) bias and variance
- Reducing avoidable bias:
  - Train bigger model
  - Train longer/better optimization algorithms
    - RMS Prop, Adam, etc
  - NN Architecture/Hyperparameters search
    - RNN and CNN
- Reducing variance:
  - More data
  - Regularization:
    - L2, dropout, data augmentation
  - NN architecture/hyperparameters search
- These concepts are easy to learn but hard to master.

### Quiz for Week 1 Machine Learning Flight Simulator
- The analogy to a flight simulator is that these are used to train pilots and they experience situations that allow them to improve much faster because they might not have encountered these problems in real life flying
- "Instead of spending years working on a machine learning project before you get to experience certain scenarios, you'll get to experience them right here."
- This is the first time this "airplane simulator" for machine learning strategy has been made widely available.
  - Maybe I can learn much faster than machine learning researchers do from work experience.
#### Questions from the Quiz'
1. Having three evaluation metrics makes it harder to choose between two different algorithms and will slow down the speed with which your team can iterate?
   - **True**
5. Can I add a new distribution of data to the training set?
   - yes. Adding data to the training set will change the training set distribution. However it is not a problem to have a different distribution between training and dev set. In constrast, it is **problematic** to have different test and dev set distributions

