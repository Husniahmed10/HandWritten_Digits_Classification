# Handwritten Digits Classification using Deep Learning

This project implements a handwritten digit recognition system using deep learning, specifically Convolutional Neural Networks (CNNs), to classify images of handwritten digits from the MNIST dataset. The model is built using TensorFlow and Keras, and the project also includes a Flask web application for making predictions through a user interface.

## Project Overview

The goal of this project is to classify images of handwritten digits (0-9) into their corresponding digit using a Convolutional Neural Network (CNN). The CNN is trained on the MNIST dataset, which consists of 28x28 pixel grayscale images of handwritten digits. The trained model can be used to predict handwritten digits uploaded by users.

### Key Features

- **Digit Recognition:** Classify handwritten digits from 0-9.
- **Web Interface:** Upload an image of a handwritten digit, and get the predicted digit using a Flask web application.
- **Model Performance:** The model is trained on the MNIST dataset using a CNN with multiple convolutional and fully connected layers, optimized with Stochastic Gradient Descent (SGD).
- **User Interface:** Interactive interface to upload images and view predictions in real-time.

## Technologies Used

The following technologies were used to build this project:

### 1. **TensorFlow and Keras**
   - **TensorFlow:** An open-source machine learning framework developed by Google. It is used for training and deploying deep learning models.
   - **Keras:** A high-level API for building and training deep learning models, which is integrated into TensorFlow. Keras provides an easy-to-use interface to define neural network architectures.
   
### 2. **Convolutional Neural Networks (CNNs)**
   - CNNs are a class of deep neural networks commonly used for image classification tasks. This project leverages CNNs for recognizing and classifying handwritten digits.
   - The architecture includes convolutional layers for feature extraction and fully connected layers for classification.

### 3. **Flask**
   - **Flask:** A lightweight Python web framework used to build the backend of the web application. Flask handles user requests, loads the trained model, processes the uploaded image, and returns the predicted digit.
   - The web server allows users to upload images and receive digit predictions via a REST API.
   
### 4. **JavaScript, HTML, and CSS (Frontend)**
   - **HTML:** Used to build the structure of the web page where users can upload images.
   - **CSS:** Provides styling for the web page to make it user-friendly and visually appealing.
   - **JavaScript:** Handles client-side interactions, such as image previewing, form submissions, and displaying prediction results.
   
### 5. **Pillow (PIL)**
   - **Pillow:** A Python Imaging Library used to process and manipulate the uploaded images before passing them to the model for prediction. It is used to convert images to grayscale, resize them, and normalize the pixel values.

### 6. **Werkzeug**
   - **Werkzeug:** A comprehensive WSGI web application library used by Flask to handle file uploads and other utilities.

### 7. **NumPy**
   - **NumPy:** A core library for scientific computing in Python. NumPy is used to handle image arrays and numerical data.

### 8. **Model File (models.h5)**
   - **H5 Format:** The trained model is saved in HDF5 format (.h5) using Keras' `model.save()` method. This file contains the architecture, weights, and training configuration of the CNN model.


