'''
Author:     Damian Kwasny
Date:       19.03.2018r
Topic:      Fundamentals of browser_based data visualization UI with Dash framework

In order to make this thing work one needs to install the below dependencies
In this script we are generating a simple web-based UI that allows the user to input a cerrtain string
and then a graph of stocks of the company assigned to that name is generated. It utilizes the Dash framework
and uses pandas_datareader to get some stock data.

It is done for pure practice
'''

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import pandas_datareader.data as web
import datetime


app = dash.Dash()

# dcc.Input creates a field where You can enter data with id 'input'
# html.Div creates field where output is shown with id 'output'
'''
app.layout = html.Div(children=[
    dcc.Input(id='input', value='Enter sth', type='text'),
    html.Div(id='output')
])

#
@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_value(input_data):
    return "Input: {}".format(input_data)
'''
# Now, let's grab some data and graph it in dash. The folowing 3 lines do this
'''
start = datetime.datetime(2015, 1, 1)
end = datetime.datetime.now()
df = web.DataReader('F', 'iex', start, end)
print(df.head())
'''
# Stuffing a graph into a UI (staticly, cant change anything in the graph this way)
'''app.layout = html.Div(children=[
    html.H1('Dash Tutorial'),
    dcc.Graph(id='example',
              figure={
                  'data': [
                      {'x':df.index, 'y': df.close, 'type':'line', 'name':'stock'}
                  ],
                  'layout': {
                      'title': 'Stock'
                   }
              })
])'''

# Now, lets try to combine above two things and create graph dynamically when user want to
# First, the layout. It will consist of an input field with id input, and output field with id 'output-graph'
app.layout = html.Div(children=[

    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output-graph')
])

# Next, tell what to do on submiting the data.
# What the code below does is that it listens to the component with id 'input' for changes in the value property
# When the change apperas, it sends the input to the function, in this case 'update_graph' and finally it
# modifies the 'Output' component which in this case is 'output-graph'
@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
    )
def update_graph(input_data):
    # parameters for the graph
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime.now()
    df = web.DataReader(input_data, 'iex', start, end)  # input_data is what we typed

    # Now, let us create the graph! We return it and it will be a child of html.div wth id output graph
    return dcc.Graph(id='example',
              figure={
                  'data': [
                      {'x': df.index, 'y': df.close, 'type': 'line', 'name': 'stock'}
                  ],
                  'layout': {
                      'title': 'Stock'
                  }
              })


if __name__ == '__main__':
    app.run_server(debug=True)