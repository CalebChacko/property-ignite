# 🏡 Property Ignite 🔥
This project focuses on integrating a machine learning (ML) model into an Android app to help investors find real-estate areas with higher rates of return (ROR).

## Overview
Entering the real-estate industry can be daunting. With many variables to consider and a rapidly changing market, it can be difficult to find a user-friendly entrypoint. Thankfully, there are many tools and resources that can equip new investors enter the space. However, these tools come at a cost of time and money. On top of that, these resources may not directly help users beginning buying properties. 

To address this problem, both Jason Dourado and myself (Caleb Chacko) have created an idea to guide investors to investigate specific areas that may lead to higher rates of returns. The idea is to abstract away some of the variables needed to understand real-estate and allow more people to enter this space. 

Our project focuses on two key technical areas:

1. Training an ML model to rate locations of a city based on ROR given a variety of input features
2. Displaying these rates on a heatmap to help users identify communities that are hot 🔥 based on user constraints (i.e. amount to invest, length of investment, etc.)

## Rate of Return (ROR) Model 📈
**Managed by Caleb**

The process of designing our model includes:
- Data Ingestion
- Exploratory Data Analysis
- Model Training
- Model Validation
- Model Deployment

### Data Ingestion

For any project, data is crucial and this project is no exception. Finding real-estate data online for free is challenging. Recently, Zillow, one of the the largest free real-estate APIs, removed their API and added a costly premium tier for its users. With many other APIs lacking in quality data, we decided to scrape data rather than use an API. This method will only be used for proof-of-concept. Once the concept is functional, we look to implement our model with a real-time API. 

The data we collected is sorted into 3 categories: location, house specs, and financial house history. We may publish this project in the future, so no specific features will be disclosed. 

For our proof-of-concept, we will be using Mississagua, Ontario. The population of the city is 1 million and is currently experiencing a hot sellers market. 

### Exploratory Data Analysis (EDA)
This task is still in development. Once more information is ready, it will be added to this readme. 

### Model Training, Validation, and Deployment
This task is still in development. Once more information is ready, it will be added to this readme. 


## Application Development 📱
**Managed by Jason**

Our application design is solely focused on the heatmap with any user constraints. 

<img src="https://github.com/CalebChacko/property-ignite/blob/main/assets/android_heat_map.PNG" width="100"/>

<!-- <img src="./Assets/android_heat_map.PNG" width="100"/> -->


