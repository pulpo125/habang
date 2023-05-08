import streamlit as st
import pandas as pd

# 데이터 로드
df = pd.read_csv('../data/movie_added.csv')

# title
st.image('https://static.amazon.jobs/teams/53/images/IMDb_Header_Page.jpg?1501027252')
st.title('IMDB Top 250 Movies :movie_camera:')

st.divider()

#1: 컬럼별 Top 5
st.header('컬럼별 Top 5')
group_by_option = st.selectbox('Select the column : ', ['None'] + ['year'] + ['genre'] + ['director_name'])

cols = 'None'
if group_by_option == 'None':
    tmp_df = df[['rank', 'title', 'imbd_votes', 'imbd_rating']]
    st.dataframe(tmp_df, width=700)
else:
    tmp_df = df[group_by_option].value_counts()[:5].reset_index()
    tmp_df = pd.DataFrame(tmp_df).rename(columns={group_by_option:'count', 'index':group_by_option})
    tmp_df.index = tmp_df.index + 1
    st.bar_chart(tmp_df, x = group_by_option, y = 'count')

    st.divider()

    group_list = tmp_df[group_by_option].to_list()
    cols = st.selectbox('Select the data: ', ['None'] + list(group_list))

#2: 1에서 선택한 데이터 보여주기
if cols == 'None':
    st.empty()

else:
    tmp_df = df[df[group_by_option].isin([cols])][['rank', 'title', 'imbd_votes', 'imbd_rating']]
    st.dataframe(tmp_df, width=700)


st.divider()

idx = st.text_input('Enter the Index')
if idx:
    st.subheader('Info.')
    st.write('Title) ' + df.loc[int(idx)]['title'])
    st.write('Genre) ' + df.loc[int(idx)]['genre'])
    st.write('Running time) ' + df.loc[int(idx)]['duration'])
    st.write('Director) ' + df.loc[int(idx)]['director_name'])
    st.write('Writer) ' + df.loc[int(idx)]['writer_name'])
    st.write('Casts)')
    st.write(df.loc[int(idx)]['cast_name'])
    st.write('Storyline)')
    st.write(df.loc[int(idx)]['storyline'])
    st.write(':link: Go to detailed information')
    st.write(df.loc[int(idx)]['link'])

else:
    st.empty()