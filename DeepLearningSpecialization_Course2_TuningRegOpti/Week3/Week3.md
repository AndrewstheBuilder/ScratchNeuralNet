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
- Normalizing the input features can speed up learning.
  - X = X / $\sigma$
    - $\sigma$ is the variance
    - How do I build the intuitions for how these things are working?
    - I vaguely remember this but I do not remember exactly how it was working.
  - Makes the search space more rounded as opposed to being elongated. Remember from earlier?
  - **Variance** - measures how far a set of numbers are spread out from their average value.
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
#### Implementing Batch Norm
- Rewatch this! Its a bunch of math

#### Fitting Batch norm into a Neural Network