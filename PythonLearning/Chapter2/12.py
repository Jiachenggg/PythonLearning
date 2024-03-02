from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

bar = Bar()
bar.add_xaxis(["中国", "美国", "英国"])
bar.add_yaxis("GDP", [3000, 2000, 1000], label_opts=LabelOpts(position="right"))
# 反转x轴和y轴
bar.reversal_axis()
bar.render("基础柱状图.html")
