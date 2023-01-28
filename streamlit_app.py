import streamlit

streamlit.title('This is the first streamlit code')
streamlit.header('Jelovnik')
streamlit.text('🥣 Juha')
streamlit.text('🐔 🍞 Glavno jelo')
streamlit.text('🥗 Prilog')
streamlit.text('🥑 Desert')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
