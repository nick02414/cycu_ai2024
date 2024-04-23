#https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/
#https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/20240416/00

import os
import requests
import pandas as pd
from datetime import datetime, timedelta

def download_and_save(url, directory, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 如果請求失敗，這將引發一個異常
        os.makedirs(directory, exist_ok=True)
        with open(os.path.join(directory, filename), 'wb') as f:
            f.write(response.content)
    except requests.exceptions.HTTPError as err:
        print(f"Error: {err} for url: {url}")

import datetime

# 定義基礎 URL 和日期範圍
base_url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/"
start_date = datetime.date(2024, 4, 16)
end_date = datetime.date(2024, 4, 22)

# 定義每小時的分鐘數
minutes = [f"{i:02d}" for i in range(0, 60, 5)]

# 對於日期範圍內的每一天
current_date = start_date
while current_date <= end_date:
    # 對於每個小時和分鐘
    for hour in range(24):
        for minute in minutes:
            # 生成 URL 和檔案名稱
            date_str = current_date.strftime("%Y%m%d")
            time_str = f"{hour:02d}{minute}00"
            url = f"{base_url}{date_str}/{hour:02d}/TDCS_M04A_{date_str}_{time_str}.csv"
            filename = f"TDCS_M04A_{date_str}_{time_str}.csv"

            # 下載和保存檔案
            download_and_save(url, '期中作業/資料', filename)

    # 移到下一天
    current_date += datetime.timedelta(days=1)