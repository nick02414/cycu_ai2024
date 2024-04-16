import pandas as pd

data = pd.read_csv('/workspaces/cycu_ai2024/期中考/地震活動彙整_638488882359017938.csv', encoding='big5', skiprows=1)
data['地震時間'] = pd.to_datetime(data['地震時間'])
filtered_data = data[(data['地震時間'] >= '2024-04-03 00:00:00') & (data['地震時間'] <= '2024-04-09 23:59:59')]
filtered_data = filtered_data.drop(columns=['編號'])
print(filtered_data.to_string(index=False))

import folium
from folium.plugins import TimestampedGeoJson

# 創建一個地圖，設定初始的經緯度和縮放等級
m = folium.Map(location=[24, 121], zoom_start=7)

# 創建一個用於存儲地震數據的列表
data = []

# 在地圖上添加標記
for index, row in filtered_data.iterrows():
    data.append({
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [row['經度'], row['緯度']]
        },
        'properties': {
            'time': row['地震時間'].isoformat(),
            'style': {'color' : 'red'},
            'icon': 'circle',
            'iconstyle':{
                'fillColor': 'red',
                'fillOpacity': 0.6,
                'stroke': 'false',
                'radius': 5
            },
            'popup': f"地震時間: {row['地震時間']}, 經度: {row['經度']}, 緯度: {row['緯度']}, 規模: {row['規模']}, 深度: {row['深度']}, 位置: {row['位置']}"
        }
    })

# 添加時間滑塊
TimestampedGeoJson(
    {'type': 'FeatureCollection', 'features': data},
    period='PT1H',
    add_last_point=True,
    auto_play=False,
    loop=False,
    max_speed=1,
    loop_button=True,
    date_options='YYYY/MM/DD HH:mm:ss',
    time_slider_drag_update=True
).add_to(m)

#儲存地圖
m.save('/workspaces/cycu_ai2024/期中考/地震活動.html')