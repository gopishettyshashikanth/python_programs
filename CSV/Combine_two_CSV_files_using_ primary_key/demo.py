import pandas, sys

df1 = pandas.read_csv('1.csv')
df2 = pandas.read_csv('2.csv')
 
df1.merge(df2, on='ID').to_csv(sys.stdout, index=False)
#df1.merge(df2, on='ID').to_csv('3.csv', index=False)
