import streamlit as st
import pandas as pd

st.markdown(
    """
<style>
span[data-baseweb="tag"] {
  background-color: blue !important;
}
</style>
""",
    unsafe_allow_html=True,
)


st.title('Seoul Bike :bike:')

df = pd.read_csv('../0_data/SeoulBikeData_added.csv')

columns = df.columns
group_by_option = st.selectbox('Group By: ', ['None'] + list(columns))
cols = st.multiselect('컬럼 선택:', list(columns))

if group_by_option == 'None':
    if cols:
        tmp_df = df[cols] # 특정 컬럼 선택 cols = ['col1', 'col2']
    else:
        tmp_df = df

else: #groubby를 할 컬럼이 선택된 경우
    if cols:
        tmp_df = df.groupby(group_by_option).mean()[cols]
    else:
        tmp_df = df.groupby(group_by_option).mean()


df_tab, plot_tab = st.tabs(['테이블', '시각화'])
with df_tab:
    st.dataframe(tmp_df)

with plot_tab:
    st.line_chart(tmp_df)