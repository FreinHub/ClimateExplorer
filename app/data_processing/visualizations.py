import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import pandas as pd
from datetime import datetime

def _prepare_dataframe(data):
    """Универсальный конвертер данных в DataFrame"""
    df_data = []
    for item in data:
        if isinstance(item, dict):
            row = {
                'date': item['date'],
                'temperature': item['temperature'],
                'precipitation': item['precipitation'],
                'humidity': item.get('humidity'),
                'country': item.get('country', ''),
                'city': item.get('city', '')
            }
        else:
            row = {
                'date': item.date,
                'temperature': item.temperature,
                'precipitation': item.precipitation,
                'humidity': getattr(item, 'humidity', None),
                'country': getattr(item, 'country', ''),
                'city': getattr(item, 'city', '')
            }
        df_data.append(row)
    return pd.DataFrame(df_data)

def generate_visualizations(data, selected_country):
    """Генерация основных графиков"""
    if not data:
        return {}
    
    df = _prepare_dataframe(data)
    plots = {}
    
    # Time Series Plot
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(
        x=df['date'], 
        y=df['temperature'],
        name='Temperature (°C)',
        line=dict(color='firebrick', width=2)
    ))
    fig1.add_trace(go.Scatter(
        x=df['date'], 
        y=df['precipitation'],
        name='Precipitation (mm)',
        yaxis='y2',
        line=dict(color='royalblue', width=2)
    ))
    
    fig1.update_layout(
        title=f'Temperature and Precipitation Trends in {selected_country}',
        yaxis=dict(title='Temperature (°C)'),
        yaxis2=dict(
            title='Precipitation (mm)',
            overlaying='y',
            side='right'
        ),
        hovermode='x unified'
    )
    plots['time_series'] = fig1.to_html(full_html=False)
    
    # Temperature Histogram (Plotly вместо Matplotlib)
    fig_hist = px.histogram(
        df, 
        x='temperature',
        nbins=15,
        title='Temperature Distribution',
        labels={'temperature': 'Temperature (°C)'}
    )
    plots['temp_hist'] = fig_hist.to_html(full_html=False)
    
    # Pie Chart (только если есть данные по городам)
    if 'city' in df.columns and len(df['city'].unique()) > 1:
        avg_by_city = df.groupby('city').mean().reset_index()
        fig2 = px.pie(
            avg_by_city,
            values='temperature',
            names='city',
            title='Average Temperature Distribution by City'
        )
        plots['pie_chart'] = fig2.to_html(full_html=False)
    
    # Scatter Plot
    if 'humidity' in df.columns:
        fig3 = px.scatter(
            df,
            x='temperature',
            y='humidity',
            trendline='ols',
            title='Temperature vs Humidity'
        )
        plots['scatter_plot'] = fig3.to_html(full_html=False)
    
    return plots

def generate_additional_visualizations(data):
    """Генерация дополнительных графиков"""
    if not data:
        return {}
        
    df = _prepare_dataframe(data)
    additional_plots = {}
    
    # Monthly Heatmap
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    
    if len(df) > 0:
        monthly_avg = df.groupby(['year', 'month'])['temperature'].mean().unstack()
        fig4 = go.Figure(data=go.Heatmap(
            z=monthly_avg.values,
            x=monthly_avg.columns,
            y=monthly_avg.index,
            colorscale='Viridis'
        ))
        fig4.update_layout(
            title='Monthly Temperature Averages (Heatmap)',
            xaxis_title='Month',
            yaxis_title='Year'
        )
        additional_plots['heatmap'] = fig4.to_html(full_html=False)
    
    # Box Plot
    if 'country' in df.columns and len(df['country'].unique()) > 1:
        fig5 = px.box(
            df,
            x='country',
            y='temperature',
            color='country',
            title='Temperature Distribution by Country'
        )
        additional_plots['box_plot'] = fig5.to_html(full_html=False)
    
    # Animated Scatter (требуется несколько лет данных)
    if 'year' in df.columns and len(df['year'].unique()) > 1:
        fig6 = px.scatter(
            df,
            x='temperature',
            y='precipitation',
            animation_frame='year',
            size='humidity',
            color='country',
            hover_name='city',
            range_x=[df['temperature'].min()-5, df['temperature'].max()+5],
            range_y=[0, df['precipitation'].max()+10],
            title='Temperature vs Precipitation Over Time'
        )
        additional_plots['animated_scatter'] = fig6.to_html(full_html=False)
    
    return additional_plots