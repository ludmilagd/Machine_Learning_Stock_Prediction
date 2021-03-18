import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import datetime as dt
import pandas_datareader as web



app = dash.Dash()
server = app.server

start = dt.datetime(2000,1,1)
end = dt.datetime.now()
df = web.DataReader('AAPL','yahoo', start, end)
df=df.reset_index()

df["Date"]=pd.to_datetime(df.Date,format="%Y-%m-%d")
df.index=df['Date']

data=df.sort_index(ascending=True,axis=0)
new_data=pd.DataFrame(index=range(0,len(df)),columns=['Date','Close'])

for i in range(0,len(data)):
    new_data["Date"][i]=data['Date'][i]
    new_data["Close"][i]=data["Close"][i]
    
new_data=new_data.set_index('Date')
dataset=new_data.values


tickers = ['TSLA','AAPL','FB','MSFT','SBUX']
df1 = web.DataReader(tickers, data_source='yahoo', start='2017-01-01', end=dt.datetime.now())
df=df1.stack().reset_index().rename(index=str, columns={"level_1": "Symbols"}).sort_values(['Symbols','Date'])
df["Date"]=pd.to_datetime(df.Date,format="%Y-%m-%d")
df.index=df['Date']


D_validationData= pd.read_csv("LSTM_validation.csv")
D_train_data= pd.read_csv("LSTM_train.csv")


fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=D_validationData["Date"], y=D_validationData["Close"],
                    mode='lines',name='Validation',line=dict(color="blue",width=4)))
fig2.add_trace(go.Scatter(x=D_validationData["Date"], y=D_validationData["Predictions"],
                    mode='lines',name='Stock Price Predicted ',line=dict(color="red",width=4)))
fig2.add_trace(go.Scatter(x=D_train_data["Date"], y=D_train_data["Close"],
                    mode='lines', name='Train',line=dict(color="darkblue",width=4)))


fig2.update_layout(hovermode='x unified',
    showlegend=True,
    plot_bgcolor="white",
    paper_bgcolor = "rgba(0,0,0,0)",
    xaxis_title="Date",
    yaxis_title="Closing Rate",
    legend_title="Data:",
    margin=dict(t=50,l=200,b=50,r=200),
    
)

fig2.update_xaxes(showline=True, linewidth=2, linecolor='white', gridcolor='lightgray')
fig2.update_yaxes(showline=True, linewidth=2, linecolor='white', gridcolor='lightgray')


moving_avg= pd.read_csv("test_mov_avg.csv")


fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=moving_avg["date"], y=moving_avg["close"],
                    mode='lines',
                    name='Test',
                    line=dict(color="darkblue",width=3)))
fig3.add_trace(go.Scatter(x=moving_avg["date"], y=moving_avg["est_N2"],
                    mode='lines',
                    name='Stock Price Predicted',
                    line=dict(color="red",width=3)))

fig3.update_layout(hovermode='x unified',
    showlegend=True,
    plot_bgcolor="white",
    paper_bgcolor = "rgba(0,0,0,0)",
    xaxis_title="Date",
    yaxis_title="Closing Rate",
    legend_title="Data:",
    margin=dict(t=50,l=200,b=50,r=200),
    
)
fig3.update_xaxes(showline=True, linewidth=1, linecolor='white', gridcolor='lightgray')
fig3.update_yaxes(showline=True, linewidth=1, linecolor='white', gridcolor='lightgray')

# Import CSV tree training data
Tree_training= pd.read_csv("Tree_training_data.csv")
Tree_prediction= pd.read_csv("Tree_model_prediction.csv")


figt = go.Figure()
figt.add_trace(go.Scatter(x=Tree_training["Date"], y=Tree_training["Close"],
                    mode='lines',
                    name='Training ',
                    line=dict(color="darkblue",width=3)))
figt.add_trace(go.Scatter(x=Tree_prediction["Date"], y=Tree_prediction["Close"],
                    mode='lines',
                    name='Validation',
                    line=dict(color="blue",width=4)))
figt.add_trace(go.Scatter(x=Tree_prediction["Date"], y=Tree_prediction["Predictions"],
                    mode='lines', name='Stock Price Predicted',
                    line=dict(color="red",width=2)))


figt.update_layout(hovermode='x unified',
    showlegend=True,
    plot_bgcolor="white",
    paper_bgcolor = "rgba(0,0,0,0)",
    xaxis_title="Date",
    yaxis_title="Closing Rate",
    legend_title="Data:",
    margin=dict(t=50,l=200,b=50,r=200),
    
)
figt.update_xaxes(showline=True, linewidth=2, linecolor='white', gridcolor='lightgray')
figt.update_yaxes(showline=True, linewidth=2, linecolor='white', gridcolor='lightgray')


