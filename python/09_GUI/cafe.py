import streamlit as st
import json

st.image('https://cdn.pixabay.com/photo/2017/04/25/08/02/coffee-beans-2258839_960_720.jpg', width=567)
# st.markdown("<img src='https://cdn.pixabay.com/photo/2017/04/25/08/02/coffee-beans-2258839_960_720.jpg' style='text-align: center; width: 500px'></img>", unsafe_allow_html=True)
# st.markdown("<h1 style='text-align: center; color: grey'>Cafe</h1>", unsafe_allow_html=True)

st.title('카페 주문 :sunglasses:')

# 메뉴판 생성
menus = {'아메리카노': 1500, '카페라떼': 2000, '밀크티': 3000}
for menu, price in menus.items():
    st.text(f'{menu}: {format(price, ",")}원')

# 메뉴 선택 버튼
with st.container():
    cols = st.columns(len(menus))
    buttons = {}
    for i, menu in enumerate(menus):
        buttons[menu] = cols[i].button(menu)

st.json(buttons)

# 음료별 선택 개수 저장
# cafe_dict = {'아메리카노': 0, '카페라떼': 0, '밀크티': 0}
# with open('cafe_dict.json', 'w') as f:
#     json.dump(cafe_dict, f)

with open('cafe_dict.json', 'r') as f:
    cafe_dict = json.load(f)

for button_name in buttons:
    if buttons[button_name]:
        cafe_dict[button_name] += 1
        with open('cafe_dict.json', 'w') as f:
            json.dump(cafe_dict, f)
        
st.divider()

text = ''
for menu in menus:
    text += f'{menu}: {cafe_dict[menu]}개 '
st.text(text)

# 총합 구하기

# menus[menu]: 가격
# cafe_dict[menu]: 개수

sum_val = 0
for menu in menus:
    sum_val += menus[menu] * cafe_dict[menu]

st.subheader(f'총합: {format(sum_val, ",")}원')

st.divider()
reset = st.button('초기화')
if reset:
    cafe_dict = {'아메리카노':0, '카페라떼':0, '밀크티':0}
    with open('cafe_dict.json', 'w') as f:
        json.dump(cafe_dict, f)


