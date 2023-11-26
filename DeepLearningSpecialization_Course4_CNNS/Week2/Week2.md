### Week 2 Deep Learning Course 4
#### Why look at case studies?
- One way to get better at building neural networks is to look at examples.
- After the next few videos you will be able to look at computer vision papers and be able to understand them.
#### Outline
- Classic Networks (How were these determined to be classic?)
  - LeNet-5
  - AlexNet
  - VGG
- ResNet (152 layer neural network)
  - Some tricks on how to build large scale neural networks
#### Classic Networks
- LeNet - 5 [paper link here]
  - Goal was to recognize hand written digits.
  - How do we go from a 32 x 32 x 1 image to a 28 x 28 x 6 output if the filter size is 5 x 5 and there are 6 filters ?
  - ![Alt text](image.png)
  - ![Alt text](../Week1/image-1.png)
  - ^ I know the formulas but how does this work? The image gets reduced in size because that is how the convolutional operation works. See below.
  - ![Alt text](<0 1CwfqZHE9fGu774w.gif>)
    - We are using the filter to do the convolutional operation. The filter is being sliden across the image then we are doing a matrix mutliplication with that part of the image and the filter contents. Its the rules of matrix multiplication that is the driving force behind the reduction of the image.
- **Advanced Details** on paper
  - 1. People were not using ReLU back then.
  - 2. Something
  - 3. This neural network had a nonlinearity after the pooling layer.
  - This is one of the harder papers. Focus on reading section 2 and some of section 3.
- AlexNet [paper link here]
  - Had a lot of similarities to LeNet but was much bigger.
  - Also used ReLU
  - **Advanced Details**:
  - Trained on multiple GPUs
  - Local Respose Normalization (not used much)
    - Motivation for this is at each position it will normalize the image across the channels so that there are not too many neurons with a high activation.
    - So that there are not too many neurons with a high activation at each position
    - Researchers have found that this does not help much.
  - This is the paper that really introduced deep learning to computer vision
  - This is a good paper to start with looking at.
- VGG - 16 [paper link here]
  - Its a much simpler network with less hyperparameters.
  - CONV = 3x3 filter, s = 1, same
  - MAX-POOL = 2x2, s = 2
  - The simplicity of this architecture made it appealing even though its quite large even by modern (2020) standards
- Architectures of these classic neural networks visualized:
  - This will help me to understand the papers
  - LeNet - 5
  - ![Alt text](image-1.png)
  - AlexNet
  - ![Alt text](image-2.png)
  - VGG - 16
  - ![Alt text](image-3.png)
