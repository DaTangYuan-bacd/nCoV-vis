from matplotlib import pyplot
from math import tanh
from _2019nCoVData import *

pyplot.plot(天数, 感染人数, 'ro')
pyplot.plot(天数, 治愈人数, 'go')
pyplot.plot(天数, [感染人数[i] - 治愈人数[i] for i in range(len(天数))], 'bo')

days = 60

def get_sicked(day):
    #2019nCoV information
    a = 0.486
    start = 40
    end = 51
    b = 1880

    return (a + 1) ** (day - start) if day < end else b * (day - end + 2)
    return max(tanh((day - start) / b) * a * b / 2 + a * b / 2, 0)

def get_re_healthy(day):
    #2019nCoV information
    a = 1.9
    start = 80

    return min((a + 1) ** (day - start), get_sicked(day))

xs = list(range(1, days + 1))
sicked_ys = [get_sicked(i) for i in xs]
re_healthy_ys = [get_re_healthy(i) for i in xs]
sick_ys = [sicked_ys[i] - re_healthy_ys[i] for i in range(days)]

pyplot.plot(xs, sicked_ys, 'r-')
pyplot.plot(xs, re_healthy_ys, 'g-')
pyplot.plot(xs, sick_ys, 'b-')
pyplot.show()
