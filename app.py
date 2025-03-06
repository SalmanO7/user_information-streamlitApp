import streamlit as st

st.title('Welcome to my first Streamlit app')
st.write('This is a simple app to show users information')

st.header('Input some data')
name = st.text_input('Enter your name')
age = st.number_input('Enter your age', min_value=0, step=1)

if st.button("Submit"):
    if not name or not age:
        st.warning('Please input some data')        
    else:
        st.success(f'Hello, I am {name} and I am {age} years old 🎉')
