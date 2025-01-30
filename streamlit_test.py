import streamlit as st

st.title("Minha Aplicação em Streamlit")
st.write("Aplicação está rodando no localhost!")

if st.button("Clique Aqui"):
    st.success("Botão Clicado!")