# Linear Regression Model data
LR_train= pd.read_csv("LR_train.csv")
LR_prediction= pd.read_csv("LR_prediction.csv")

# Create figure lines for Linear Regression Model
figLR = go.Figure()
figLR.add_trace(go.Scatter(x=LR_train["Date"], y=LR_train["Close"],
                    mode='lines',
                    name='Training ',
                    line=dict(color="darkblue",width=3)))
figLR.add_trace(go.Scatter(x=LR_prediction["Date"], y=LR_prediction["Close"],
                    mode='lines',
                    name='Validation',
                    line=dict(color="blue",width=3)))
figLR.add_trace(go.Scatter(x=LR_prediction["Date"], y=LR_prediction["Predictionslr"],
                    mode='lines', name='Stock Price Predicted',
                    line=dict(color="red",width=3)))



figLR.update_layout(hovermode='x unified',
    showlegend=True,
    plot_bgcolor="white",
    paper_bgcolor = "rgba(0,0,0,0)",
    xaxis_title="Date",
    yaxis_title="Closing Rate",
    legend_title="Data:",
    margin=dict(t=50,l=200,b=50,r=200),
    
)

figLR.update_xaxes(showline=True, linewidth=2, linecolor='white', gridcolor='lightgray')
figLR.update_yaxes(showline=True, linewidth=2, linecolor='white', gridcolor='lightgray')


# Getting Info for all Models comparison
l30=dt.datetime.now()- dt.timedelta(30)
m_actual = web.DataReader('AAPL','yahoo', l30, dt.datetime.now())
m_actual=m_actual.reset_index()

# COMPLETE code to get models table
l30=dt.datetime.now()- dt.timedelta(30)

# Actual
m_actual_df = web.DataReader('AAPL','yahoo', l30, dt.datetime.now())
m_actual_df=m_actual_df.reset_index()
m_actual=m_actual_df[['Date','Close']]
m_actual["Model"]="Actual Close Price"
m_actual.rename(columns={'Close':'Predictions'}, inplace=True)

# LR
m_LR=LR_prediction[['Date','Predictionslr']]
m_LR["Model"]="Linear Regression Model"
m_LR.rename(columns={'Predictionslr':'Predictions'}, inplace=True)


# Tree Prediction
m_tree=Tree_prediction[['Date','Predictions']]
m_tree["Model"]="Tree Model"

# Moving Average
m_MA=moving_avg[['date','est_N2']]
m_MA["Model"]="Moving Average Model"
m_MA.rename(columns={'est_N2':'Predictions','date':"Date"}, inplace=True)
m_MA["Date"]=pd.to_datetime(m_MA.Date,format="%Y-%m-%d")
m_MA1 = m_MA[(m_MA['Date']>(dt.datetime.now()- dt.timedelta(30))) & (m_MA['Date']<dt.datetime.now())] 

# Long short-term memory
D_validationData["Date"]=pd.to_datetime(D_validationData.Date,format="%Y-%m-%d")
m_LSTM=D_validationData[['Date','Predictions']]
m_LSTM["Model"]="Long Short-Term Memory"
m_LSTM1 = m_LSTM[(m_LSTM['Date']>(dt.datetime.now()- dt.timedelta(30))) & (m_LSTM['Date']<dt.datetime.now())]  


# Model table
frames=[m_tree,m_actual,m_LR,m_MA1,m_LSTM1]
models=pd.concat(frames)
models

# HTML code to render results- Layout formating

