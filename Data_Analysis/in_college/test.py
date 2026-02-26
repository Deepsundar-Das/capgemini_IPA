import pandas as pd
#%%
s=pd.Series({'a':1,'b':2})
#%%
print(s.values)
print(s.size)
print(s.dtype)
print(s.mean())
#%%
print(s.std())
print(s.value_counts())
pd.DataFrame([1,2],[3,4])
#%%
pd.DataFrame({'a':[1,2],'b':[3,6]})
#%%
df = pd.read_csv("WineQT.csv")
df.head

#%%
df.head(5)
#%%
df.sample(5)