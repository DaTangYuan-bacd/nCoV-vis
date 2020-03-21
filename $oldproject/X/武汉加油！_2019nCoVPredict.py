from matplotlib import pyplot
from _2019nCoVData import *
from predict import *


_2019nCoV感染人数预测器 = 插值器()
_2019nCoV感染人数预测器.加入数据(天数, 感染人数)

plotXs = list(range(1, 60))
plotYs = [_2019nCoV感染人数预测器(i) for i in plotXs]
pyplot.plot(天数, 感染人数, 'r-')
pyplot.plot(plotXs, plotYs)
pyplot.show()
