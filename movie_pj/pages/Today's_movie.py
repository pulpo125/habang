import streamlit as st
import pandas as pd

# 데이터 로드
df = pd.read_csv('data/movie_eda.csv')

### Header
st.title(':thinking_face:오늘의 영화는?')

st.divider()

st.markdown("""<span style='color:grey'>오늘은 또 어떤 영화를 감상해야 할지 고민인 당신!<span/><br/>
<span>지금 당신의 상황을 입력해주세요.<span/><br/>
<span>IMDB TOP 250 영화 데이터를 기반으로 추천해드립니다.:smile:<span/>""", unsafe_allow_html=True)

### Main
## 질문 1: 시간 관련
with st.sidebar:
    hour = st.radio(
        '얼마나 시간이 있나요?',
        ['1시간 정도 있어요', '영화는 2시간이 기본이죠', '하루종일 영화 보고싶어요']
    )
# st.markdown('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

if hour == '1시간 정도 있어요':
    running_time = '1h'
    # st.write(running_time)
elif hour == '영화는 2시간이 기본이죠':
    running_time = '2h'
    # st.write(running_time)
else:
    running_time = '3h'
    # st.write(running_time)

duration_contains = df['duration'].str.contains(running_time)
df_duration = df[duration_contains]

## 질문 2: 장르 관련
genre_dic = {'웃고 싶은 날':'Comedy', '울고 싶은 날':'Drama'}

with st.sidebar:
    what_day_lst = st.multiselect('오늘은 어떤 날이야?', ['웃고 싶은 날', '울고 싶은 날'])
    if what_day_lst:
        for i in what_day_lst:
           genre_contains = df['genre'].str.contains(genre_dic[i])
        #    df_genre = df[duration_contains]
        #    pd.concat()
    else:
        st.text(2)

st.text(genre_contains)
## 추천 결과
# 데이터 프레임 합치기

# 랜덤으로 하나만 추출
movie_recommendation = df_duration.sample(n=1)
idx = int(list(movie_recommendation.index)[0])

# 추천 영화 info
st.subheader("오늘의 영화는 '" + df_duration.loc[int(idx)]['title'] + "' 입니다.")
st.write('장르) ' + df_duration.loc[int(idx)]['genre'])
st.write('러닝타임) ' + df_duration.loc[int(idx)]['duration'])
st.write('감독) ' + df_duration.loc[int(idx)]['director_name'])
st.write('작가) ' + df_duration.loc[int(idx)]['writer_name'])
st.write('출연진)')
st.write(df_duration.loc[int(idx)]['cast_name'])
st.write('줄거리)')
st.write(df_duration.loc[int(idx)]['storyline'])
st.write(':link: Go to detailed information')
st.write(df_duration.loc[int(idx)]['link'])

# 만약 이미 봤다는 버튼을 누르면 데이터프레임에서 해당 컬럼 제거 후 다시 랜덤 추출
# if st.button('이미 봤어요'):
#     # 본 영화일 때
#     df_duration.drop([idx], axis=0, inplace=True)
# else:
#     # 안본 영화일 때
#     st.empty()

# 더이상 추천할 영화가 없다면 다시 상황 입력 유도


