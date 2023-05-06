import datetime

def extract_weekday(date_text):
    '''
    문자열로 날짜를 입력 받고, 요일을 반환하는 함수
    yyyy-mm-dd, yyyy/mm/dd, dd-mm-yyyy, dd/mm/yyyy 형태 호환 가능
    '''

    split_char = '/' if '/' in date_text else '-'
    split_list = list(map(int, date_text.split(split_char)))

    if len(str(split_list[0])) == 4:
        yyyy, mm, dd = split_list
    else:
        dd, mm, yyyy = split_list

    datetime_obj = datetime.date(yyyy, mm, dd)
    day = datetime_obj.weekday()

    return ['월', '화', '수', '목', '금', '토', '일'][day]

if __name__ == '__main__':
    print(extract_weekday('2023/05/04'))
    print(extract_weekday('2023-05-05'))