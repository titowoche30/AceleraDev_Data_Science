import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import base64
from os import listdir
from os.path import isfile, join

def plot_locations_maxtemp(temp_rain_data,year):
    locations = temp_rain_data['location'].unique()
    fig = go.Figure()
    cond1 = temp_rain_data['date'].dt.year==year
    
    for local in locations:
        cond2 = temp_rain_data['location'] == local
        sub = temp_rain_data[(cond1) & (cond2)]
        fig.add_trace(go.Scattergl(x=sub['date'], y=sub['maxtemp'],name=local))

    fig.update_layout(height=600, width=800,title_text='Temperaturas Máximas no ano de {}'.format(year),xaxis_title="Datas",
        yaxis_title="Temperatura Máxima (celsius)",xaxis_rangeslider_visible=True)
    
    return fig


def main():
    st.title('Gráficos dos Dados Meteorológicos da Austrália')
    st.image('media/Australia.jpg',width=300)
    rain_data = pd.read_csv('./data/rain_data_completo.csv',parse_dates=['date'])
    st.header('Dados')
    st.dataframe(rain_data.head())

    st.subheader('Gráficos')
    temp_rain_data = rain_data.copy()
    years = sorted(temp_rain_data['date'].dt.year.unique())
    
    for year in years:
        fig = plot_locations_maxtemp(temp_rain_data,year)
        st.write(fig)

    fig = go.Figure()
    for year in years[2:-1]:
        cond1 = temp_rain_data['date'].dt.year == year
        sub = temp_rain_data[cond1]

        fig.add_trace(go.Violin(y=sub['maxtemp'],name=str(year),box_visible=True,meanline_visible=True))

    fig.update_layout(title='Temperaturas Máximas entre 2009 e 2016',xaxis_title="Ano",yaxis_title="Temperatura Máxima (celsius)")
    st.write(fig)

    fig = go.Figure()
    for year in years[2:-1]:
        cond1 = temp_rain_data['date'].dt.year == year
        sub = temp_rain_data[cond1]
        
        fig.add_trace(go.Violin(y=sub['mintemp'],name=str(year),box_visible=True,meanline_visible=True))

    fig.update_layout(title='Temperaturas Mínimas entre 2009 e 2016',xaxis_title="Ano",yaxis_title="Temperatura Mínima (celsius)")
    st.write(fig)

    locations = temp_rain_data['location'].unique()
    rain_per_local_yes,rain_per_local_no = [],[]

    rain_data_yes = temp_rain_data[temp_rain_data['raintomorrow'] == 'Yes']
    rain_data_no = temp_rain_data[temp_rain_data['raintomorrow'] == 'No']

    for local in locations:
        cond1 = rain_data_yes['location'] == local
        cond2 = rain_data_no['location'] == local
        cond3 = rain_data_yes[cond1]['rainfall'] > 1
        cond4 = rain_data_no[cond2]['rainfall'] > 1
        
        rain_per_local_yes.append(np.nanmean(rain_data_yes[(cond1) & (cond3)]['rainfall'].values))
        rain_per_local_no.append(np.nanmean(rain_data_no[(cond2) & (cond4)]['rainfall'].values))

    fig = go.Figure()
    fig.add_trace(go.Bar(name='Rain Tomorrow',x=locations,y=rain_per_local_yes))
    fig.add_trace(go.Bar(name='Not Rain Tomorrow',x=locations,y=rain_per_local_no))


    fig.update_layout(barmode='group',height=1000, width=1000,title_text='Distribuição de Rain Tomorrow nos locais',xaxis_title="Local",
            yaxis_title="Quantidade média de chuva(mm)",xaxis_rangeslider_visible=True)
    st.write(fig)

    st.subheader('Correlações')
    rain_data['raintoday']=rain_data['raintoday'].map(dict(Yes=1, No=0))
    rain_data['raintomorrow']=rain_data['raintomorrow'].map(dict(Yes=1, No=0))

    corr=rain_data.corr()
    plt.figure(figsize=(16,16))
    sns.heatmap(corr,cmap='PuBu',annot=True,linewidths=.5,square=True)
    st.pyplot()


if __name__ == "__main__":
    main()