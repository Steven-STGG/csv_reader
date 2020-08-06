pd_mode = pandas.read_csv(f,delimiter="\t")   #read file
pd_mode.to_csv("名字.csv"，index=False)






删除行列：
pd_mode=pd_mode.drop(labels=0)


排序：
pd_mode.sort_values("Equiv.FieldStrength")











Filtering DATA:
pd_mode["Total"] = pd_mode.iloc[:,2:4].sum(axis=1)
print(pd_mode.loc[pd_mode["Packet"] == "CHINA_TELECOM"])  #找packet里所有是chinatelecom

print(pd_mode.loc[(pd_mode["Packet"] == "CHINA_TELECOM") | (pd_mode["Packet"] == "Three") ]) 
#条件索引

b=pd_mode.loc[pd_mode["Packet"].str.contains("CH|Th")]



Conditional Change:
pd_mode.loc[pd_mode["Packet"] == "CHINA_TELECOM","Frequency"] =3



pd_mode.groupby(["Equiv.FieldStrength"]).count()











 # a=pd_mode["Packet"]
                # print(list(a))
                # pd_mode["total"] = pd_mode.iloc[1:,2:4].sum(axis=1)
                # print(pd_mode)
                # print(pd_mode.loc[(pd_mode["Packet"] == "CHINA_TELECOM") | (pd_mode["Packet"] == "Three") ])
                # a=pd_mode.loc[pd_mode["Packet"]=="Three"]
                
                pd_mode=pd_mode.drop(labels=0)
                new_df = pandas.DataFrame(columns=pd_mode.columns)
                # pd_mode.loc[pd_mode["Packet"] == "CHINA_TELECOM","Frequency"] =3
                
            
                print(new_df)