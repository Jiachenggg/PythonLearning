from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

f = open("D:/resource/PycharmProjects/PythonLearning/test_txt/1960-2019全球GDP数据.csv", "r",
         encoding="GB2312")  # ANSI编码
data_lines = f.readlines()
f.close()
# 删除第一行数据
data_lines.pop(0)

data_dict = {}
# { 1960: [ [美国, 123], [中国,321], ......  ], 1961: [ [美国, 123], [中国,321], ......  ], ...... }
for line in data_lines:
    year = int(line.split(",")[0])
    country = line.split(",")[1]
    gdp = float(line.split(",")[2])
    # 判断字典里有无指定的key
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

timeline = Timeline({"theme": ThemeType.ESSOS})
# 排序年份
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    # 取出本年份GDP前8的国家
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1] / 100000000)

    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8GDP数据")
    )

    timeline.add(bar, str(year))

timeline.add_schema(
    play_interval=500,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)

timeline.render("1960-2019全球GDP前8国家数据.html")
