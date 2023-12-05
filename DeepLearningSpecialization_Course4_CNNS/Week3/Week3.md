### Week3 Deep Learning Course #4
- Apply CNNs to the hottest and (most challenging) field in computer vision: object detection.
- Objectives:
- Identify the components used for object detection (landmark, anchor, bounding box, grid,...) and their purpose
- Implement object detection
- Implement non-max suppression to increase accuracy
- Implement intersection over union
- Handle bounding boxes, a type of image annotation popular in deep learning.
- Apply sparse categorical crossentropy for pixelwise prediction.
- Implement semantic image segmetation on the CARLA self-driving car dataset
- Explain the difference between a regular CNN and a U-net
- Build a U-net
#### Object Localization
- Image classification (1 Object)
- What are localization and detection?
- Localization: Where in the image is the object (1 object)
- Detection: What is the object detected. (multiple objects)
- You can have a CNN output 4 parameters (b_x, b_y, b_h, b_w) and these are the parameters of the bounded box. ![Alt text](image.png)
- ![Alt text](image-1.png)
  - P_c is saying whether an image was detected in the image or not.
  - Then the 3 spaces at the end are for detecting if it was a perdesterian, car, or motorcycle
  - We mostly care about how well the network is predicting the first space which is P_c
#### Landmark Detection
- In general cases you can have the neural network generate x and y coordinates which are the landmarks of some stuff you wanted the neural network to detect.
- What are landmarks? ![Alt text](image-2.png)
- As opposed to a bounded box as shown on the left. The neural network detects points in a image as shown on right.
- You can detect as many landmarks as you want!
- Someone will have had to go through a laboriously generate all of these landmarks.
### Object Detection
- Use the building blocks from the previous sections
- Sliding windows detection algorithm
#### Sliding Windows Detection
- You slide a bounded box across the whole image. Going through every region of the image to detect a object. ![Alt text](image-3.png)
- There is a huge disadvantage to this which is the computational cost.
  - Increasing the stride can improve cost but reduce the performance.
- The sliding windows can be implemented much more efficiently. Which we will see in the next video/section
### Convolutional Implementation of Sliding Windows
#### Turning FC layer into convolutional layers
- ![Alt text](image-4.png)
- You do this conversion by adding filters.
- On the bottom half of the image those are not FC layers but the places where the FC layers were converted into convolutional layers.
#### Convolution implementation of sliding windows
- ![Alt text](image-5.png) This method shares the computation in the areas of the image where there is overlap. As you can see there are four possible sliding windows in the whole image (color coded)
- Is this basically compression?
- This algorithm has one problem. the position of the bounded boxes are not going to be too accurate
### Bounding Box Predictions
#### YOLO Algorithm
- You Only Look Once
- ![Alt text](image-6.png)
- P_c is only assigned on the grid where the center of the image lies
- ![Alt text](image-7.png)
- For each of these 3x3 grid cells there is a corresponding 8 dimensional vector.
- This is a convolutional implementation. there is one shared computation for all of the 3x3 grid cells.
#### Specify the Bounding Boxes
- b_x, b_y, b_h, b_w are specified relative to the grid cell
- ![Alt text](image-8.png)
- In the next few videos he will show ideas that can make this algorithm even better.