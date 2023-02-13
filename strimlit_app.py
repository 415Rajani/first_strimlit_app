import pandas
import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('breakfast Menu')
streamlit.text('🥣omega3 & blueberry oatmeal')
streamlit.text('🥗 Kale,Spinach Rocket smoothie')
streamlit.text('🐔Hard-boiled Free-range Egg')
streamlit.text('🥑🍞Avacado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
