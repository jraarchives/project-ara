import streamlit as st
st.title(":blue[Project LPK 2025]")
st.header(":orange[Penentuan bilangan ganjil atau genap]")
number = st.number_input("Insert a number",min_value=0, max_value=1000")
if number%2==1:
    st.write("Bilangan", number,"termasuk bilangan")
else:
    st.write("Bilangan", number,"termasuk bilangan")
