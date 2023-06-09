import streamlit as st
import pymysql
import pandas as pd

# 커넥션 객체 및 커서 생성
conn = pymysql.connect(host='127.0.0.1'
                , port=3306
                , user = 'root'
                , password='root1234'
                , db = 'mydb'
                , charset='utf8'
                ) 

cur = conn.cursor()

st.image('https://cdn.pixabay.com/photo/2017/04/25/08/02/coffee-beans-2258839_960_720.jpg')
st.title('카페 주문 목록 확인 :coffee:')

# 주문 리스트 추출
cur.execute('SELECT * FROM cafe_order')
cafe_order_list = cur.fetchall()
order_id_list = [cafe_order[0] for cafe_order in cafe_order_list]

order_id = st.selectbox('주문 목록 선택', ['None'] + order_id_list)

# 주문번호에 해당하는 주문 목록 확인
if order_id == 'None':
    st.text('주문 목록을 확인해주세요.')
else:
    sql_script = f'''
    SELECT om.order_id, m.name, m.price, om.menu_num, m.price * om.menu_num
    FROM menu AS m, order_menu AS om
    WHERE m.menu_id = om.menu_id AND om.order_id = {order_id}
    '''

    cur.execute(sql_script)
    col_names = ['주문번호', '메뉴', '가격', '수량', '가격x수량']
    order_id_df = pd.DataFrame(cur.fetchall(), columns=col_names)
    st.dataframe(order_id_df)

    # 총 금액 출력    
    total = order_id_df['가격x수량'].sum()
    st.text(f'총 금액: {format(total, ",")} 원')