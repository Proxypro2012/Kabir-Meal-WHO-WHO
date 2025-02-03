import streamlit as st
import streamlit_extras
import streamlit_extras.let_it_rain
from streamlit_extras.card import card
import streamlit_extras.theme
import streamlit_shadcn_ui as ui
import streamlit_antd_components as sac


r1col1, r1col2, r1col3 = st.columns([1, 2, 1])
r2col1, r2col2, r2col3 = st.columns([1, 2, 1])


with r1col2:
  st.title("The Microwave Coffee")
  st.image("Coffee.JPG", caption="Price: $6.99 for pack of two.")
  
with r2col1:
  st.header("FAQ")
  st.text("Where can I buy it?")
  st.info("At this really cool fast-food place known as the Starbucks, famous for its Coffee and other food elements")

streamlit_extras.let_it_rain.rain('•', 20, falling_speed=5, animation_length="infinite")


