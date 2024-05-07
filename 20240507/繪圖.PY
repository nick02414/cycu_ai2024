import os
import pandas as pd
import requests
import io
import matplotlib.pyplot as plt

# 路徑設定
data_path = r"/workspaces/cycu_ai2024/20240507"
input_file = os.path.join(data_path, "資料.csv")
output_file = os.path.join(data_path, "資料2.csv")

# 函數定義
def gantry_to_numeric(gantry):
    if gantry[-1] == 'N':
        return int(gantry[3:7])*10 
    elif gantry[-1] == 'S':
        return int(gantry[3:7])*10 + 1

def speed_to_category(speed):
    if pd.isnull(speed):
        return 0
    elif speed <= 20:
        return 1
    elif speed <= 39:
        return 2
    elif speed <= 59:
        return 3
    elif speed <= 79:
        return 4
    else:
        return 5

# 讀取 CSV 檔案
df = pd.read_csv(input_file)

# 保留 vehicleType 為 31 和 GantryFrom 開頭前三碼為01F 的所有資料
df = df[(df["VehicleType"] == 31) & (df["GantryFrom"].str.startswith("01F"))]

# 將處理後的資料寫存入 output_file
df.to_csv(output_file, index=False)

# 讀取 CSV 檔案
df = pd.read_csv(output_file)

# 將 TimeInterval 欄位轉換成數值型態 ( x軸 )
df['TimeInterval'] = pd.to_datetime(df['TimeInterval']).apply(lambda x: x.hour * 12 + x.minute // 5)

# 將 GantryFrom、GantryFrom 欄位轉換成數值型態 ( y軸 )
df['GantryFrom'] = df['GantryFrom'].apply(gantry_to_numeric)
df['GantryTo'] = df['GantryTo'].apply(gantry_to_numeric)

# 將兩個欄位合併成一個欄位(將gantryfrom * 100000 與 gantryto 相加)，命名為 GantryFromTo  (y軸)
df['GantryFromTo'] = df['GantryFrom'] * 100000 + df['GantryTo']

# 將速度轉換成類別型態，命名為 SpaceMeanSpeed ( 顏色 )
df['SpaceMeanSpeed'] = df['SpaceMeanSpeed'].apply(speed_to_category)

# 假設你的 DataFrame 叫做 df
fig = plt.figure(figsize=(20, 12))  # 改變這裡的數值以放大或縮小圖形
ax = fig.add_subplot(111, projection='3d')

# 創建一個顏色映射
color_map = {0: 'white', 1: 'purple', 2: 'red', 3: 'orange', 4: 'yellow', 5: 'green'}
df['color'] = df['SpaceMeanSpeed'].map(color_map)

# 繪製散點圖
scatter = ax.scatter(df['TimeInterval'], df['GantryFromTo'], df['TrafficVolume'], c=df['color'])

# 設置圖表標題和軸標籤
ax.set_title('里程、交通量、速度、時間')
ax.set_xlabel('TimeInterval')
ax.set_ylabel('GantryFromTo')
ax.set_zlabel('TrafficVolume')

# 儲存圖片20240507
plt.savefig(os.path.join(data_path, "20240507.png"))