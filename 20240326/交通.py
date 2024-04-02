import requests

url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/20240325/00/"

response = requests.get(url)

if response.status_code == 200:
    # 將網頁內容解析或處理的程式碼
    # 這裡可以使用 BeautifulSoup 或其他解析庫來處理網頁內容
    # 例如：
    # from bs4 import BeautifulSoup
    # soup = BeautifulSoup(response.text, 'html.parser')
    # ... 處理網頁內容的程式碼 ...
    pass
else:
    print("無法取得網頁內容，請檢查網址是否正確或網路連線是否正常。")
# 找url網頁內容裡的所有歷史資料庫檔案
import os
from bs4 import BeautifulSoup

# 解析網頁內容
soup = BeautifulSoup(response.text, 'html.parser')
# 找到所有的連結元素
links = soup.find_all('a')

# 建立一個空的列表來存放檔案名稱
file_names = []

# 逐一檢查連結元素
for link in links:
    # 取得連結的 href 屬性值
    href = link.get('href')
    # 如果 href 屬性值是以 .csv 結尾的檔案
    if href.endswith('.csv'):
        # 將檔案名稱加入到列表中
        file_names.append(href)

# 列印所有找到的檔案名稱
for file_name in file_names:
    print(file_name)
    # 下載檔案
    file_url = url + file_name
    response = requests.get(file_url)
    if response.status_code == 200:
        # 將檔案內容寫入本地檔案
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"已下載檔案：{file_name}")
    else:
        print(f"無法下載檔案：{file_name}")

