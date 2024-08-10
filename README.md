# Mildew Detector in Cherry Leaves

The Mildew Detector is an application that can predict whether a an individual cherry leaf is healthy or contains powdery mildew. 

The app is built around a supervised ML model that performs binary classification with single-label predictions. 

[Live Application](https://hb-mildew-detection-3fcc7e940ca3.herokuapp.com/)

![Device Mockup](/workspace/mildew-detector/docs/images/device-mockup.png)

## Dataset Content

* The image dataset is a dataset retrieved from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves). For this project, a hypothetical user story was applied to utilise predictive analysis to business criterias that could be implemented in a real case scenario. 

* The dataset consists of over 4000 images taken of healthy and mildew infested cherry leaves, collected from the company Farmy & Foods' cherry crops. Cherry tress can be infected with the fungus Podosphaera clandestina, resulting in powdery mildew on the leaves. To check the trees manually for mildew is a tedious, time-consuming process for employees. The application was designed to streamline the process. When mildew is being detected in an individual of the crops, a compound can be applied to kill the fungus. 

## Business requirements 

The business requirements for the application from client was the following: 

1. The client is interested in conducting a study to visually differentiate a cherry leafthat is healthy from one that contains powdery mildew.

2. The client is interested in predicting if a cherry tree is healthy or contains powdery mildew.

## Hypothesis and how to validate

- Cherry leaves infected with powdery mildew is expected to have clear marks/signs, spread in patches over the leaf, that can differentiate them from healthy leaves. 

- An Image Montage shows that typically a mildew infested leaf has white-ish marks across it. Although, Average Image, Variability Image and Difference between Averages studies did not reveal any clear pattern to differentiate one from another.

## Rationale to map the business requirements to the Data Visualizations and ML tasks

### Business requirement 1: Data Visualization 

1. Display mean and standard deviation: 
   * Show statistics for healthy leaves and leaves infested with powdery mildew 
   * Implement visual differentiation between the two types 

2. Compare average leaves: 
   * Display the difference between an average healthy leaf and an average mildew infested leaf 
   * Visualize the distinction between the two types

3. Create image montages: 
   * Provide montages of healthy cherry leaves and leaves infested with powdery mildew
   * Visualize the differentation between the two types

### Business requirement 2: Image Classification 

1. Predict leaf health: 
   * Develop capability to determine whether a a given cherry leaf is healthy or infested with powdery mildew 

2. Model development and reporting: 
   * Build a machine learning model 
   * Generate adequate reports 

## ML Business case 

* From the given dataset, we want to construct an ML model that can predict if a cherry leaf contains powdery mildew or not. 

* The purpose of the model will be the streamlining of verification of the status of a cherry tree, to determine whether it needs treatment or not. 

* The model output will be put as a flag, with the ability to predict if a leaf contains powdery mildew or not, and give it the label of 'healthy' or 'powdery mildew'. The image will be uploaded directly into the application. 

* The model success metrics has so far been set at 100% on the given test set 

* The training data has been obtained from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves), with an image dataset consisting of 4208 images. The images have been uniformed to (256, 256, 3). 

## Dashboard design 

### Page 1: Quick Project Summary 

