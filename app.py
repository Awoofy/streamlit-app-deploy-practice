import streamlit as st

st.title("アプリ")

input_message = st.text_input(label="文字数カウントの対象となる文章を入力してください。")
text_count = len(input_message)

if st.button("文字数カウント"):
    st.write(f"入力された文章は、{text_count}文字です。")