_2019_12_8_至今天数 = 57
天数 = list(range(1, _2019_12_8_至今天数 + 1))
感染人数 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 7, 27, 27, 27, 44, 59, 61, 61, 61, 61,
           61, 61, 61, 61, 61, 61, 61, 65, 72, 121, 198, 270, 440, 571, 830, 1287, 1975, 2744, 4515, 5974, 7711,
           9693, 11821, 19544, 21558]
治愈人数 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 34, 38, 49, 51, 60, 103, 124, 243, 331, 361]
平均潜伏期 = 5
#R0 =  [(感染人数[i + 5] / 感染人数[i] - 1) for i in range(_2019_12_8_至今天数 - 1)] + [float('NaN')] * 5

每日增加 = [(感染人数[i] - 感染人数[i - 1]) for i in range(1, _2019_12_8_至今天数)]
R0 = [1.0] + [(每日增加[i + 平均潜伏期] / 感染人数[i]) for i in range(_2019_12_8_至今天数 - 平均潜伏期 - 1)] + [float('NaN')] * 5
print(R0, len(R0))