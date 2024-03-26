import requests
import pandas as pd

base_url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/20240325/"

for i in range(0, 24):
    url = base_url + "{:02d}/".format(i)
    for j in range(0, 60, 5 ):
        filename='''TDCS_M04A_20240325_{:02d}{:02d}00.csv'''.format(i,j)
        print(filename)
        res = requests.get(url + filename)
        if res.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(res.content)


filename='''TDCS_M04A_20240325_000000.csv'''
#filename 最後面的數字代表的是小時 分鐘 秒，例如000000代表00:00:00 
#000500 代表 00:05:00
#如果每5分鐘一筆資料，利用迴圈產生檔名
#例如:  TDCS_M04A_20240325_000000.csv
#              TDCS_M04A_20240325_000500.csv
for i in range(0, 1):
    for j in range(0, 60, 5 ):
        filename='''TDCS_M04A_20240325_{:02d}{:02d}00.csv'''.format(i,j)
        print(filename)
        res = requests.get(url + filename)
if res.status_code == 200:
    with open(filename,'wb') as f:
        f.write(res.content)
else:
    print("Failed to download file, status code: ", res.status_code)

# 合併所有的 DataFrame
df = pd.concat(dfs,axis=0)

# 依照索引排序
df.sort_index(inplace=True)

# 輸出為一個新的 CSV 檔案
df.to_csv("C:\\Users\\User\\Desktop\\cycu_ai2024\\20240326\\output5.csv")
