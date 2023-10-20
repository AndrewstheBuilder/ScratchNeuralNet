## Week 3
### Hyperparameter Tuning
#### Hyperparameters
- One of the pain points of ml is the sheer number of hyperparameters you have to tune.
- alpha, beta1, beta2, epsilon, # layers, # hidden units....
- alpha is the most important hyperparameter to tune for most archs.
- some hyperparameters are much more important than others
#### Try random values: Don't use a grid
- Have a graph of hyperparameters. 2D graph
  - Choose points at random instead of using a grid.
#### Coarse to fine
- Zoom into a particular point in the graph and try more points in that region. sample more densely
#### Using an Appropraite scale to pick Hyperparamters
- Sampling at random does not mean across the uniform scale/
##### Picking hyperpar at random
- Sample uniformly at random. Instead of the normal scale you can use the log scale to sample more uniformly across the range of numbers. For example sampling numbers between 0.00001 - 1.
  - In the linear scale, there are a lot less numbers between 0.0001-0.1 as opposed to 0.1-1
    - You spend 90% of your resources sampling between 0.1 and 1 and 10% sampling between 0.0001 - 0.1.
    - What he means by the log scale is 10$^r$
    - r = -4 * np.random.rand() <- r <- [-4, 0]
    - $\alpha$ = 10$^r$
    - Example of why this is called the log scale
      - say we are going from 0.0001 - 1
      - a = $\log_{10}(0.0001)$ = -4
        - 10$^r$ = 10$^4$ = 0.0001
    - To figure out the range of r just take the log of the start of the range(a) through to the end of the range(b).
      - a = log$_{10}$(start)
      - b = log$_{10}$(end)
      - Set r uniformly at random [a, b]
  - The log scale allows you to search the range of parameters to search faster.
- The linear scale does not allow us to pick uniformly
- What if the mathematical justification for this?
#### Hyperparameters Tuning in Pracrice: Pandas vs. Caviar
- Intuitions for hyperparameter tuning does change over time.
  - Re-evaluate once every several months
- One way to do it is to babysit one model. Watching the model as it trains.
  - Panda approach. Pandas usually only have one baby.
- Other approach is to train many models in parallel.
  - It could be the cost of the training set, dev set etc.
  - Fish have multiple babies so this can be called the caviar approach.
### Batch Normalization
#### Normalizing Activations in a Network
- Batch norm makes your hyperparameter search problem that much easier, makes your neural network more robust.
  - The choice of hyperparameters that work well is in a much bigger range.