app.layout = html.Div([
   
    html.H1("Apple Stock Price Prediction- Machine Learning & Python", style={'textAlign': 'center','color':'#07098d'}),
    html.H2("", style={'textAlign': 'center','color':'#07098d'}),
    dcc.Tabs(id="tabs", children=[
       
        dcc.Tab(label='LSTM',children=[
			html.Div([				
			    html.H2("Long Short-Term Memory (LSTM)", 
                        style={'textAlign': 'center'}),
                html.H3("On this LSTM Model 75% of the data was trained and 25% was tested to predict Apple stock price using the past 60 days closing price.", 
                        style={'textAlign': 'left'}),
                html.H3("The data was taken from Yahoo from 2010-01-04 to 2021-03-16. The LSTM-rsme is 24.37", 
                        style={'textAlign': 'left'}),
                html.H3("The predicted price for the March 17th = USS 123.5", 
                        style={'textAlign': 'left'}),
                html.H3("The predicted price for the March 18th = USS 128.5 ", 
                        style={'textAlign': 'left'}),


                dcc.Graph(id = 'GrapLTSM',
                        figure = fig2),
                     ]
                ),   		
        ]),


        dcc.Tab(label='Moving Average',children=[
			html.Div([				
			    html.H2("Moving Average to predict Apple Stock  Price", 
                        style={'textAlign': 'center'}),
                html.H3("The moving average is a simple technical analysis tool that smooths out price data by creating a constantly updating average.", 
                        style={'textAlign': 'left'}),

                dcc.Graph(id = 'GrapMovingAvg',
                        figure = fig3),
                    ]
                ),
        ]),

        dcc.Tab(label='Tree Model and Linear Regression',children=[
			html.Div([				
			    html.H2("Apple Sock Price Prediction For the Last 30 Days - Tree Prediction Model", 
                        style={'textAlign': 'center'}),
                # html.H3("Tree Model and Linear Regression Stock Prediction Tree Model and Linear Regression Stock Prediction Tree Model and Linear Regression Stock Prediction", 
                #         style={'textAlign': 'left'}),

                dcc.Graph(id = 'GrapTreeLR',
                        figure = figt),
                

                html.H2("Apple Stock Price For The Last 30 Days - Linear Regression Model", 
                        style={'textAlign': 'center'}),
                # html.H3("Tree Model and Linear Regression Stock Prediction Tree Model and Linear Regression Stock Prediction Tree Model and Linear Regression Stock Prediction", 
                #         style={'textAlign': 'left'}),

                dcc.Graph(id = 'GrapLR',
                        figure = figLR),
            ],className="container"),
            
        ]),

        dcc.Tab(label='Model Comparison', children=[
            html.Div([
                html.H2("Select Model to compare", 
                        style={'textAlign': 'center','color':'#07098d'}),
                                      
                dcc.Dropdown(id='my-dropdownM',
                             options=[{'label': 'Long Short-Term Memory', 'value': 'Long Short-Term Memory'},
                                      {'label': 'Moving Average','value': 'Moving Average Model'},
                                      {'label': 'Tree Model','value': 'Tree Model'}, 
                                      {'label': 'Actual Close Price','value' :'Actual Close Price'},
                                      {'label': 'Linear Regression', 'value': 'Linear Regression Model'}], 
                             multi=True,value=['Actual Close Price'],
                             style={"display": "block", "margin-left": "auto", 
                                    "margin-right": "auto", "width": "60%"}),
                dcc.Graph(id='models'),
                
            ], className="container"),
        ]),



        dcc.Tab(label='Stock Data other Companies', children=[
            html.Div([
                html.H2("Stocks Price comparison High and Lows", 
                        style={'textAlign': 'center','color':'#07098d'}),
                                      
                dcc.Dropdown(id='my-dropdown',
                             options=[{'label': 'Tesla', 'value': 'TSLA'},
                                      {'label': 'Starbucks','value': 'SBUX'},
                                      {'label': 'Apple','value': 'AAPL'}, 
                                      {'label': 'Facebook', 'value': 'FB'}, 
                                      {'label': 'Microsoft','value': 'MSFT'}], 
                             multi=True,value=['SBUX'],
                             style={"display": "block", "margin-left": "auto", 
                                    "margin-right": "auto", "width": "60%"}),
                dcc.Graph(id='highlow'),

                html.H2("Stocks Market Volume", style={'textAlign': 'center'}),
         
                dcc.Dropdown(id='my-dropdown2',
                             options=[{'label': 'Tesla', 'value': 'SBUX'},
                                      {'label': 'Starbucks', 'value': 'SBUX'},
                                      {'label': 'Apple','value': 'AAPL'}, 
                                      {'label': 'Facebook', 'value': 'FB'},
                                      {'label': 'Microsoft','value': 'MSFT'}], 
                             multi=True,value=['SBUX'],
                             style={"display": "block", "margin-left": "auto", 
                                    "margin-right": "auto", "width": "60%"}),
                dcc.Graph(id='volume')
            ], className="container"),
        ])
    ])
])



