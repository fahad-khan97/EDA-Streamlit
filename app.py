import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
import sweetviz as sv;
from streamlit_pandas_profiling import st_profile_report
import streamlit.components.v1 as components
import codecs

home = '''
    # EDA using Pandas and Sweetviz

'''

def display_sweetviz_html(report, height=500, width=800):
    report_file = codecs.open(report, 'r')
    html = report_file.read()
    components.html(html, height=height, width=width, scrolling=True)

def render_home():
    st.markdown(home)
    st.image('img/home.png', height=500, width=500)

def render_pandas_profiler():
    st.header('EDA using Pandas Profile')
    input_file = st.file_uploader('Upload CSV', type=['csv'])
    if input_file:
        df = pd.read_csv(input_file)
        st.dataframe(df.head())
        profile = ProfileReport(df)
        st_profile_report(profile)

def render_sweetviz_profiler():
    st.subheader('EDA using Sweetviz')
    input_file = st.file_uploader('Upload CSV', type=['csv'])
    if input_file:
        df = pd.read_csv(input_file)
        st.dataframe(df.head())
        if st.button('Generate Sweetviz Report'):
            report = sv.analyze(df)
            report.show_html()
            display_sweetviz_html('SWEETVIZ_REPORT.html')

def main():
    menu = ['Home', 'EDA - Pandas', 'EDA - Sweetviz']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Home':
        render_home()
    
    elif choice == 'EDA - Pandas':
        render_pandas_profiler()
    
    elif choice == 'EDA - Sweetviz':
        render_sweetviz_profiler()

if __name__ == '__main__':
    main()