#### Normalizing inputs to speed up learning
- "Unfortunately, terms are used differently in different fields, by different people within the same field, etc., so I'm not sure how well this can be answered for you here. You should make sure you know the definition that your instructor / the textbook is using for "normalized". However, here are some common definitions:" Reference: [stats-exchange](https://stats.stackexchange.com/questions/70553/what-does-normalization-mean-and-how-to-verify-that-a-sample-or-a-distribution)
- Normalizing the input features can speed up learning.
  - X = X / $\sigma$
    - $\sigma$ is the ~~variance~~.
      - Nope it is the standard deviation.
    - How do I build the intuitions for how these things are working?
    - I vaguely remember this but I do not remember exactly how it was working.
  - Makes the search space more rounded as opposed to being elongated. Remember from earlier?
  - **Variance** - measures how far a set of numbers are spread out from their average value.
    - Calculating the **mean** for a dataset might not give an exact answer if the dataset is always changing for example calculating the average amount of time american spends on t.v. People are dying and being born everyday so this value is always changing.
    - **Variance** is $\sigma^2$
    - **Standard Deviation** is $\sigma$
  - **Normalization** - rescales a dataset so that each value falls between 0 and 1. (got this searching for stat def of normalization)
    - From coursera Week 1 of this course
    - Normalization steps:
      - 1. Subtract mean to make the dataset have zero mean
      - 2. Normalize variance
        - $\sigma^2$ = $\dfrac{1}{m}$ $\sum_{i=1}^{m}$ X$^{(2i)}$
        - X /= $\sigma$
      - Use same $\sigma$ and $\mu$ for normalizing the test set.
      - Unnormalized cost function will be very squished out
        - X$_1$: 1....1000
        - X$_2$: 0....1
      - Normalized cost function needs much less oscillations to reach the minimum loss.
        - X$_1$: 0...1
        - X$_2$: -1...1
        - X$_3$: 1...2
        - See now input features are on a similar scale.
        - Normalizing makes the training go faster.
- **Batch Norm** normalizes the dataset.
#### Implementing Batch Norm
- Z tilda is computed because we do not want the hidden units to have the same distribution as unit variance and zero mean.
  - We introduce hyperparameters $\gamma$ and $\beta$
  - Without this adjustment it is basically calculating the identity function
    - An **Identity Function** is a function that always returns the value used as its argument, unchanged.
- Batch Norm should standardize mean and variance but $\gamma$ and $\beta$ will make sure it does not stay at the identity function range.
### Fitting Batch norm into a Neural Network
#### Adding Batch Norm to a network
- Each neural computes Z then has a afterwards which is the activation.
- Implementing batch norm is like one line of code in a deep neural network.
  - Not the apis right but the raw implementation?
#### Working with mini-batches
- We can get rid of the bias in mini batches because when we subtract out the mean it gets cancelled out.
  - How???
  - Oh batch norm zeros out the means so the bias does not do anything for us.
#### Implementing (mini-batch) Gradient Descent
- In each hidden layer use Batch Norm(BN) to replace Z$^l$ with $\stackrel{\sim}{Z}$
- We compute gradients for $\beta$ and $\gamma$

### Why does Batch Norm work?
- You have seen how normalizing input range of features to take on a similar range of values can speed up training. Batch Norm is doing the same thing for your hidden units.
  - This is just a partial picture. There are a couple of farther intuitions
#### Learning on shifting input distribution
- "Covariate shift" - the idea of the inputs changing. For example going from a input distribution of black cats to different colored cats. Your ML model may not be expected to generalize really well to the new input set.
#### Why this is a problem with neural networks?
- Batch norm reduces the amount the distribution of the hidden units changes
  - The mean and variance will stay the same as determined by $\beta$ and $\gamma$. It does not have to be mean 0 and variance 1.
- This weakens the coupling between the later layers and earlier layers.
#### Batch Norm as regularization
- Batch norm has a slight regularization effect
- each mini-batch is scaled by the mean/variance computed on just that mini-batch.
- This adds some noise to the values z$^{[l]}$ withint that minibatch. So similar to dropout, its teaching the unit not to rely too much on the previous layer. Each hidden layer's activations has a bit of noise.
- By using a bigger mini-batch you reduce this regularization effect
  - How???
- This was not the intended effect of batch norm.
- Batch norm uses minibatches so at test time you may need to do something different.
  - Why do we need to worry about doing something different at test time?
### Batch Norm at Test Time
- Batch norm handles data one mini batch at a time. It computes mean and variance across a single mini batch.
  - So at test time you might not have mini batches. So you may need to do something different to make sure your predictions make sense.
- We estimate mean and variance using exponentially weighted average(across mini-batch).
- In practice this is pretty robust of how the mean and variance actually is.
- Refresh yourself on why this needs to be done!!
- At test time you may not have the whole data set to compute mean and variance.
- $\mu, \sigma^2$ using exponentially weighted average (across mini batches)
  - You are keeping a running average as you come across these values.
  - Exponentially weighted average is sometimes called running average

## Multi-Class Classification
### Softmax Regression
- Imagine you have to recognize multiple classes instead of just binary classification. For exampel recognizing cats, dogs, and baby chicks
  - There would be 4 classes here because there is also an other if it is none of the above three classes.
#### Softmax layer
- This is what is used for the multi-class classification.
- Its the last layer.
- Here is how it works so we get Z$^l$ at the final layer (l)
  - Z$^l$ = [5,2,-1,3]
  - we take these to the power of e
    - t = $[e^5, e^2, e^{-1}, e^3]$
    - t = [148.4, 7.4, 0.4, 20.1]
    - ${\sum}_{j=0}^{5}$ $t_j$ = 176.3
    - a$^{[L]}$ = $\dfrac{t}{176.3}$
- I want to build a multi-classifier building of the Simple Neural Network I did but this time do it on something semi useful. I want to keep it simple so I will initially use linear activations.
  - 1. Find a cool dataset to model.
  - "But AI and data science have great value even for a pizza maker. He can use a linear classifier to predict which pizza might be popular at which time"
### Training a Softmax Classifier
#### Understanding softmax
- contrasting with a hard max [1, 0, 0, 0]. Where you just get a single 1 and the rest are 0s.
- A softmax has probabilities [0.842, 0.042, 0.002, 0.114]
- Softmax regression generalizes logistic regression to C classes.
  - If C = 2, softmax reduces to logistic regression.
  - For example: a$^[L]$ = [0.842, 0.158]. You will choose the first element
#### Loss Function
- we end up with a -log(correct_class) for the loss function. So we want to make the value of correct_class as high as possible to get a low loss.
- L($\stackrel{-}{y}$, y) = - $\sum_{j=1}^4 y_jlog\stackrel{-}{y}^{j}$
  - Make L() small
- J($W^{[l]}, b^{[l]}, ....$) = $\dfrac{1}{m}\sum_{i=1} ^ m L(\stackrel{-}{y}$, y)

#### Gradient Descent with Softmax
- Backprop: dz$^{[L]}$ = $\hat{y}$ - y
- $\hat{y}$ is the predicted probabilities by softmax.

## Introduction to Programming Frameworks
### Deep Learning Frameworks
  - Its more practical and efficient to use a deep learning framework to go about the process of building an AI.
  - Choosing deep learning frameworks
    - Ease of programming
    - running speed
    - truly open (open source with good governance)
      - Without governance companies may gradually chose to close it off in the future.
#### TensorFlow
- Tensorflow is dead apparently.
#### Motivating Problem
- Some cost function we want to minimize.
- Some complicated cost function depending on all of the parameters of our neural network. We need to use this deep learning framework to solve it.