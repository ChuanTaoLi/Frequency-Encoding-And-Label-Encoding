import pandas as pd

data1 = pd.read_excel(r'D:\0文献整理\网络入侵检测\KDD99\KDDTrain.xlsx')
data2 = pd.read_excel(r'D:\0文献整理\网络入侵检测\KDD99\KDDTest_without_unkown.xlsx')

df1 = data1[['protocol_type', 'service', 'flag']].copy()
df2 = data2[['protocol_type', 'service', 'flag']].copy()

'''频率编码'''
for col in df1.columns:
    df1[col + '_frequency_encoded'] = df1[col].map(df1[col].value_counts(normalize=True))

for col in df2.columns:
    df2[col + '_frequency_encoded'] = df2[col].map(df2[col].value_counts(normalize=True))

df1.to_excel('KDDTrain_frequency_encoded.xlsx', index=False)
df2.to_excel('KDDTest_frequency_encoded.xlsx', index=False)
