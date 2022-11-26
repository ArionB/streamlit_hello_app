import streamlit as st 

st.title('hello streamlit app')
st.header('This is added after deployment')
from datetime import datetime, time
date_now = datetime.now
st.write(time_now)
