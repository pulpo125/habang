# 1. release_date에 따른 주가 데이터 추출 함수
import pandas as pd

def create_top_album_stock(top_album_stock_tuple):
    tmp_df = pd.DataFrame(top_album_stock_tuple)
    tmp_df.columns = ['agency_name', 'date', 'stock_price']

    date_list = list(tmp_df.loc[:, 'date'].drop_duplicates())
    jyp_stock_list = list(tmp_df.loc[tmp_df['agency_name'] == 'JYP', 'stock_price'])
    sm_stock_list = list(tmp_df.loc[tmp_df['agency_name'] == 'SM', 'stock_price'])
    yg_stock_list = list(tmp_df.loc[tmp_df['agency_name'] == 'YG', 'stock_price'])

    top_album_stock_df = pd.DataFrame()
    top_album_stock_df['date'] = date_list
    top_album_stock_df['jyp_stock_price'] = jyp_stock_list
    top_album_stock_df['sm_stock_price'] = sm_stock_list
    top_album_stock_df['yg_stock_price'] = yg_stock_list
    
    return top_album_stock_df, date_list


# 2. 일간 변동률 및 변동률 누적 합계 계산 함수
# 일간 변동률 = daily rate of change (drc)
# 변동률 누적 합계 = cumulative sum rate of change (cs)
def calculate_rate_of_change(top_album_stock_df, date_list):
    rate_of_change_df = pd.DataFrame()
    rate_of_change_df['date'] = date_list
    rate_of_change_df['jyp_drc'] = ( top_album_stock_df['jyp_stock_price'] - top_album_stock_df['jyp_stock_price'].shift(1) ) / top_album_stock_df['jyp_stock_price'] * 100
    rate_of_change_df['jyp_cs'] = rate_of_change_df['jyp_drc'].cumsum()
    rate_of_change_df['sm_drc'] = ( top_album_stock_df['sm_stock_price'] - top_album_stock_df['sm_stock_price'].shift(1) ) / top_album_stock_df['sm_stock_price'] * 100
    rate_of_change_df['sm_cs'] = rate_of_change_df['sm_drc'].cumsum()
    rate_of_change_df['yg_drc'] = ( top_album_stock_df['yg_stock_price'] - top_album_stock_df['yg_stock_price'].shift(1) ) / top_album_stock_df['yg_stock_price'] * 100
    rate_of_change_df['yg_cs'] = rate_of_change_df['yg_drc'].cumsum()
    
    return rate_of_change_df