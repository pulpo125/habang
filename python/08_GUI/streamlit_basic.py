import streamlit as st
# 터미널: streamlit run streamlit_basic.py

st.title('제목')


st.divider()

# 라디오 버튼
radio_val = st.radio('좋아하는 과일은?', ['사과', '딸기', '망고'])

# 버튼 
btn_state1 = st.button('제출')
if btn_state1: # 버튼 상태가 True 이면 (버튼을 누르기 전은 False, 버튼을 누르면 True)
    st.text(radio_val)

st.divider()

# 체크박스
check_state = st.checkbox('확인')
st.text(check_state) # 체크 전은 False, 체크 후는 True

# 다중 선택
multiselect_state = st.multiselect('여러 항목 선택 가능: ', ['사과', '딸기', '망고'])
if multiselect_state:
    st.text(multiselect_state)

# https://docs.streamlit.io/