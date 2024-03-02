from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType

bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GDP", [3000, 2000, 1000], label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP", [5000, 5000, 3000], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "英国"])
bar3.add_yaxis("GDP", [8000, 7000, 6000], label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

# 创建时间线对象
timeline = Timeline({"theme": ThemeType.ESSOS})

# 在时间线内添加柱状图对象
timeline.add(bar1, "2020")
timeline.add(bar2, "2021")
timeline.add(bar3, "2022")

# 自动播放设置
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

# 使用timeline对象生成图，而不是bar对象
timeline.render("基础时间线柱状图.html")
