import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests
import pandas as pd
from io import StringIO

# 網頁 URL
base_url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/20240325/"

# 儲存所有的 DataFrame
dfs = []

# 遍歷每個小時
for hour in range(24):
    # 遍歷每個五分鐘的時間段
    for minute in range(0, 60, 5):
        # 建立 URL
        url = f"{base_url}{str(hour).zfill(2)}/TDCS_M04A_20240325_{str(hour).zfill(2)}{str(minute).zfill(2)}00.csv"
        
        # 嘗試下載 CSV 檔案
        try:
            response = requests.get(url, verify=False)
            df = pd.read_csv(StringIO(response.text), usecols=[0, 1, 2, 3, 4, 5], 
                             names=['時間', '上游偵測站編號', '下游偵測站編號', '車種', '中位數旅行時間', '交通量'], 
                             index_col=0, parse_dates=True)
            dfs.append(df)
        except Exception as e:
            print(f"Failed to download {url}: {e}")

# 合併所有的 DataFrame
df = pd.concat(dfs,axis=0)

# 依照索引排序
df.sort_index(inplace=True)

# 輸出為一個新的 CSV 檔案
df.to_csv("C:\\Users\\User\\Desktop\\cycu_ai2024\\20240326\\output5.csv")

  