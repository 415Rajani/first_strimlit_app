
import pandas
import streamlit
import requests
import snowflake.connector


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

fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit Advice')
fruit_choice=streamlit.text_input('what fruit like  information about?','Kiwi')
streamlit.write('user_entered',fruit_choice)
                                  

fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)



fruityvice_normalize=pandas.json_normalize(fruityvice_response.json())

streamlit.dataframe(fruityvice_normalize)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