@app.callback(Output('highlow', 'figure'),
              [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown):
    dropdown = {"TSLA": "Tesla","SBUX":"Starbucks","AAPL": "Apple","FB": "Facebook","MSFT": "Microsoft",}
    trace1 = []
    trace2 = []
    for stock in selected_dropdown:
        trace1.append(
          go.Scatter(x=df[df["Symbols"] == stock]["Date"],
                     y=df[df["Symbols"] == stock]["High"],
                     mode='lines', opacity=0.7, 
                     name=f'High {dropdown[stock]}',textposition='bottom center'))
        trace2.append(
          go.Scatter(x=df[df["Symbols"] == stock]["Date"],
                     y=df[df["Symbols"] == stock]["Low"],
                     mode='lines', opacity=0.6,
                     name=f'Low {dropdown[stock]}',textposition='bottom center'))
    traces = [trace1, trace2]
    data = [val for sublist in traces for val in sublist]
    figure = {'data': data,
              'layout': go.Layout(colorway=["#5E0DAC", '#FF4F00', '#375CB1', 
                                            '#FF7400', '#FFF400', '#FF0056'],
            height=600,
            title=f"High and Low Prices for {', '.join(str(dropdown[i]) for i in selected_dropdown)} Over Time",
            xaxis={"title":"Date",
                   'rangeselector': {'buttons': list([{'count': 1, 'label': '1M', 
                                                       'step': 'month', 
                                                       'stepmode': 'backward'},
                                                      {'count': 6, 'label': '6M', 
                                                       'step': 'month', 
                                                       'stepmode': 'backward'},
                                                      {'step': 'all'}])},
                   'rangeslider': {'visible': True}, 'type': 'date'},
             yaxis={"title":"Price (USD)"})}
    return figure


@app.callback(Output('volume', 'figure'),
              [Input('my-dropdown2', 'value')])
def update_graph(selected_dropdown_value):
    dropdown = {"TSLA": "Tesla","AAPL": "Apple","FB": "Facebook","SBUX":"Starbucks","MSFT": "Microsoft",}
    trace1 = []
    for stock in selected_dropdown_value:
        trace1.append(
          go.Scatter(x=df[df["Symbols"] == stock]["Date"],
                     y=df[df["Symbols"] == stock]["Volume"],
                     mode='lines', opacity=0.7,
                     name=f'Volume {dropdown[stock]}', textposition='bottom center'))
    traces = [trace1]
    data = [val for sublist in traces for val in sublist]
    figure = {'data': data, 
              'layout': go.Layout(colorway=["#5E0DAC", '#FF4F00', '#375CB1', 
                                            '#FF7400', '#FFF400', '#FF0056'],
            height=600,
            title=f"Market Volume for {', '.join(str(dropdown[i]) for i in selected_dropdown_value)} Over Time",
            xaxis={"title":"Date",
                   'rangeselector': {'buttons': list([{'count': 1, 'label': '1M', 
                                                       'step': 'month', 
                                                       'stepmode': 'backward'},
                                                      {'count': 6, 'label': '6M',
                                                       'step': 'month', 
                                                       'stepmode': 'backward'},
                                                      {'step': 'all'}])},
                   'rangeslider': {'visible': True}, 'type': 'date'},
             yaxis={"title":"Transactions Volume"})}
    return figure

@app.callback(Output('models', 'figure'),
              [Input('my-dropdownM', 'value')])

def update_graph(mydropdownM):
    dropdown = {"Actual Close Price":"Actual Close Price","Long Short-Term Memory": "Long Short-Term Memory","Moving Average Model":"Moving Average","Tree Model": "Tree Model","Linear Regression Model": "Linear Regression",}
    trace1=[]  
    for model in mydropdownM:  
            trace1.append(
                go.Scatter(x=models[models["Model"] == model]["Date"],
                           y=models[models["Model"] == model]["Predictions"],
                           mode='lines', opacity=0.7, 
                           name=f' {dropdown[model]}',textposition='bottom center'))
    traces = [trace1]    
    data = [val for sublist in traces for val in sublist]
    figure = {'data': data,
              'layout': go.Layout(colorway=["#5E0DAC", '#FF4F00', '#375CB1', 
                                            '#FF7400', '#FFF400', '#FF0056'],
            height=400,
            title=f"ML Models: {', '.join(str(dropdown[i]) for i in mydropdownM)} ",
            xaxis={"title":"Date",
                   'rangeselector': {'buttons': list([{'count': 1, 'label': '1M', 
                                                       'step': 'month', 
                                                       'stepmode': 'backward'},
                                                      {'count': 6, 'label': '6M', 
                                                       'step': 'month', 
                                                       'stepmode': 'backward'},
                                                      {'step': 'all'}])},
                   'rangeslider': {'visible': False}, 'type': 'date'},
             yaxis={"title":"Price (USD)"})}
    return figure


if __name__=='__main__':
	app.run_server(debug=True)