- These networks are classic because now there are even more powerful networks.
#### ResNets
- Very very deep neural networks are hard to train because of vanishing and exploding gradients problem.
- ResNet aims to solve that problem.
#### Residual block
- WTF is this shit?
- Residual blocks have mutliple residual skip connections
- ![Alt text](image-5.png)
- Supplemental Resource Notes below [https://towardsdatascience.com/residual-blocks-building-blocks-of-resnet-fd90ca15d6ec]:
- In a traditional neural network each layer feeds onto the next layer.
- In a network with residual blocks, each layer feeds into the next layer *and* directly into layers about 2-3 hops away.
- With a resnet you can have the training error go down as the number of layers go up. I need to understand why this works.
- ![Alt text](image-6.png)
  - Single Residual Block
- Neural networks are **universal function approximators** and the accuracy increases with the number of layers. (I think I know what this is saying. Its trying to find a function that fits every problem and the number of layers is important because???)
- there is a limit to the number of layers that can be added though because of the vanishing and exploding gradients problem and the curse of dimensionality (which was???)
  - Curse of Dimensionality is a set of problems related to the high dimensionality of data. I cannot think of the intuition for any at the moment.
- The degration problem:
  - Shallower networks train better than deep ones because for the deep networks we will see that the accuracy will saturate at one point and eventually degrade. And this is usuaully not caused due to overfitting!!
    - So why not skip these extra layers and match the accuracy of the shallow sub-networks. But how?
    - We can learn the identity function by skipping layers that is why there is a identity on the *Single Residual Block* image
    - **Stopped at trying to understand the Residual Block**
#### Why ResNets work?
- ![Alt text](image-7.png)
  - This explains where the ResNet will find the identity function. If W^[l+1] = 0 it just returns a^l
  - You can have a weight in front of the a^[l] we are passing in the residual connection. This will be a matrix mult.
- Very deep networks have struggles learning the identity function. Since ResNets help performance then that means that it should be able to not hurt performance.
#### Networks in networks and 1x1 Convolutions
#### What does a 1x1 convolution do?
- ![Alt text](image-8.png)
  - The top 1x1 convolution does nothing but the bottom one is good.
  - The bottom thing is whats called a network in network convolution.
#### Using 1x1 Convolutions
- What if the number of channels has gotten too big and you want to shrink.
- ![Alt text](image-9.png)
- 1. Can help add or reduce the number of channels in a network
- 2. Can be used to add a nonlinearity to the CNN
### Inception Network Motivation
- You can use whatever filter sizes, pooling layers, and just concatenate the outputs and have the network choose the ordering of it?
#### The problem of computational cost
- ![Alt text](image-10.png)
  - Without 1x1 convolutions this will take a 120M multiplies.
#### Using 1x1 convolution
- ![Alt text](image-11.png)
- This will only use a 12.4M multiplies.
- Shrinking down the neural network does not seem to hurt the performance (the bottleneck layer)
#### Inception Network
#### Inception Module
- ![Alt text](image-12.png)
- So there is some side branchs
- ![Alt text](image-13.png)
  - The side branches are being used to make a prediction to make sure that the hidden layers are being trained reasonably.
- Inception Networks are called GoogleNet to pay homage to the LeNet.
- If you understand the inception module then you can understand the inception network. The inception network is basically the inception module repeated.
### MobileNet
- Some practical advice on buildng these kinds of neural networks
#### Motivation for MobileNets
- Low computation cost at deployment
- This is useful for mobile phones.
- Depth-wise separable convolutions are beneficial here.
#### Normal Convolution
![Alt text](image-14.png)
#### Depthwise Separable Convolution
- There is a 2 steps
- 1. There is a depthwise convolution
- 2. Then there is a pointwise convolution
- ![Alt text](image-15.png)
- Now lets flesh this out!
#### Depthwise Convolution
- ![Alt text](image-16.png)
#### Pointwise Convolution
- ![Alt text](image-17.png)
#### Cost Analysis
![Alt text](image-18.png)
#### MobileNet Architecture
- Everywhere you would have used a normal convolution you can now use a depthwise and pointwise convolution.
- ![Alt text](image-19.png)
- We renamed pointwise convolution to Projection for reasons that we will learn about soon.
#### MobileNet v2 Bottleneck
- ![Alt text](image-20.png)
- We are projecting down from a nxnx18 to a nxnx3 therefore the pointwise convolution is called a projection.
- The mobile bottle neck layer will be repeated 17 times
#### EfficientNet
- You want to adjust to different edge networks scaling up or down based on the amount of resources available to you.
- ![Alt text](image-21.png)
### Practival Advice for using ConvNets
#### Using open-source implementations
- A lot of these neural networks are difficult to replicate based on only reading the paper.
- Look online for an open source implementation of the paper it can help speed up progress/
  - This is probably what I would do first before trying to implement a paper from scratch.
#### Transfer Learning
- You can download weights that someone else has used on a architecture. They have probably trained with lots of resources and time to build this network. They have done the hyperparameter tuning already.
- You can freeze to only train softmax layers weights but freeze the other layer's weights
  - ![Alt text](image-22.png)
- You can save to disk and then train a softmax classifier on top of that.
### Data Augmentation
- You need more data
#### Common  Augmentation Method
- Mirroring
- Random Cropping
  - In practice it works well.
#### Color Shifting
- RGB
- Sometimes called "PCA color" augmentation
- This was talked about in the AlexNet Paper.
#### Implementing Distortions During Training
- You have a stream of images coming from the hard disk. You can use a CPU thread to do the distortion to the image. Then the image is passed to some other thread to do training.
- Use someone else's open source implementation to get started for data augmentation. If there is some variation that hasn't been done before then you may need to tune these hyperparameters yourself.
### State of Computer Vision
#### Data vs. Hand-Engineering
- <--- Little Data ------ Image Recognition --------- Lots of Data --->
- ![Alt text](image-23.png)
- We just don't have enough data for computer vision.
- Transfer of Learning helps a lot when there is little data
#### Tips for doing well on benchmarks/winning competitions
- Ensembling
  - Train serval networks independently and average their outputs.
  - Not used in production but used mainly for benchmarks
- Multi-crop at test time
  - Same thing like ensembling. This is primarily used for benchmarks.
#### Use open source code
- Use architectures of networks published in the literature.
- Use open source implementations if possible
- Use pretrained models and fine tune them on your dataset.
### Quiz for this week
- I got a 60% on the first quiz. And I had to use chat gpt for one of the questions on MobileV2. This sucks ;|
1. What is the use of 1x1 layers?
   -
### Homework
- Read the AlexNet paper [https://paperswithcode.com/method/alexnet]
- This has been one of the most confusing weeks of this whole course. Hopefully everything is as simple as Andrew Ng has laid out in these videos and I just have to deepen my understanding of things by diving into these papers. Start with the paper he said is the easiest to get into and build momentum from there that is my strategy.