import folium
import pandas as pd

import pandas as pd
from sodapy import Socrata


client = Socrata("data.melbourne.vic.gov.au", None)


CPBL = client.get("vh2v-4nfs", limit=2000)  #CPBL:CarParkBayLocation
CPBL_df = pd.DataFrame.from_records(CPBL)

CPBR = client.get("ntht-5rk7", limit=20000)#CPBR:Car Park Bay Restrictions
CPBR_df = pd.DataFrame.from_records(CPBR)


#*****
merge_df=pd.merge(CPBL_df,CPBR_df,left_on='bay_id',right_on='bayid', how='left')
#merge_df.isnull().any()
#merge_df.info()
df=merge_df.iloc[:,[0,1,2,4,5,9,10,11,12,13,16,17,18]]
df[['lat','lon','disabilityext1','duration1']].apply(pd.to_numeric)

def mark_map(data):
    """
    带有标注的地图
    :param data:
    :return:
    """
    # 地图制作
    myMap = folium.Map(location=[-37.82, 144.95], zoom_start=14)

    for i in range(len(data)):
        # 自定义 popup 内容
        test = folium.Html(
            '<b>bay_id:{}</b></br> <b>statues:{}</b></br> <b>description:{}</b></br> <b>effectiveonph:{}</b></br> '.format(data.iloc[i]['bay_id'], data.iloc[i]['status'], data.iloc[i]['description1'],data.iloc[i]['effectiveonph1']),
            script=True)
        
        popup = folium.Popup(test)
        
        if df.iloc[i]['status']=='Unoccupied':
            icon=folium.Icon(color='red', icon='info-sign')
        else:
            icon=folium.Icon(color='blue', icon='ok-sign')
        
        folium.Marker([data.iloc[i]['lat'], data.iloc[i]['lon']], popup=popup,icon=icon).add_to(myMap)

    # 保存地图
    myMap.save('testMap.html')

#if __name__ == '__main__':
mark_map(df)