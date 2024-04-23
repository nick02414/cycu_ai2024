import pandas as pd

# 讀取 CSV 文件，使用 'big5' 編碼，跳過第一行
data = pd.read_csv('/workspaces/cycu_ai2024/20240409/地震活動彙整_638482860699678349.csv', encoding='big5', skiprows=1)

# 將 '地震時間' 列轉換為 datetime 對象
data['地震時間'] = pd.to_datetime(data['地震時間'], format='%Y/%m/%d %H:%M')

# 選擇特定時間範圍的數據
start_time = pd.to_datetime('2024/4/3 0:00:00')
end_time = pd.to_datetime('2024/4/9 23:59:59')
selected_data = data[(data['地震時間'] >= start_time) & (data['地震時間'] <= end_time)]

# 選擇 '地震時間'，'經度'，'緯度'，'規模' 列
selected_columns = selected_data[['地震時間', '經度', '緯度', '規模']]

# 打印選擇的數據
print(selected_columns)

import folium

# 創建一個地圖對象，設置初始地點和縮放級別
m = folium.Map(location=[24.5, 121], zoom_start=7)

# 從 DataFrame 中獲取經緯度數據和地震時間、規模數據
locations = selected_columns[['緯度', '經度']].values.tolist()
magnitudes = selected_columns['規模'].values.tolist()

import pandas as pd
# 假設 '地震時間' 列是以 UNIX 時間戳（秒）來表示的
selected_columns['地震時間'] = pd.to_datetime(selected_columns['地震時間'], unit='s')

# 現在你可以像之前那樣使用 strftime 方法了
times = selected_columns['地震時間'].dt.strftime("%Y-%m-%d %H:%M:%S").values.tolist()

# 在地圖上繪製點
for i in range(len(locations)):
    folium.Marker(locations[i], popup=f"地震時間: {times[i]}, 規模: {magnitudes[i]}").add_to(m)

# 顯示地圖
m.save('/workspaces/cycu_ai2024/20240409/earthquake_marker_map.html')

# 顯示地圖
m.save('/workspaces/cycu_ai2024/20240409/earthquake_marker_map.html')