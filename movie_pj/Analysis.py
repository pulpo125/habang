import streamlit as st
import pandas as pd

# 데이터 로드
df = pd.read_csv('data/movie_eda.csv')

### Sidebar
with st.sidebar:
    st.subheader("How to use")
    st.markdown("""<span style='color:grey'>IMDB Top 250 영화 데이터를 이용하여<span/><br/>
    <span>년도별, 장르별, 감독별로 순위에<span/><br/>
    <span>가장 많이 랭킹된 Top 5를 분석합니다.:smile:<span/><br/>
    <span>컬럼을 선택하고 자세히 보고 싶은 데이터를 선택한 후<span/><br/>
    <span>상세정보가 궁금한 영화의 순위를 검색창에 입력해주세요.<span/><br/>
    <hr style='margin: 0px; border-bottom: 3px dashed rgba(49, 51, 63, 0.2);'>""", unsafe_allow_html=True)

with st.sidebar:
    group_by_option = st.selectbox('컬럼을 선택하세요: ', ['None'] + ['year'] + ['genre'] + ['director_name'])

# title
st.title(':movie_camera: IMDB Top 250 Movies')

#1: 컬럼별 Top 5
cols = 'None'
if group_by_option == 'None':
    tmp_df = df[['title', 'imbd_votes', 'imbd_rating']]
    tmp_df.index=tmp_df.index+1
    tmp_df.index.name = 'rank'
    st.dataframe(tmp_df, width=700)
else:
    st.subheader(f'{group_by_option}별 가장 많이 랭킹된 Top 5')
    tmp_df = df[group_by_option].value_counts()[:5].reset_index()
    tmp_df = pd.DataFrame(tmp_df).rename(columns={group_by_option:'count', 'index':group_by_option})
    st.bar_chart(tmp_df, x = group_by_option, y = 'count')

    group_list = tmp_df[group_by_option].to_list()
    with st.sidebar:
        cols = st.selectbox('데이터를 선택해주세요: ', ['None'] + list(group_list))

#2: 1에서 선택한 데이터 보여주기
if cols == 'None':
    st.empty()

else:
    st.subheader(f'{cols}의 데이터셋')
    tmp_df = df[df[group_by_option].isin([cols])][['title', 'imbd_votes', 'imbd_rating']]
    tmp_df.index = tmp_df.index+1
    tmp_df.index.name = 'rank'
    st.dataframe(tmp_df, width=700)


with st.sidebar:
    st.markdown("<hr style='margin: 0px; border-bottom: 3px dashed rgba(49, 51, 63, 0.2);'>", unsafe_allow_html=True)
    idx = st.text_input('검색하고 싶은 순위(rank)를 입력해주세요.')
    if idx:
        st.write(df.loc[int(idx)]['link'])

    else:
        st.empty()