import numpy as np
import pandas as pd

#导入数据
fpath = r"D:\乱玩python\IAT\IAT被试资料\20.xls"
df1 = pd.read_excel(fpath,header=None)
df = pd.read_excel(fpath)

#记录性别及其他数据
print(df1.iloc[0, 1])
df=df.iloc[1:161]
RightAnswer=df.iloc[:,2].values
Response=df.iloc[:,3].values
RT=df.iloc[:,4].values
RT=1000*(np.array(RT))

#错误率超过20%删除
s=0
for i in range(160):
    #将秒转成毫秒，超过3000ms按照3000ms来记录，低于300ms按照300ms记录
    if RT[i] >=3000:
        RT[i] =3000
    elif RT[i] <=300:
        RT[i] =300
    if RightAnswer[i] != Response[i]:
        s+=1
print(s/160)

#对原始反应数据进行对数处理
for i in range(160):RT[i]=np.log10(RT[i])

#将相容组合不相容组分别进行平均处理，再用不相容减去相容
aver1=np.mean(RT[0:80])
aver2=np.mean(RT[80:160])
aver=aver2-aver1
print(aver)