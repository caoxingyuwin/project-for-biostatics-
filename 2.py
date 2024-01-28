import pandas as pd
from scipy.stats import fisher_exact

#
data = pd.read_csv("/Volumes/a/working/127/NS_workshop_data.csv")

# 層別変数
strata_vars = ["AGEGR1N", "PSCTGR1N", "BILIGR1N"]

# 第一層
for var1 in data[strata_vars[0]].unique():
    print("第一層変数:", var1)
    
    # 第二层分层变量
    for var2 in data[strata_vars[1]].unique():
        print("第二層変数:", var2)
        
        # 第三层分层变量
        for var3 in data[strata_vars[2]].unique():
            print("第三層変数:", var3)
            
            # 根据分层组合筛选数据
            df_strata = data[(data[strata_vars[0]] == var1) &
                             (data[strata_vars[1]] == var2) &
                             (data[strata_vars[2]] == var3)]
            
            # 构造 2x2 的列联表
            observed = [[sum((df_strata["TRT01P"] == "HISTORICAL") & (df_strata["CNSR"] == 1)),
                         sum((df_strata["TRT01P"] == "HISTORICAL") & (df_strata["CNSR"] == 0))],
                        [sum((df_strata["TRT01P"] == "NS-2024") & (df_strata["CNSR"] == 1)),
                         sum((df_strata["TRT01P"] == "NS-2024") & (df_strata["CNSR"] == 0))]]
            
            # 进行 Fisher's Exact Test
            odds_ratio, p_value = fisher_exact(observed)
            
            # Fisher's Exact Test 结果
            print("Fisher's Exact Test 結果:")
            print("OR値（Odds Ratio）:", odds_ratio)
            print("p 値:", p_value)
            print()


'''
結果
第一層変数: 2
第二層変数: 2
第三層変数: 1
Fisher's Exact Test 結果:
OR値（Odds Ratio）: 0.39326173311755186
p 値: 0.01049267633110287

第三層変数: 2
Fisher's Exact Test 結果:
OR値（Odds Ratio）: 0.41263940520446096
p 値: 0.09318186886030871

第三層変数: 3
Fisher's Exact Test 結果:
OR値（Odds Ratio）: 0.6756756756756757
p 値: 0.5101124462967905

第二層変数: 1
第三層変数: 1
Fisher's Exact Test 結果:
OR値（Odds Ratio）: 0.9506172839506173
p 値: 1.0

第三層変数: 2
Fisher's Exact Test 結果:
OR値（Odds Ratio）: inf
p 値: 0.5841120579880498

第三層変数: 3
Fisher's Exact Test 結果:
OR値（Odds Ratio）: inf
p 値: 1.0

第一層変数: 1
第二層変数: 2
第三層変数: 1
Fisher's Exact Test 結果:
OR値（Odds Ratio）: 0.3849535080304311
p 値: 0.009666484392849417

第三層変数: 2
Fisher's Exact Test 結果:
OR値（Odds Ratio）: 0.23109243697478993
p 値: 0.005505290787556993

第三層変数: 3
Fisher's Exact Test 結果:
OR値（Odds Ratio）: 0.19431988041853512
p 値: 0.013990284323687662

第二層変数: 1
第三層変数: 1
Fisher's Exact Test 結果:
OR値（Odds Ratio）: 0.192090395480226
p 値: 0.012424587543466778

第三層変数: 2
Fisher's Exact Test 結果:
OR値（Odds Ratio）: nan
p 値: 1.0

第三層変数: 3
Fisher's Exact Test 結果:
OR値（Odds Ratio）: nan
p 値: 1.0
'''