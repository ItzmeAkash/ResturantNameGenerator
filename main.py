import streamlit as st
import langchain_demo


st.title("Restaurant Name Generator")


cusisne = st.sidebar.selectbox("Pick a Cuisine",("India","Italian","Maxican","Arabic","American"))

def generate_restaurant_name_and_items(cuisine):
    return {
        'restaurant_name': 'Curry Delight',
        'menu_item': 'samosa, panner tikka'
    }

if cusisne:
    response = langchain_demo.generate_restaurant_name_and_items(cusisne)
    
    st.header(response['restaurant_name'])
    menu_items = response['menu_item'].split(",")
    st.write('**Menu Items**')
    for items in menu_items:
        st.write("-", items)