### Week 4 started on 12/12/2023
#### Learning Objectives
- **Main** Explore how CNNs can be applied to multiple fields, including art generation and face recognition, then implement your own algorithm to generate art and recognize faces.
- Differentiate between face recognition and face verification
- Implement one-shot learning to solve a face recognition problem.
- Apply the triplet loss function to learn a network's parameters in the context of face recognition.
- Explain how to pose face recognition as binary classification problem.
- Map face images into 128-dimensional encodings using a pretrained model.
- Perform face verification and face recognition with these encodings
- Implement the Neural Style Transfer.
- General novel artistic images using Neural Style Transfer.
- Define the style cost function for Neural Style Transfer.
- Define the content cost function for Neural Style Transfer
### What is facial recognition?
- Face verification vs face recognition
  - recognition is much harder than verification.
- **Face Verification**: input image, name/ID.
  - Output whether the input image is that of the claimed person
- **Recognition**: has a database of K persons, get an input image, output ID if the image is any of the K persons (or "not recognized")
- Recognition is harder because there are K-1 chances of getting it wrong.
### One Shot Learning
- Learning from one example to recognize the person again.
- A small training is not good. What if a new person joins your team? You will have to retrain the neural network?
#### Learning a "similarity" functon
- d(img1, img2) = degree of difference between images
- If d(img1, img2) <= tao "same"
    else > tao "different"
- Learning this function d allows us to solve the one shot learning problem.
