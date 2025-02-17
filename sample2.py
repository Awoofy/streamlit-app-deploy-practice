import streamlit as st

st.title("へんなアプリ")
st.write("モード①:文字数カウント")
st.write("入力フォームに文字を入力すると、文字数をカウントします。")
st.write("モード②:BMI計算")
st.write("入力フォームに身長と体重を入力すると、BMIを計算します。")

select_mode = st.radio("モードを選択してください。", ["文字数カウント", "BMI計算"])

st.divider()

if select_mode == "文字数カウント":
    imput_message = st.text_input(label="文字数カウントの対象となる文章を入力してください。")
    text_count = len(imput_message)
else:
    height = st.number_input("身長を入力してください。", min_value=0.0, max_value=300.0, value=0.0, step=0.1)
    weight = st.number_input("体重を入力してください。", min_value=0.0, max_value=500.0, value=0.0, step=0.1)
    bmi = weight / (height / 100) ** 2

if st.button("実行"):
    if select_mode == "文字数カウント":
        if imput_message:
            st.write(f"入力された文章は、{text_count}文字です。")
        else:
            st.error("何も入力されていません。")
    else:
        if height and weight:
            st.write(f"あなたのBMIは、{bmi:.2f}です。")