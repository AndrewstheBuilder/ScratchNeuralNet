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
- Idea -> Code -> Experiment in a loop.
- Precision and Recall make literally zero sense to me right now.
  - Precision: totalPositive / (totalPositive + falsePositive)
    - or truePositive/actualResults
    - So the question now is how are (totalPositive+falsePositive) the actualResults ?
  - Recall: truePositive/(truePositive+falseNegative)
    - or truePositive / predictedResults
- These two metrics are only focused on the positive answer(which is the correct answer) and the metrics related to the actual number of positive results (precision) vs the predicted number of positive results(recall)