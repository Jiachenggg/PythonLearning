"""
    数据可视化案例：全国疫情地图
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *

f = open("D:/resource/PycharmProjects/PythonLearning/test_txt/疫情.txt", "r", encoding="UTF-8")
data = f.read()
f.close()

# 将JSON字符串转换为Python字典
data_dict = json.loads(data)

# 从字典中取出各省份的数据
province_data_list = data_dict["areaTree"][0]["children"]

# 绘图所需要的数据列表
data_list = []
for province_data in province_data_list:
    province_name = province_data["name"] + "省"
    province_confirm = province_data["total"]["confirm"]
    data_list.append((province_name, province_confirm))

# 创建地图对象
map = Map()
map.add("中国各省份疫情分布", data_list, "china")

# 设置全局配置项set_global_opts
map.set_global_opts(
    title_opts=TitleOpts(title="全国新冠肺炎疫情地图", pos_left="center", pos_bottom="1%"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1-9", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "10-99", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "label": "100-500", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "1-9", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "label": "10-99", "color": "#CC3333"},
            {"min": 100000, "label": "100-500", "color": "#990033"}
        ]
    )
)

# 调用render方法，生成地图
map.render("全国新冠肺炎疫情地图.html")
