import pandas as pd
import numpy as np
'''
df_cctv_col
['기관명', '소계', '2013년도 이전', '2014년', '2015년', '2016년']
df_pop_col
['구별', '인구수', '한국인', '외국인', '고령자']
cctv 소계를 기준으로 오름차순
'''

ctx ='../data/'
df_cctv=pd.read_csv(ctx+'CCTV_in_Seoul.csv')
df_pop=pd.read_excel(ctx+'population_in_Seoul.xls'
                  ,encoding='utf-8'
                  ,header=2
                  ,usecols='B,D,G,J,N')


df_cctv_col = df_cctv.columns
df_pop_col = df_pop.columns

df_cctv.rename(columns={df_cctv.columns[0]:'구별'},inplace=True)
#inplace=True -> 실제 변수의 내용을 바꿔라

df_pop.rename(columns={df_pop.columns[0]:'구별'
                ,df_pop.columns[1]:'인구수'
                ,df_pop.columns[2]:'한국인'
                ,df_pop.columns[3]:'외국인'
                ,df_pop.columns[4]:'고령자'},inplace=True)

#문제 1: df_cctv 를 소계 기준 오름차순 정렬
#답 1: df_cctv= df_cctv.sort_index(by='소계',ascending=False)
#print(df_cctv)

#문제 2: df_pop에서 0번 행 삭제
# 답 2:
#df_pop.drop([0],inplace=True)
#print(df_pop)

#문제 3: df_pop에서 구별 기준 중복 제거
#답 3: df_pop=df_pop.duplicated()
#print(df_pop)
#df_pop['구별'].unique()

#문제 4: df_pop에서 null 체크 (null 있는지 여부)
#답 4: df_pop=df_pop.isna()
#print(df_pop)
#df_pop[df_pop['구별'].isnull()]
#null 26번 행 삭제
#df_pop.drop([26],inplace=True)
#print(df_pop)
#문제 5: df_pop에서 인구수 기준 오름차순 정렬
#답 5: df_pop = df_pop.sort_index(by='인구수',ascending=True)
#print(df_pop)

#문제 6: df_cctv에서 '2013년도 이전','2014년','2015년','2015년','2016년' 열 삭제 -> df_cctv에서 '구별','소계'만 남김
#df_cctv.drop(['2013년도 이전', '2014년', '2015년', '2016년'],1,inplace=True)
#print((df_cctv))

df_pop.drop([0],inplace=True)
df_pop['구별'].unique()
df_pop[df_pop['구별'].isnull()]
df_pop.drop([26],inplace=True)
df_pop['외국인비율']=(df_pop['외국인']/df_pop['인구수'])*100
df_pop['고령자비율']=(df_pop['고령자']/df_pop['인구수'])*100
df_cctv.drop(['2013년도 이전', '2014년', '2015년', '2016년'],1,inplace=True)

df_cctv_pop = pd.merge(df_cctv,df_pop,on='구별')

'''
r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
'''

#np.corrcoef()
df_cctv_pop.set_index('구별',inplace=True)
cor1=np.corrcoef(df_cctv_pop['고령자비율'],df_cctv_pop['소계'])
cor2=np.corrcoef(df_cctv_pop['외국인비율'],df_cctv_pop['소계'])

#print("고령자비율 상관계수 {} \n 외국인비율 상관계수 {}"
      #.format(cor1,cor2))

df_cctv_pop.to_csv(ctx+'cctv_pop.csv')
