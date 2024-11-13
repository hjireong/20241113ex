import streamlit as st

st.title("GPT-4o-mini 기반 응답 앱")
api_key = st.text_input("OpenAI API Key를 입력하세요:", type="password")
user_input = st.text_input("질문을 입력하세요:")

if st.button("Submit"):
    st.write("여기에 응답이 출력됩니다.")
