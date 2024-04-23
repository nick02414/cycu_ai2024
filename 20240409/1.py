import pandas as pd

# 讀取 CSV 文件，使用 'big5' 編碼，跳過第一行
data = pd.read_csv('/workspaces/cycu_ai2024/20240409/地震活動彙整_638482860699678349.csv', encoding='big5', skiprows=1)

# 打印所有的列名
print(data.columns)