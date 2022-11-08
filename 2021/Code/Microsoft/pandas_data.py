import pandas

df = pandas.read_csv('Code\Microsoft\export_file.csv',index_col='Description',header=0)

df.to_csv('hrdata_modified.csv')
print(df)