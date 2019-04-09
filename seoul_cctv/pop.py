import pandas as pd

ctx ='../data/'
csv=ctx+'CCTV_in_Seoul.csv'
xls=ctx+'population_in_Seoul.xls'
cctv_data = pd.read_csv(csv)
pop_data = pd.read_excel(xls)

print(pop_data.head())
print(cctv_data.head())