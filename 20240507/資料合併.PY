import os
import pandas as pd
import requests
import io

#設定目錄路徑/workspaces/cycu_ai2024/20240507/資料
directory = r"/workspaces/cycu_ai2024/20240507/資料"

# 獲取目錄下的所有檔案名稱
filenames = os.listdir(directory)


# 讀取每個 CSV 檔案，並將它們存儲在一個列表中
dfs = [pd.read_csv(f"{directory}/{filename}") for filename in filenames if filename.endswith('.csv')]

# 檢查 dfs 是否為空
if dfs:
    # 依照欄位名稱合併所有的 DataFrame，欄位名稱如下 TimeInterval、GantryFrom、GantryTo、VehicleType、SpaceMeanSpeed、交通量
    df = pd.concat(dfs, ignore_index=True)

    # 將合併後的 DataFrame 寫入到一個新的 CSV 檔案並存於此位置/workspaces/cycu_ai2024/20240507
    df.to_csv(r"/workspaces/cycu_ai2024/20240507/資料.csv", index=False)
else:
    print("在指定的目錄下沒有找到任何 CSV 檔案。")