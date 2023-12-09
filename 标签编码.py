import pandas as pd
from sklearn.preprocessing import LabelEncoder

data1 = pd.read_excel(r'D:\0文献整理\网络入侵检测\KDD99\KDDTrain.xlsx')
data2 = pd.read_excel(r'D:\0文献整理\网络入侵检测\KDD99\KDDTest_without_unkown.xlsx')

'''标签编码'''
label_encoder = LabelEncoder()
df1 = pd.DataFrame()
df2 = pd.DataFrame()

df1['Attack_Types'] = label_encoder.fit_transform(data1['Attack_Types'])
df2['Attack_Types'] = label_encoder.transform(data2['Attack_Types'])

df1.to_excel('KDDTrain_label_encoded.xlsx', index=False)
df2.to_excel('KDDTest_label_encoded.xlsx', index=False)
