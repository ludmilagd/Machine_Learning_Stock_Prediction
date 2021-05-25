# Machine Learning for Stock Market Prediction

## Analyzing Apple Stock Data to Predict Gain/Loss leveraging Machine Learning Models
### Data Source: Yahoo Finance

## Overview:

Stock market prediction can be a very profitable business, reason why it has been on the eye of investors and individuals for a long time. World's economy is constantly fluctuating as a complex mix of trends and unpredicted events. The need for better ways to predict the future value of stocks is key to financial success and we decided to use Machine learning to explore this topic.

Machine Learning has proved to be a good predictor for stock prices. However, there are several Machine Learning Models and techniques that can be used in the financial field. 

It is the intend of this project to compare predictions of the most popular models available applied specifically to Apple Stock Prices.

Since some analysts like to compare Stock Price History for low and high Price of the targeted company to other industries, a chart of stock prices for a few other companies was included in the last tab of the application.

## Process
ML is a data analytics technique that teaches computers how to learn from the data without the need of an equation as model. For this project, supervised learning was selected to achieve predictive analytics. 
To utilize Machine Learning advanced technology, the team used Jupyter Notebook to develop Python code to extract required data and also to create, train and validate the model.
Yahoo Finance was used as data source to retrieved historical stock prices up to the previous day that this application is being accessed.
The four models selected to predict Apple Stock Price are: Moving Average, LSTM (Long-Short-Term Model), Decision Tree and Linear Regression. 


### Data loading 
Yahoo finance is a reliable and free source of information for stock prices and offers 5 years of history. Python has a module that wraps the Yahoo Finance API that can be called relatively easy and provides information up to the previous day. This project incorporates this python module to train and validate the models, and also to gather information to later be plotted in the application.

## Visualization

Dash plotly was the tool selected to present the results of this analysis. Dash is a JavaScript library that combines Flasks, HTML and charting capabilities to create interactive visualizations with amazing features. The Flask application connects a local host service to storage information retrieved from yahoo finance and from a local/github drive to later be plotted and rendered in an HTML format file. The final application was launched to the internet in Heroku Platform. Heroku is a cloud platform that allows users to deploy and run applications in a cloud

Technologies: Herouku, Python (SciPy package), Matplotlib, Pandas & Dash Plotly Machine Learning Models: Moving Average, LSTM (Long Short Term Model), Decision Tree and Linear Regression.

Link to Dash application deployed to the web through Heroku (Cloud Application Platform)

https://g8-stock-prediction.herokuapp.com/


![image](https://user-images.githubusercontent.com/70984918/119550630-4361f200-bd5e-11eb-8834-31773ce13087.png)

![image](https://user-images.githubusercontent.com/70984918/119550658-478e0f80-bd5e-11eb-88bb-81e929d78e3c.png)

![image](https://user-images.githubusercontent.com/70984918/119550671-4bba2d00-bd5e-11eb-878e-34a6bd1e1890.png)

![image](https://user-images.githubusercontent.com/70984918/119550682-4eb51d80-bd5e-11eb-9561-22dd8988d034.png)

![image](https://user-images.githubusercontent.com/70984918/119550693-51177780-bd5e-11eb-9805-37bda73a4af4.png)

Development Team

Christine Brown
Doris Meiere
Ludmila Garcia
Victoria Jeshurun
Lizzie Stenhaug
