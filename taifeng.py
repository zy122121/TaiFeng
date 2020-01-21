import pandas as pd
import numpy as ny
import matplotlib.pyplot as plt
import geopandas
import seaborn as sns
from urllib import request
import re
from shapely.geometry import LineString,Point
from urllib import parse
from urllib.request import urlopen
import hashlib
import json
from wordcloud import WordCloud
import warnings

#warnings.filterwarning('ignore')
# 数据输出时对齐列名
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
# 显示中文标签
plt.rc('font', family='SimHei', size=18)
sns.set()
#%matplotlib inline

#加载数据集
data=pd.read_excel(r'case\taifeng.xlsx')
#数据规格
# print(data.shape)
# print(data.tail(10))

# 地理编码，通过登陆地址信息得到经、纬度
def get_location1(address):
    my_ak = '8aWRTO1ROUesxpZ6OYCuhzPXmGtourz6'
    url = 'http://api.map.baidu.com/geocoding/v3/'
    output = 'json'
    address = quote(address)
    uri = url + '?' + 'address=' + address + '&output=' + output + '&ak=' + my_ak
    req = request.urlopen(uri)
    res = req.read().decode("utf-8")
    temp = json.loads(res)
    l0g = temp['result']['location']['lng']
    lat = temp['result']['location']['lat']
    return(lat,lon)

# 添加经、纬度字段
data['coor']=dtat['登陆地点'].apply(lambda x:get_location1(x))
data['lat']=data['coor'].apply(lambda x:list(x)[0])
data['lon']=data['coor'].apply(lambda x:list(x)[1])

# 地理逆编码，通过经纬度获取省、市、县区三级单位