# Machine Learning for Stock Market Prediction

Analyzing Apple Stock Data to Predict Gain/Loss leveraging Machine Learning Models

Data Source: Yahoo Finance

Overview: 

Stock market prediction can be a very profitable busines, reason why it has been on the eye of stock inverstors for a long time. World's economy is constantly fluctuaring as a complex mix of trends and unpredicted events. The need for better ways to predict the future value of stocks is always present.

Machine Learning has proved to be a good predictor for stock prices. However, there are several Machine Learning Models and techniques that can be used in the financial field. It is the intend of this project to compare some of the most popular models aviabale to predict Apple Stock Prices. 

Since some analyst like to compare history of the low and high Price of the targeted company to other industries, a chart of stock prices for a few other companies was included in this applications. 

**Process**

In order to achieve the goal, the team created the Python coding for each of the selected Models using Jypoter Notebook. Yahoo Finance was used as data source

**Data loading**
Yahoo finance is a reliable and free source of information for stock prices and offeres 5 years of history. Python has a module that wraps the Yahoo Finance API that can be called relativly easy and provides information up to the previous day. This project incorporates this python module to train and validate the models, and also to gather information to later be ploted in the application.

**Model Training and Validation**

The Machine learning models were processed in jupiter notebook utilizing Python, Pandas and Matplotlib to create trend charts. The results of the different models were saved in Github to later be used by the application.

**Visualization**

Dash plotly was the tool selected to present the results of this analysis. Dash is a Javascript library that combines Flasks, HTML and charting capabilities to create interactive visualizations with amazing features. The Flask application connects a local host service to storage information retrieved from yahho finance and from a local/github drive to later be ploted and rended in an HTML format file.
The final application was launched to the internet in Heroku Plataform. Heroku is a cloud plataform that allows users to deploy and run applications in a cloud

The four models selected are: Moving Average, LSTM (Long Short Term Model), Decision Tree and Linear Regression. 
In this applciation, built in Dash JavaScript, will provide the user three different Machine Learning Models to predict Stock Market Value for Apple. 
It also present a chart to compare historical Stock price for companies in different Industry Sectors. 

Technologies:Herouku, Python (SciPy package), Matplotlib, Pandas & Dash Plotly 
Machine Learning Models: Moving Average, LSTM (Long Short Term Model), Decision Tree and Linear Regression. 

Link to Dash application deployed to the web through Heroku (Cloud Application Plataform) 

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
