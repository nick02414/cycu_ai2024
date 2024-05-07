# 設定 CSV 檔案的 URL
# 以迴圈方式幫我從 https://tisvcloud.freeway.gov.tw/history/TDCS/M03A/20240429/00/TDCS_M03A_20240429_000000.csv  https://tisvcloud.freeway.gov.tw/history/TDCS/M03A/20240429/00/TDCS_M03A_20240429_000500.csv 到 https://tisvcloud.freeway.gov.tw/history/TDCS/M03A/20240429/23/TDCS_M03A_20240429_235500.csv 這個網址下載所有的檔案
import os
import pandas as pd
import requests
import io


for i in range(0, 24):
    for j in range(0, 60, 5):
        # 設定 URL
        url = f"https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/20240429/{i:02d}/TDCS_M05A_20240429_{i:02d}{j:02d}00.csv"
        # 下載檔案
        response = requests.get(url)
        # 讀取 CSV 檔案，並設定欄位名稱
        df = pd.read_csv(io.StringIO(response.content.decode('utf-8')), names=["TimeInterval", "GantryFrom", "GantryTo", "VehicleType", "SpaceMeanSpeed", "TrafficVolume"])
        # 將處理後的資料寫存入 /workspaces/cycu_ai2024/20240507/資料
        df.to_csv(f"/workspaces/cycu_ai2024/20240507/資料/{i:02d}{j:02d}.csv", index=False)
        print(f"{i:02d}{j:02d}.csv 下載並處理成功")

# 設定目錄路徑/workspaces/cycu_ai2024/20240507/資料
directory = r"/workspaces/cycu_ai2024/20240507/資料"

# 獲取目錄下的所有檔案名稱
filenames = os.listdir(directory)

# 讀取每個 CSV 檔案，並將它們存儲在一個列表中
dfs = [pd.read_csv(f"{directory}\\{filename}") for filename in filenames if filename.endswith('.csv')]

# 檢查 dfs 是否為空
if dfs:
    # 依照欄位名稱合併所有的 DataFrame，欄位名稱如下 TimeInterval、GantryFrom、GantryTo、VehicleType、SpaceMeanSpeed、交通量
    df = pd.concat(dfs, ignore_index=True)

    # 將合併後的 DataFrame 寫入到一個新的 CSV 檔案並存於此位置/workspaces/cycu_ai2024/20240507
    df.to_csv(r"/workspaces/cycu_ai2024/20240507/資料.csv", index=False)
else:
    print("在指定的目錄下沒有找到任何 CSV 檔案。")