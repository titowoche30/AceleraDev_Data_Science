import streamlit as st
import pandas as pd

def main_basics():
    st.title('Hello World - taco paca') 
    st.header('Headerzin - h1')
    st.subheader('Subheaderzin - h2')
    st.text('Olha o meu textinho paragadun <p>')
    #st.image(imagem.png)
    #st.audio()
    #st.video()
    st.markdown('butãozin')
    botao = st.button('butaozin')
    if botao:
        st.markdown('clicou hein')
    else:
        st.markdown('nao clicou hein')

    st.markdown('checkbox')
    check = st.checkbox('Caixa de cheque')
    if check:
        st.markdown('com cheque :)')
    else:
        st.markdown('sem cheque :(')

    
    st.markdown('radio')
    opt = st.radio('Escolha uma opção', ('Opt 1','Opt 2'))
    if opt == 'Opt 1':
        st.markdown('Escolheu o 1 hein')
    if opt == 'Opt 2':
        st.markdown('Escolheu o 2 hein')

    st.markdown('Select box')
    s_box = st.selectbox('Escolha uma opção', ('Opt 1','Opt 2'))
    if s_box == 'Opt 1':
        st.markdown('Escolheu o 1 hein')
    if s_box == 'Opt 2':
        st.markdown('Escolheu o 2 hein')

    st.markdown('Multiselect')
    m_select = st.multiselect('Escolha uma opção', ('Opt 1','Opt 2','Opt 3'))
    st.markdown(f'escolheu = {m_select}')
    
    st.set_option('deprecation.showfileUploaderEncoding', False)
    st.markdown('file reader e pandinha')
    file = st.file_uploader('Manda o CSV, pvt',type='csv')
    if file is not None:
        df = pd.read_csv(file)
        st.markdown(f'Numero de linhas = {df.shape[0]}')
        st.markdown(f'Numero de colunas = {df.shape[1]}')


def main():
    st.title('Streamlit e Pandas')
    # file = st.file_uploader('Manda o CSV, pvt',type='csv')
    # if file is not None:
    #     df = pd.read_csv(file)

    slider = st.slider('Número de linhas',1,100)
    df = pd.read_csv('rain_data_com_probs.csv')
    st.markdown('Dataframe')
    st.dataframe(df.head(slider))
    st.markdown('Table')
    st.table(df.head(slider))
    st.markdown('Write')
    st.write(df.columns,df.describe())







if __name__ == "__main__":
    #main_basics()
    main()
