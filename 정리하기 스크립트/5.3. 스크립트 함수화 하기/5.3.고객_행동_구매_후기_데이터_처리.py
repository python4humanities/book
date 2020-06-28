import pandas as pd

def cdj_analysis(src_file_path, rst_file_path):
    """
    고객 행동 데이터 처리 모듈
    :param src_file_path: 고객 행동 원본 데이터 경로
    :param rst_file_path: 처리 결과를 저장할 경로
    """
    df_data = pd.read_excel(src_file_path, sheet_name='Sheet1', index_col='model')
    df_cdj = df_data.loc[:, ['view', 'click', 'keep', 'sales', 'review_score']]
    df_price = df_data.loc[:, ['price']]
    df_price = df_price.sort_values(by='price', ascending=False)

    for element in df_cdj.columns:
        df_cdj[f'rank_{element}'] = df_cdj[element].rank(ascending=False, method='min')
        df_cdj[f'rank_{element}'] = pd.to_numeric(df_cdj[f'rank_{element}'], downcast='integer')

    writer = pd.ExcelWriter(rst_file_path, engine='xlsxwriter')  # 엑셀 파일 객체 생성
    df_cdj.to_excel(writer, sheet_name='cdj')                 # cdj 시트에 df_cdj 전달
    df_price.to_excel(writer, sheet_name='price')         # price 시트에 df_price 전달

    cdj_chart = writer.book.add_chart({'type': 'line'})     # cdj 선형 차트 생성
    cdj_cat = ['cdj', 0, 6, 0, 10]
    cdj_val_a = ['cdj', 1, 6, 1, 10]
    cdj_val_b = ['cdj', 2, 6, 2, 10]
    cdj_chart.add_series({'name': 'A', 'categories': cdj_cat, 'values': cdj_val_a})
    cdj_chart.add_series({'name': 'B', 'categories': cdj_cat, 'values': cdj_val_b})
    cdj_chart.set_y_axis({'major_unit': 1, 'minor_unit': None, 'reverse': True})
    cdj_chart.set_title({'name': '제품 A, B의 고객 구매 경로'})
    writer.sheets['cdj'].insert_chart(11, 0, cdj_chart)

    price_chart = writer.book.add_chart({'type': 'column'})    # price 세로막대형 차트 생성
    price_cat = ['price', 1, 0, 10, 0]
    price_val = ['price', 1, 1, 10, 1]
    price_chart.add_series({'name': 'Price', 'categories': price_cat, 'values': price_val})
    price_chart.set_title({'name': '제품 별 가격 포지션'})
    writer.sheets['price'].insert_chart(0, 2, price_chart)

    writer.save()

