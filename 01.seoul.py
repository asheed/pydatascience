import pandas as pd

# CCTV_Seoul = pd.read_csv('data/01.CCTV_in_Seoul.csv', encoding='utf-8')
# print(CCTV_Seoul.head())
# print(CCTV_Seoul.columns)
# print(CCTV_Seoul.columns[0])
#
# CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0] : '구별'}, inplace=True)
# print(CCTV_Seoul.head())

pop_seoul = pd.read_excel('data/01.population_in_seoul.xls',
                          header=2,
                          usecols='B, D, G, J, N',
                          encoding='utf-8')
print(type(pop_seoul))
pop_seoul.rename(columns={ pop_seoul.columns[0]: '구별',
                           pop_seoul.columns[1]: '인구수',
                           pop_seoul.columns[2]: '한국인',
                           pop_seoul.columns[3]: '외국인',
                           pop_seoul.columns[4]: '고령자'}, inplace=True)
print(pop_seoul.head())