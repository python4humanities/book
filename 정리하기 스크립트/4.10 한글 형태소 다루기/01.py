from konlpy.tag import Okt

okt = Okt()
voc = '냉장고가 필요해 알아보던 중 가격이 제일 적당한 것 같아 구입했어여.'
kwds_pos = okt.pos(voc, norm=True, stem=True)
print(kwds_pos)
# 명사, 형용사, 동사만 선별
kwds_filtered = [x for x, y in kwds_pos if y in ['Noun', 'Adjective', 'Verb']]
print(kwds_filtered)
