import dash
from dash_html_components.Meta import Meta
import dash_table
from dash.dependencies import Input, Output
from dash_bootstrap_components._components.Select import Select
import dash_core_components as dcc
from dash_core_components.RadioItems import RadioItems
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

def init_dasboard(server):
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/',
        
        external_stylesheets=[dbc.themes.BOOTSTRAP]
    )

    df = pd.DataFrame({
        'month': ['Enero', 'Febrero', 'Marzo'],
        'day': [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
        ],
        'users': [
            [325, 324, 405, 400, 424, 404, 417, 432, 419, 394, 410, 426, 413, 419, 404, 408, 401, 377, 368, 361, 234, 356, 345, 
                354, 345, 345, 378, 344, 342, 412, 453], 
            [432, 419, 394, 410, 426, 413, 419, 404, 408, 401, 377, 368, 361, 234, 356, 345, 354, 345, 345, 378, 344, 342, 412, 
                453, 324, 405, 400, 424],
            [408, 401, 377, 368, 361, 234, 356, 345, 354, 345, 345, 378, 344, 342, 412, 453, 324, 405, 400, 424, 432, 419, 394, 
                410, 426, 413, 419, 404, 408, 401, 377]
        ]
    })

    df2 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

    dash_app.layout = html.Div(children=[
        html.Meta(httpEquiv='X-UA-Compatible', content='IE=edge'),
        html.Meta(name='viewport', content='width=device-width, initial-scale=1, shrink-to-fit=no, maximum-scale=1, minimum-scale=1, user-scalable=0'),
        html.Div(style={'border-bottom': '2px solid black'}, className='d-flex flex-column justify-content-between', children=[
            dbc.Container(className="d-flex justify-content-around", children=[
                dbc.RadioItems(id='option-group', className='mt-5 mr-5',
                    value='mensual', options=[
                        {'label': 'Mensual', 'value': 'mensual', 'class': 'pt-5'},
                        {'label': 'Diario', 'value': 'diario'}
                    ],
                ),

                dbc.Select(id='option-month', className='mt-5', 
                    value=0, options=[
                        {'label': df['month'][i], 'value': i} for i in range(len(df['month']))
                    ]
                ),
            ]),

            dcc.Graph(id='graph-1', config={'displayModeBar': False}),

            dcc.Graph(id='graph-2'), 
        ]),

        #html.Div(style={'height': '100vh', 'border-bottom': '2px solid black'}, className='p-4 d-flex flex-column justify-content-between', children=[
        #    dash_table.DataTable(
        #        id='datatable',
        #        columns=[{'name': i, 'id': i, 'selectable': True} for i in df2.columns],
        #        data=df2.to_dict('records'),
        #        filter_action='native',
        #        sort_action='native',
        #        sort_mode='multi',
        #        row_selectable='multi',
        #        selected_columns=[],
        #        selected_rows=[],
        #        page_action='native',
        #        page_current=0,
        #        page_size=20
        #    ),
        #    html.Div(id='datatable-graph', style={'overflowY': 'scroll'})
        #]),
    ])

    #@dash_app.callback(
    #    Output('datatable', 'style_data_conditional'),
    #    Input('datatable', 'selected_columns')
    #)
    #def update_styles(selected_columns):
    #    return [{
    #        'if': {'column_id': i},
    #        'background_color': '#D2F3FF',
    #    } for i in selected_columns]


    #@dash_app.callback(
    #    Output('datatable-graph', 'children'),
    #    Input('datatable', 'derived_virtual_data'),
    #    Input('datatable', 'derived_virtual_selected_rows')
    #)
    #def update_graphs(rows, derived_virtual_selected_rows):
    #    if derived_virtual_selected_rows is None:
    #        derived_virtual_selected_rows = []

    #    dff = df2 if rows is None else pd.DataFrame(rows)
    #    colors = ['#7FDBFF' if i in derived_virtual_selected_rows else '#0074D9'
    #                for i in range(len(dff))]

    #    return [
    #        dcc.Graph(
    #            id=column,
    #            figure={
    #                'data': [
    #                    {
    #                        'x': dff['country'],
    #                        'y': dff[column],
    #                        'type': 'bar',
    #                        'marker': {'color': colors}
    #                    }
    #                ],
    #                'layout': {
    #                    'xaxis': {'automargin': True},
    #                    'yaxis': {
    #                        'automargin': True,
    #                        'title': {'text': column}
    #                    },
    #                    'height': 700,
    #                    'margin': {'t': 10, 'l': 10, 'r': 10}
    #                }
    #            }
    #        ) for column in ['pop', 'lifeExp', 'gdpPercap'] if column in dff
    #    ]


    @dash_app.callback(
        Output('graph-1', 'figure'),
        Output('graph-2', 'figure'),
        Input('option-month', 'value'),
        Input('option-group', 'value')
    )
    def change_month(pos, group):
        pos = int(pos)
        fig1 = None

        if group == 'mensual':
            if pos == 0:
                fig1 = go.Figure(go.Indicator(
                    mode = "number+delta",
                    value = sum(df['users'][pos]), 
                    delta = {'reference': sum(df['users'][pos]), 'valueformat': '.0f'},
                    title = {"text": "Usuarios mensuales en {}".format(df['month'][pos])},
                    align = 'center',
                    domain = {'y': [0, 1], 'x': [0, 1]}
                ))
            else:
                fig1 = go.Figure(go.Indicator(
                    mode = "number+delta",
                    value = sum(df['users'][pos]), 
                    delta = {'reference': sum(df['users'][pos-1]), 'valueformat': '.0f'},
                    title = {"text": "Usuarios mensuales en {}".format(df['month'][pos])},
                    align = 'center',
                    domain = {'y': [0, 1], 'x': [0, 1]}
                ))
        else:
            fig1 = go.Figure(go.Indicator(
                mode = 'number+delta',
                value = df['users'][pos][len(df['users'][pos])-1],
                delta = {'reference': df['users'][pos][len(df['users'][pos])-2], 'valueformat': '.0f'},
                title = {'text': 'Usuarios el último día de {}'.format(df['month'][pos])},
                align = 'center',
                domain = {'y': [0, 1], 'x': [0, 1]}
            ))     

        fig2 = go.Figure(go.Scatter(
            y = df['users'][pos],
            x = df['day'][pos],
            fill = 'tonexty'
        ))   

        fig2.update_layout(plot_bgcolor='white')

        return fig1, fig2

    