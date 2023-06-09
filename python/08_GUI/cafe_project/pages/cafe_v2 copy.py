import streamlit as st
import os
import json

st.image('https://cdn.pixabay.com/photo/2016/11/29/12/54/cafe-1869656_960_720.jpg', width=500)

ROOT_PATH = '..'
st.title('카페 주문')

menus = {'아메리카노': 1500, '카페라떼': 2000, '밀크티': 3000}
for menu, price in menus.items():
    st.text(f'{menu}: {format(price,",")}원')

#  st.button 대신에 st.number_input 사용
number_input_dict = {menu: st.number_input(menu, min_value=0) for menu in menus}

st.divider()
text = ''
for menu in menus:
    text += f'{menu}: {number_input_dict[menu]} 개 '
st.text(text)

sum_val = sum([number_input_dict[menu] * menus[menu] for menu in menus])
st.subheader(f'총합: {format(sum_val, ",")}원')

st.divider()
