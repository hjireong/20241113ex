import streamlit as st
import openai

# 제목 설정
st.title("GPT-4o-mini 기반 응답 앱")

# OpenAI API Key 입력 받기
api_key = st.text_input("OpenAI API Key를 입력하세요:", type="password")
if api_key:
    openai.api_key = api_key

# 사용자 입력 받기
user_input = st.text_input("질문을 입력하세요:")

# 버튼 클릭 시 응답 출력
if st.button("Submit"):
    if user_input:
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",  # 예시 모델
                prompt=user_input,
                max_tokens=150
            )
            st.write("응답:", response.choices[0].text.strip())
        except Exception as e:
            st.error(f"에러가 발생했습니다: {e}")
    else:
        st.warning("질문을 입력하세요.")
