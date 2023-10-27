### Week 2 Course 3 Deep Learning
### Error Analysis
#### Carrying Out Error Analysis
- Andrej said it was suprising how many different tasks you can fine tune an AI model to work on well.
- See if its worth it to improve the error rate of a ML model. Base it on how much of that data is actually in your dataset.
  - For example say you have a 100 images and 5 images are of dogs in the data set and 5% of it is mislabeled in the dev set. And you have a total train error of 10%. It may not be worth it to focus on improving the loss because there won't be much reduction in the training error rate.
#### Evaluate Multiple Ideas in Parallel
- You can use a spread sheet to evaluate what gets mislabeled incorrectly and labeled correctly in the dataset
- Find your mislabeled categories in the dev set(because the dev set is what you use for tuning.). You can create new categories if you notice something particular that is messing up your classifier.
#### Cleaning Up Incorrectly Labeled Data
- The human label on the data is incorrect in the train set.
- DL algorithms are quite robust to random errors in the training set!
  - Wow! Why?
- Incorrectly Labeled Data on Dev or Test set
  - In your error analysis spreadsheet have a column for Incorrectly Labeled data.
  - ![Error Analysis Spreadsheet](image.png)
  - Plot errors for:
    - Overall dev set error
    - Errors due to incorrect labels
    - Errors due to other causes
- Goal of dev set is to help you select between two classifiers A & B.
#### Correcting incorrect dev/test set examples
- Apply same process to your dev and test sets to make sure they continue to come from the same distribution.
- Consider examining examples your algorithm got right as well as ones it got wrong.
  - Maybe something you change will make what is classified correctly go down.
- Feeding data to deep learning usually works. But manually looking at examples has its place in applied deep learning.
  - Getting an understanding of what your ML algorithm is getting wrong and right can help you decide what to prioritize on quicker and better.
#### Build your First System Quickly, then Iterate
- First setup dev/test set metric
- Build Initial system quickly
- Use Bias/Variance analysis & Error analysis to prioritize next steps.
- This advice applies less strongly if you have a lot of experience in the area you are building or there is a lot of academic literature in the area you are building.
  - Do not overthink it.
  - Do not underthink it.
  - Andrew Ng on average have seen a lot of teams overthink it.
### Mismatched Training and Dev/Test Set
#### Training and Testing on Different Distributions
- You have 200,000 images from one distribution and 10,000 images from another distribution
- Option 1: Shuffle these images together.
  - Adv: Train, test, and dev has the same distributions
  - Disadv: the proportion of the 10k distribution is much smaller than the 200k distribution.
- Option 2: Have training set 200k + 5k(from 10k), dev and test set will be all from 10k dist.
  - Adv: You are aiming the target where you want it to be if you really care about the 10k distr.
#### Speech Recognition Example
- Say you have worked on speech recognition before and you have a lot of data from those previous attempts, but not on the current problem.
- Training: all the data you have from previous experiences etc.
- Dev/Test
  - Set it what you actually care about optimizing for.
  - Assuming you do have as much data for this thing.
- Another option
  - Train set: has all of your previous data + some data from the thing you actually care about
  - Dev/Test: the data for the target thing you care about
### Bias and Variance with mismatched data dist
- The way you analyze bias and variance changes when the distribution of the test/dev and train set is different
#### Cat Classifier Example
- Assume humams get close to 0% error.
  - Training error .... 1%
  - Dev error .... 10%
- Training-dev set: same dist as training set but not used for training. Use that to tease out the variance and importance of the bias we have seen.
  - Training Error: 1%
  - Training-dev: 9%
  - Dev error: 10%
    - This shows that you have a variance problem. Look at difference between training error and training-dev error.
    - training-dev set is basically what the dev set would have been if there was not a difference in the dist between training and dev sets.
- Another example:
  - Training Error: 1%
  - Training-dev Error: 1.5%
  - Dev Error: 10%
    - There is a data mismatch here looking at the differnce in error rate between training-dev and dev.
    - Somehow your neural network has learned to do well on a different distribution of data.
- Another another example:
  - Human Error: 0%
  - Training Error: 10%
  - Training dev error: 11%
  - Dev Error: 12%
    - Avoidable bias is quite high between human error and training error
- Another another another example:
  - Human Error: 0%
  - Training Error: 10%
  - Training dev error: 11%
  - Dev Error: 12%
    - There are 2 issues there is the avoidable bias problem between the human error and the training error and the data mismatch problem between training-dev error and dev error.
#### Bias/variance on mismatched training and dev/test sets
- !The errors you should worry about](image-1.png)
- Example to show that this is possible:
  - Human Error: 0%
  - Training Error: 10%
  - Training dev error: 6%
  - Dev Error: 6%
### Addressing Data Mismatch