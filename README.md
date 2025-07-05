# Autonomous_Self_Driving_Cars
A Computer Vision project using Neural Networks
## Overview

This project aims to develop a self-driving car system using computer vision techniques and neural networks. Initially, data is collected using the Udacity simulator, following which it is preprocessed to remove biases. We draw inspiration from Nvidia's 2016 [research paper](https://images.nvidia.com/content/tegra/automotive/images/2016/solutions/pdf/end-to-end-dl-using-px.pdf) on end-to-end deep learning for self-driving cars.

## Data Collection

Data collection is performed using the Udacity simulator, which provides a realistic environment for training the model. The simulator allows users to drive a virtual car and records data such as images and corresponding steering angles, throttle, reverse and speed in a CSV file.

To collect data, follow these steps:
1. Download the Udacity simulator executable file [Check out their github repo](https://github.com/udacity/self-driving-car-sim.git).
2. Run the simulator on your system and navigate through various scenarios to capture diverse driving conditions.

## Model Training

Following the approach outlined in Nvidia's paper, we train a neural network model on the collected data. The model is trained to predict steering angles directly from images, effectively learning the mapping from raw sensory data to steering commands.

The trained model is saved in an HDF5 file format using keras.

## Simulation and Real-Time Control

Initially, the model is deployed in the Udacity simulator to observe its performance. However, it becomes apparent that the model may be overfitted to the specific tracks in the simulator.

To address this issue, we shift our focus to edge detection techniques for self-driving cars. Real-time screenshots of the car's video feed are captured, preprocessed using OpenCV, and subjected to Canny edge detection algorithm developed by John F. Canny in 1986. 

The edges are further processed to derive their derivative, and based on the positive-to-negative ratio, control commands are generated using Python's `keyboard` module.

## Usage

To run the project, follow these steps:

1. Ensure you have all the necessary dependencies installed. You can find the requirements in the `requirements.txt` file.
2. Launch the Udacity simulator and run the `drive.py` file to connect it to the Python script using SocketIO and Flask.
3. Select a track on the autonomous mode and see the car drive itself.
4. Now, download Trackmania and build a track for the lane detection algorithm.
5. Execute the main script, which will capture real-time screenshots, process them, and generate control commands for the car.

## Demo Video 
https://youtu.be/oW5gA0JFwbM

## Acknowledgments

This project builds upon the work of Nvidia's research paper on end-to-end learning for self-driving cars. We also thank the creators of the Udacity simulator for providing a valuable platform for data collection and testing. We also thank @entBabby for their comprehensive tutorial on self-driving car using Convolutional Neural Network.

## Contributing

Contributions are welcome! If you have any ideas for improvement or want to report issues, feel free to open an issue or submit a pull request.
 
