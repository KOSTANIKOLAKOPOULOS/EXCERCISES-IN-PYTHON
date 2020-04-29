#INSPECTOR LEKAS
import pandas as pd
df = pd.read_excel('new.xls')
print(df[['TIME','2017','2018']][13:15])
print(df.iloc[10])
#for index,row in df.iterrows():
#	print(index,row)
#print(df.loc[df['2008'] > 70])
#print(df.sort_values('2007',ascending=False))
#df['test']='test'
#print(df)
#df['M.O.']=df.iloc[:,1:13].mean(axis=1)
#print(df)
df['MAX']=df.iloc[:,1:13].max(axis=1)
print(df)
from matplotlib import pyplot as plt
x=[3,4,5,6,7]
y=[33,44,45,55,66]
plt.bar(x,y)
plt.show()