def review_analysis(src_file_path, rst_file_path, font_file_path='./font/SeoulNamsanM.ttf'):
    """
    구매 후기 데이터 처리 모듈
    :param src_file_path: 구매 후기 원본 데이터 경로
    :param rst_file_path: 처리 결과를 저장할 경로
    :param font_file_path: 글꼴 경로
    """

    from pandas import DataFrame as df
    import re
    from statistics import mean
    from konlpy.tag import Okt
    from collections import Counter
    from wordcloud import WordCloud as WC

    f = open(src_file_path, 'rt', encoding='utf-8', errors='ignore')
    rev = f.read()
    f.close()

    ptrn_html_code = re.compile(r'&[a-zA-Z]+?;')  # HTML 코드 패턴
    ptrn_html_tag = re.compile(r'</?[a-zA-Z]+?>')  # HTML 태그 패턴
    ptrn_all_clean = re.compile(r'[^0-9a-zA-Z가-힣.,:/\s]')  # 기타 불용어 패턴
    for cleaner in [ptrn_html_code, ptrn_html_tag, ptrn_all_clean]:
        rev = re.sub(cleaner, '', rev)

    re_phrase = r'^([AB]):([a-z]+?)관련/점수:([1-5])점/내용:([0-9a-zA-Z가-힣.,:\s]+?)$'
    ptrn_phrase = re.compile(re_phrase, re.M)
    rev_values = re.findall(ptrn_phrase, rev)
    models, topics, scores, texts = zip(*rev_values)
    df_rev = df({'model': models, 'topic': topics, 'score': scores, 'text': texts})

    df_rev['score'] = pd.to_numeric(df_rev['score'], downcast='integer', errors='ignore')
    df_rev_mean = df_rev.pivot_table(values='score', index='model', columns='topic', aggfunc=mean)
    df_rev_diff = df_rev_mean.diff(periods=-1)
    topic_diff_max = df_rev_diff.loc['A', :].idxmax()  # B대비 A의 성과가 가장 좋은 토픽 탐색
    topic_diff_min = df_rev_diff.loc['A', :].idxmin()  # B대비 A의 성과가 가장 나쁜 토픽 탐색

    writer = pd.ExcelWriter(rst_file_path, engine='xlsxwriter')  # 엑셀 파일 객체 생성
    df_rev_mean.to_excel(writer, sheet_name='score_mean')
    df_rev_diff.to_excel(writer, sheet_name='score_diff')

    m_chart = writer.book.add_chart({'type': 'radar'})  # 토픽별 평균 점수로 방사형 차트 생성
    m_cat = ['score_mean', 0, 1, 0, 5]
    m_val_a = ['score_mean', 1, 1, 1, 5]
    m_val_b = ['score_mean', 2, 1, 2, 5]
    m_chart.add_series({'name': 'A', 'categories': m_cat, 'values': m_val_a})
    m_chart.add_series({'name': 'B', 'categories': m_cat, 'values': m_val_b})
    m_chart.set_title({'name': '토픽별 점수 평균'})
    writer.sheets['score_mean'].insert_chart(3, 0, m_chart)

    d_chart = writer.book.add_chart({'type': 'column'})  # 토픽별 평균 점수 차이로 차트 생성
    d_cat = ['score_diff', 0, 1, 0, 5]
    d_val = ['score_diff', 1, 1, 1, 5]
    d_chart.add_series({'name': 'A-B', 'categories': d_cat, 'values': d_val})
    d_chart.set_title({'name': '토픽별 점수 평균 차이 (A-B)'})
    writer.sheets['score_diff'].insert_chart(2, 0, d_chart)

    def get_kwds(x):
        okt = Okt()  # 형태소 분석 객체 생성
        kwds = okt.pos(x, norm=True, stem=True)
        kwds_filtered = [x for x, y in kwds if y in ['Noun', 'Adjective', 'Verb']]
        return kwds_filtered

    df_rev.loc[:, 'kwd'] = df_rev.loc[:, 'text'].map(get_kwds)
    df_rev.to_excel(writer, sheet_name='reviews')

    for topic in [topic_diff_max, topic_diff_min]:
        for model in ['A', 'B']:
            df_filtered = df_rev[(df_rev['model'] == model) & (df_rev['topic'] == topic)]
            list_kwd = df_filtered['kwd'].sum()
            dict_kwd_cnt = Counter(list_kwd)
            df_kwd_cnt = df({'kwd': list(dict_kwd_cnt.keys()), 'cnt': list(dict_kwd_cnt.values())})
            df_kwd_cnt = df_kwd_cnt.sort_values(by='cnt', ascending=False)
            sheet_name = f'kwd_cnt_{model}_{topic}'
            df_kwd_cnt.to_excel(writer, sheet_name=sheet_name, index=False)
            wc = WC(max_words=40, font_path=font_file_path, background_color='white')
            wc.generate_from_frequencies(dict_kwd_cnt)
            rst_png_file_path = f'./sample/kwd_cnt_{model}_{topic}.png'
            wc.to_file(rst_png_file_path)
            writer.sheets[sheet_name].insert_image(3, 4, rst_png_file_path)

    writer.save()

if __name__ == '__main__':

    cdj_analysis('./sample/고객_행동.xlsx', './sample/고객_행동_분석.xlsx')
    review_analysis('./sample/구매_후기.txt', './sample/구매_후기_분석.xlsx')